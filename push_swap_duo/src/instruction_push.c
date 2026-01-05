/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   instruction_push.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:24:04 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 18:51:39 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "instruction.h"
#include "bench.h"

int	pa(t_stack *stack_b, t_stack *stack_a, t_bench *bench)
{
	if (push_stack(stack_b, stack_a) == 0)
		return (0);
	ft_printf("pa\n");
	if (bench && bench->active)
	{
		bench->pa++;
		bench->total_ops++;
	}
	return (4);
}

int	pb(t_stack *stack_a, t_stack *stack_b, t_bench *bench)
{
	if (push_stack(stack_a, stack_b) == 0)
		return (0);
	ft_printf("pb\n");
	if (bench && bench->active)
	{
		bench->pb++;
		bench->total_ops++;
	}
	return (5);
}
