/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:53:45 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 19:29:26 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef BENCH_H
# define BENCH_H

# include "ft_printf.h"
# include "parser.h"
# include "stack.h"

typedef struct s_bench
{
	int			sa;
	int			sb;
	int			ss;
	int			pa;
	int			pb;
	int			ra;
	int			rb;
	int			rr;
	int			rra;
	int			rrb;
	int			rrr;
	int			total_ops;
	double		disorder;
	t_strategy	strategy_used;
	char		*complexity;
	int			active;
}				t_bench;

double			get_ratio_disordered(t_stack *stack);
void			print_bench(t_bench *bench);
void			init_bench(t_bench *bench, t_args *args);

#endif