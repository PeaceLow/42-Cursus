/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 12:30:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 13:32:24 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "main.h"

long	get_timestamp(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return (tv.tv_sec * 1000L + tv.tv_usec / 1000L);
}

int	sim_stopped(t_env *env)
{
	int	stopped;

	pthread_mutex_lock(&env->stop_lock);
	stopped = env->stop_sim;
	pthread_mutex_unlock(&env->stop_lock);
	return (stopped);
}

void	stop_sim(t_env *env)
{
	pthread_mutex_lock(&env->stop_lock);
	env->stop_sim = 1;
	pthread_mutex_unlock(&env->stop_lock);
}
