/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   instruction.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:22:20 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/06 22:06:51 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef INSTRUCTION_H
# define INSTRUCTION_H
# include "stack.h"
# include "ft_printf.h"
# include "operators.h"
# include "bench.h"

int	sa(t_stack *stack_a, t_bench *bench);
int	sb(t_stack *stack_b, t_bench *bench);
int	ss(t_stack *stack_a, t_stack *stack_b, t_bench *bench);
int	pa(t_stack *stack_a, t_stack *stack_b, t_bench *bench);
int	pb(t_stack *stack_a, t_stack *stack_b, t_bench *bench);
int	ra(t_stack *stack_a, t_bench *bench);
int	rb(t_stack *stack_b, t_bench *bench);
int	rr(t_stack *stack_a, t_stack *stack_b, t_bench *bench);
int	rra(t_stack *stack_a, t_bench *bench);
int	rrb(t_stack *stack_b, t_bench *bench);
int	rrr(t_stack *stack_a, t_stack *stack_b, t_bench *bench);

#endif
