/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   struct.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 10:51:33 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 13:30:07 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STRUCT_H
# define STRUCT_H

# include <pthread.h>

# define SCHED_FIFO_T	0
# define SCHED_EDF_T	1

typedef struct s_request
{
	int					coder_id;
	long				deadline;
	long				arrival;
	int					active;
	pthread_cond_t		cond;
}	t_request;

typedef struct s_dongle
{
	pthread_mutex_t		mutex;
	long				available_at;
	int					id;
	int					nb_coders;
	t_request			*queue;
	int					queue_size;
	pthread_mutex_t		queue_lock;
}	t_dongle;

typedef struct s_env
{
	int				nb_coders;
	long			time_to_burnout;
	long			time_to_compile;
	long			time_to_debug;
	long			time_to_refactor;
	int				nb_compiles_required;
	long			dongle_cooldown;
	int				scheduler_type;
	long			start_time;
	pthread_mutex_t	print_lock;
	int				stop_sim;
	pthread_mutex_t	stop_lock;
	t_dongle		*dongles;
}	t_env;

typedef struct s_coder
{
	int				id;
	int				nb_compiles;
	long			last_compile_start;
	t_dongle		*left_dongle;
	t_dongle		*right_dongle;
	t_env			*env;
	pthread_t		thread;
}	t_coder;

#endif