/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   instruction_reverse_rotate.c                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:24:04 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 18:51:39 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "instruction.h"
#include "bench.h"

int	rra(t_stack *stack_a, t_bench *bench)
{
	if (reverse_rotate(stack_a) == 0)
		return (0);
	ft_printf("rra\n");
	if (bench && bench->active)
	{
		bench->rra++;
		bench->total_ops++;
	}
	return (9);
}

int	rrb(t_stack *stack_b, t_bench *bench)
{
	if (reverse_rotate(stack_b) == 0)
		return (0);
	ft_printf("rrb\n");
	if (bench && bench->active)
	{
		bench->rrb++;
		bench->total_ops++;
	}
	return (10);
}

int	rrr(t_stack *stack_a, t_stack *stack_b, t_bench *bench)
{
	if (reverse_rotate(stack_a) == 0 || reverse_rotate(stack_b) == 0)
		return (0);
	ft_printf("rrr\n");
	if (bench && bench->active)
	{
		bench->rrr++;
		bench->total_ops++;
	}
	return (11);
}
