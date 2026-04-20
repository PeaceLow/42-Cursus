/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 12:30:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 13:35:22 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "main.h"

static int	all_compiled_enough(t_coder *coders, t_env *env)
{
	int	i;

	if (env->nb_compiles_required <= 0)
		return (0);
	i = 0;
	while (i < env->nb_coders)
	{
		if (coders[i].nb_compiles < env->nb_compiles_required)
			return (0);
		i++;
	}
	return (1);
}

static int	coder_burned_out(t_coder *coder, t_env *env)
{
	long	deadline;
	long	now;

	now = get_timestamp();
	deadline = coder->last_compile_start + env->time_to_burnout;
	return (now >= deadline);
}

static void	log_burnout(t_coder *coder)
{
	long	ts;

	pthread_mutex_lock(&coder->env->print_lock);
	ts = get_timestamp() - coder->env->start_time;
	printf("%ld %d burned out\n", ts, coder->id);
	pthread_mutex_unlock(&coder->env->print_lock);
}

static int	check_burnout(t_coder *coders, t_env *env)
{
	int	i;

	i = 0;
	while (i < env->nb_coders)
	{
		if (coder_burned_out(&coders[i], env))
		{
			stop_sim(env);
			log_burnout(&coders[i]);
			return (1);
		}
		i++;
	}
	return (0);
}

void	*monitor_routine(void *arg)
{
	t_coder	*coders;
	t_env	*env;

	coders = ((t_coder **)arg)[0];
	env = ((t_env **)arg)[1];
	while (!sim_stopped(env))
	{
		usleep(1000);
		if (check_burnout(coders, env))
			break ;
		if (all_compiled_enough(coders, env))
		{
			stop_sim(env);
			break ;
		}
	}
	return (NULL);
}
