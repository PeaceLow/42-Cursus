/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   instruction_swap.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:24:04 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/19 10:48:03 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "instruction.h"
#include "bench.h"

int	sa(t_stack *stack_a, t_bench *bench)
{
	if (swap(stack_a) == 0)
		return (0);
	if (!bench || bench->verbose)
		ft_printf("sa\n");
	if (bench && bench->active)
	{
		bench->sa++;
		bench->total_ops++;
	}
	return (1);
}

int	sb(t_stack *stack_b, t_bench *bench)
{
	if (swap(stack_b) == 0)
		return (0);
	if (!bench || bench->verbose)
		ft_printf("sb\n");
	if (bench && bench->active)
	{
		bench->sb++;
		bench->total_ops++;
	}
	return (2);
}

int	ss(t_stack *stack_a, t_stack *stack_b, t_bench *bench)
{
	int	ret_a;
	int	ret_b;

	ret_a = swap(stack_a);
	ret_b = swap(stack_b);
	if (ret_a == 0 && ret_b == 0)
		return (0);
	if (!bench || bench->verbose)
		ft_printf("ss\n");
	if (bench && bench->active)
	{
		bench->ss++;
		bench->total_ops++;
	}
	return (3);
}
