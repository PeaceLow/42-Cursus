/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 10:28:52 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 13:33:09 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "main.h"

void	log_status(t_coder *coder, const char *msg)
{
	long	ts;

	pthread_mutex_lock(&coder->env->print_lock);
	pthread_mutex_lock(&coder->env->stop_lock);
	if (!coder->env->stop_sim)
	{
		ts = get_timestamp() - coder->env->start_time;
		printf("%ld %d %s\n", ts, coder->id, msg);
	}
	pthread_mutex_unlock(&coder->env->stop_lock);
	pthread_mutex_unlock(&coder->env->print_lock);
}

static int	start_threads(t_coder *coders, t_env *env, pthread_t *mon,
	void *mon_args[2])
{
	int	i;

	mon_args[0] = coders;
	mon_args[1] = env;
	if (pthread_create(mon, NULL, monitor_routine, mon_args) != 0)
		return (1);
	i = 0;
	while (i < env->nb_coders)
	{
		if (pthread_create(&coders[i].thread, NULL,
				coder_routine, &coders[i]) != 0)
			return (1);
		i++;
	}
	return (0);
}

static void	wait_and_cleanup(t_env *env, t_coder *coders, pthread_t monitor)
{
	int	i;

	pthread_join(monitor, NULL);
	stop_sim(env);
	i = 0;
	while (i < env->nb_coders)
	{
		pthread_join(coders[i].thread, NULL);
		i++;
	}
	cleanup(env, coders);
}

int	main(int ac, char **av)
{
	t_env		env;
	t_coder		*coders;
	pthread_t	monitor;
	void		*mon_args[2];

	if (verify_args(ac, av))
		return (1);
	init_env(&env, av);
	coders = (t_coder *)malloc(sizeof(t_coder) * env.nb_coders);
	if (!coders)
		return (1);
	init_coders(coders, &env, env.nb_coders);
	if (start_threads(coders, &env, &monitor, mon_args))
	{
		cleanup(&env, coders);
		return (1);
	}
	wait_and_cleanup(&env, coders, monitor);
	return (0);
}
