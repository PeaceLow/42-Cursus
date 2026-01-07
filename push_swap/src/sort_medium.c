/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_medium.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 02:18:57 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/06 22:52:35 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

static int	get_max_pos(t_stack *stack)
{
	t_node	*curr;
	int		max;
	int		max_pos;
	int		i;

	curr = stack->top;
	max = -1;
	max_pos = 0;
	i = 0;
	while (curr)
	{
		if (curr->value > max)
		{
			max = curr->value;
			max_pos = i;
		}
		curr = curr->next;
		i++;
	}
	return (max_pos);
}

static void	push_back_to_a(t_stack *a, t_stack *b, t_bench *bench)
{
	int	max_pos;

	while (b->size > 0)
	{
		max_pos = get_max_pos(b);
		index_to_top(b, max_pos, STACK_B, bench);
		pa(a, b, bench);
	}
}

int	get_optimal_range(int size)
{
	int	range;

	range = (ft_sqrt(size) * 3) + 5;
	return (range);
}

void	sort_chunk(t_stack *a, t_stack *b, t_bench *bench)
{
	int	i;
	int	range;

	convert_to_ranks(a);
	range = get_optimal_range(a->size);
	i = 0;
	while (a->size > 0)
	{
		if (a->top->value <= i)
		{
			pb(a, b, bench);
			rb(b, bench);
			i++;
		}
		else if (a->top->value <= i + range)
		{
			pb(a, b, bench);
			i++;
		}
		else
			ra(a, bench);
	}
	push_back_to_a(a, b, bench);
}
