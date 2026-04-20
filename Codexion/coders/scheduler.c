/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   scheduler.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 12:30:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 13:34:50 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "main.h"

static int	find_next(t_dongle *d, int type)
{
	int	best;
	int	i;

	best = -1;
	i = -1;
	while (++i < d->nb_coders)
	{
		if (d->queue[i].active)
		{
			if (best == -1)
				best = i;
			else if (type == SCHED_EDF_T
				&& d->queue[i].deadline < d->queue[best].deadline)
				best = i;
			else if (type == SCHED_FIFO_T
				&& d->queue[i].arrival < d->queue[best].arrival)
				best = i;
		}
	}
	return (best);
}

static void	enqueue_coder(t_coder *coder, t_dongle *dongle, int slot)
{
	long	deadline;

	deadline = coder->last_compile_start + coder->env->time_to_burnout;
	pthread_mutex_lock(&dongle->queue_lock);
	dongle->queue[slot].coder_id = coder->id;
	dongle->queue[slot].deadline = deadline;
	dongle->queue[slot].arrival = get_timestamp();
	dongle->queue[slot].active = 1;
	dongle->queue_size++;
	pthread_mutex_unlock(&dongle->queue_lock);
}

static void	wait_dongle(t_coder *coder, t_dongle *dongle, int slot)
{
	long	now;

	while (1)
	{
		now = get_timestamp();
		if (now < dongle->available_at)
		{
			pthread_mutex_unlock(&dongle->queue_lock);
			usleep((dongle->available_at - now) * 1000);
			pthread_mutex_lock(&dongle->queue_lock);
			continue ;
		}
		if (find_next(dongle, coder->env->scheduler_type) == slot)
			break ;
		pthread_cond_wait(&dongle->queue[slot].cond, &dongle->queue_lock);
	}
}

void	dongle_take(t_coder *coder, t_dongle *dongle)
{
	int	slot;

	slot = coder->id - 1;
	enqueue_coder(coder, dongle, slot);
	pthread_mutex_lock(&dongle->mutex);
	pthread_mutex_lock(&dongle->queue_lock);
	wait_dongle(coder, dongle, slot);
	dongle->queue[slot].active = 0;
	dongle->queue_size--;
	pthread_mutex_unlock(&dongle->queue_lock);
	log_status(coder, "has taken a dongle");
}

void	dongle_release(t_coder *coder, t_dongle *dongle)
{
	int	next;

	pthread_mutex_lock(&dongle->queue_lock);
	dongle->available_at = get_timestamp() + coder->env->dongle_cooldown;
	next = find_next(dongle, coder->env->scheduler_type);
	if (next >= 0)
		pthread_cond_signal(&dongle->queue[next].cond);
	pthread_mutex_unlock(&dongle->queue_lock);
	pthread_mutex_unlock(&dongle->mutex);
}
