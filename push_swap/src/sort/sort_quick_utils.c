/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_quick_utils.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 00:27:46 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/09 16:51:23 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

int	get_pivot(t_stack *stack, int len)
{
	int	*tab;
	int	pivot;

	tab = stack_to_array(stack);
	if (!tab)
		return (stack->top->value);
	sort_table(tab, len);
	pivot = tab[len / 2];
	free(tab);
	return (pivot);
}

void	partition_a(t_stack *a, t_stack *b, int *counts, t_bench *bench)
{
	int	pivot;
	int	len;
	int	i;

	len = counts[0];
	pivot = get_pivot(a, len);
	counts[1] = 0;
	counts[2] = 0;
	i = -1;
	while (++i < len)
	{
		if (a->top->value < pivot)
		{
			counts[1]++;
			pb(a, b, bench);
		}
		else
		{
			counts[2]++;
			ra(a, bench);
		}
	}
}

void	partition_b(t_stack *a, t_stack *b, int *counts, t_bench *bench)
{
	int	pivot;
	int	len;
	int	i;

	len = counts[0];
	pivot = get_pivot(b, len);
	counts[1] = 0;
	counts[2] = 0;
	i = -1;
	while (++i < len)
	{
		if (b->top->value >= pivot)
		{
			counts[1]++;
			pa(a, b, bench);
		}
		else
		{
			counts[2]++;
			rb(b, bench);
		}
	}
}
