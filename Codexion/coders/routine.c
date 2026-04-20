/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   routine.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 12:30:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/04/16 09:05:07 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "main.h"

static void	coder_sleep(t_coder *me, long ms)
{
	long	end;

	end = get_timestamp() + ms;
	while (get_timestamp() < end && !sim_stopped(me->env))
		usleep(500);
}

static int	take_dongles(t_coder *me)
{
	if (me->left_dongle == me->right_dongle)
	{
		dongle_take(me, me->left_dongle);
		while (!sim_stopped(me->env))
			usleep(100);
		return (0);
	}
	if (me->left_dongle->id < me->right_dongle->id)
	{
		dongle_take(me, me->left_dongle);
		dongle_take(me, me->right_dongle);
	}
	else
	{
		dongle_take(me, me->right_dongle);
		dongle_take(me, me->left_dongle);
	}
	return (1);
}

static void	release_dongles(t_coder *me)
{
	if (me->left_dongle == me->right_dongle)
	{
		dongle_release(me, me->left_dongle);
		return ;
	}
	if (me->left_dongle->id < me->right_dongle->id)
	{
		dongle_release(me, me->right_dongle);
		dongle_release(me, me->left_dongle);
	}
	else
	{
		dongle_release(me, me->left_dongle);
		dongle_release(me, me->right_dongle);
	}
}

static int	execute_routine(t_coder *me)
{
	take_dongles(me);
	if (sim_stopped(me->env))
	{
		release_dongles(me);
		return (0);
	}
	me->last_compile_start = get_timestamp();
	log_status(me, "is compiling");
	me->nb_compiles++;
	coder_sleep(me, me->env->time_to_compile);
	release_dongles(me);
	if (sim_stopped(me->env))
		return (0);
	log_status(me, "is debugging");
	coder_sleep(me, me->env->time_to_debug);
	if (sim_stopped(me->env))
		return (0);
	log_status(me, "is refactoring");
	coder_sleep(me, me->env->time_to_refactor);
	return (1);
}

void	*coder_routine(void *arg)
{
	t_coder	*me;

	me = (t_coder *)arg;
	while (!sim_stopped(me->env))
	{
		if (!execute_routine(me))
			break ;
	}
	return (NULL);
}
