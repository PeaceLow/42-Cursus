/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_stats.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 21:18:34 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/14 13:03:43 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

int	stack_contains(t_stack *s, int value)
{
	t_node	*cur;

	if (!s)
		return (0);
	cur = s->top;
	while (cur)
	{
		if (cur->value == value)
			return (1);
		cur = cur->next;
	}
	return (0);
}

int	is_empty(t_stack *stack)
{
	return (stack->size == 0);
}

void	print_stack(t_stack *stack)
{
	t_node	*current;

	if (!stack)
	{
		ft_printf("Stack is NULL\n");
		return ;
	}
	current = stack->top;
	ft_printf("Stack (size: %d): ", stack->size);
	while (current)
	{
		ft_printf("[%d]", current->value);
		current = current->next;
		if (current)
			ft_printf(" -> ");
	}
	ft_printf("\n");
}

int	is_sorted(t_stack *stack, int len, int asc)
{
	t_node	*curr;

	curr = stack->top;
	while (--len > 0)
	{
		if (asc)
		{
			if (curr->value > curr->next->value)
				return (0);
		}
		else
		{
			if (curr->value < curr->next->value)
				return (0);
		}
		curr = curr->next;
	}
	return (1);
}
