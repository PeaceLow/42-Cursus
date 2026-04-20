/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 12:30:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 13:30:15 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "main.h"

static void	init_dongle(t_env *env, t_dongle *d, int id)
{
	int	j;

	d->id = id;
	d->available_at = 0;
	d->queue_size = 0;
	d->nb_coders = env->nb_coders;
	d->queue = (t_request *)malloc(sizeof(t_request) * env->nb_coders);
	pthread_mutex_init(&d->mutex, NULL);
	pthread_mutex_init(&d->queue_lock, NULL);
	j = 0;
	while (j < env->nb_coders)
	{
		d->queue[j].active = 0;
		pthread_cond_init(&d->queue[j].cond, NULL);
		j++;
	}
}

void	init_env(t_env *env, char **av)
{
	int	i;

	env->nb_coders = atoi(av[1]);
	env->time_to_burnout = (long)atoi(av[2]);
	env->time_to_compile = (long)atoi(av[3]);
	env->time_to_debug = (long)atoi(av[4]);
	env->time_to_refactor = (long)atoi(av[5]);
	env->nb_compiles_required = atoi(av[6]);
	env->dongle_cooldown = (long)atoi(av[7]);
	if (ft_strcmp(av[8], "edf") == 0)
		env->scheduler_type = SCHED_EDF_T;
	else
		env->scheduler_type = SCHED_FIFO_T;
	env->stop_sim = 0;
	pthread_mutex_init(&env->print_lock, NULL);
	pthread_mutex_init(&env->stop_lock, NULL);
	env->dongles = (t_dongle *)malloc(sizeof(t_dongle) * env->nb_coders);
	i = 0;
	while (i < env->nb_coders)
	{
		init_dongle(env, &env->dongles[i], i);
		i++;
	}
	env->start_time = get_timestamp();
}

void	init_coders(t_coder *coders, t_env *env, int nb)
{
	int	i;

	i = 0;
	while (i < nb)
	{
		coders[i].id = i + 1;
		coders[i].nb_compiles = 0;
		coders[i].last_compile_start = env->start_time;
		coders[i].env = env;
		coders[i].left_dongle = &env->dongles[i];
		coders[i].right_dongle = &env->dongles[(i + 1) % nb];
		i++;
	}
}

void	cleanup(t_env *env, t_coder *coders)
{
	int	i;
	int	j;

	i = 0;
	while (i < env->nb_coders)
	{
		j = 0;
		while (j < env->nb_coders)
		{
			pthread_cond_destroy(&env->dongles[i].queue[j].cond);
			j++;
		}
		pthread_mutex_destroy(&env->dongles[i].mutex);
		pthread_mutex_destroy(&env->dongles[i].queue_lock);
		free(env->dongles[i].queue);
		i++;
	}
	pthread_mutex_destroy(&env->print_lock);
	pthread_mutex_destroy(&env->stop_lock);
	free(env->dongles);
	free(coders);
}
