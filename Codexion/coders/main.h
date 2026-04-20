/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 10:29:01 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 12:18:19 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef MAIN_H
# define MAIN_H

# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include <string.h>
# include <pthread.h>
# include <sys/time.h>
# include "struct.h"

long	get_timestamp(void);
void	log_status(t_coder *coder, const char *msg);
int		sim_stopped(t_env *env);
void	stop_sim(t_env *env);

void	init_env(t_env *env, char **av);
void	init_coders(t_coder *coders, t_env *env, int nb);
void	cleanup(t_env *env, t_coder *coders);

void	*coder_routine(void *arg);
void	*monitor_routine(void *arg);

void	dongle_take(t_coder *coder, t_dongle *dongle);
void	dongle_release(t_coder *coder, t_dongle *dongle);

int		verify_args(int ac, char **av);
int		ft_strcmp(const char *s1, const char *s2);

#endif