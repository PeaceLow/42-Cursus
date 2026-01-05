/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   instruction_rotate.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:24:04 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 18:51:39 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "instruction.h"
#include "bench.h"

int	ra(t_stack *stack_a, t_bench *bench)
{
	if (rotate(stack_a) == 0)
		return (0);
	ft_printf("ra\n");
	if (bench && bench->active)
	{
		bench->ra++;
		bench->total_ops++;
	}
	return (6);
}

int	rb(t_stack *stack_b, t_bench *bench)
{
	if (rotate(stack_b) == 0)
		return (0);
	ft_printf("rb\n");
	if (bench && bench->active)
	{
		bench->rb++;
		bench->total_ops++;
	}
	return (7);
}

int	rr(t_stack *stack_a, t_stack *stack_b, t_bench *bench)
{
	if (rotate(stack_a) == 0 || rotate(stack_b) == 0)
		return (0);
	ft_printf("rr\n");
	if (bench && bench->active)
	{
		bench->rr++;
		bench->total_ops++;
	}
	return (8);
}
