/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 02:18:57 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/20 02:51:54 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

int	min_stack(t_stack *stack)
{
	t_node	*current;
	int		min;
	int		index;
	int		min_index;

	if (is_empty(stack))
		return (-1);
	current = stack->top;
	min = current->value;
	index = 0;
	min_index = 0;
	while (current)
	{
		if (current->value < min)
		{
			min = current->value;
			min_index = index;
		}
		current = current->next;
		index++;
	}
	return (min_index);
}

void	index_to_top(t_stack *stack, int index, t_stack_id id, t_bench *bench)
{
	int	mid;

	mid = stack->size / 2;
	if (index <= mid)
	{
		while (index-- > 0)
		{
			if (id == STACK_A)
				ra(stack, bench);
			else
				rb(stack, bench);
		}
	}
	else
	{
		index = stack->size - index;
		while (index-- > 0)
		{
			if (id == STACK_A)
				rra(stack, bench);
			else
				rrb(stack, bench);
		}
	}
}

void	sort_selection(t_stack *a, t_stack *b, t_bench *bench)
{
	int	min_index;

	while (a->size > 0)
	{
		min_index = min_stack(a);
		index_to_top(a, min_index, STACK_A, bench);
		pa(a, b, bench);
	}
	while (b->size > 0)
	{
		pa(b, a, bench);
	}
}
