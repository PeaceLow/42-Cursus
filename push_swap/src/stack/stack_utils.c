/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 21:18:34 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/14 13:07:08 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

void	free_stack(t_stack *stack)
{
	t_node	*current;
	t_node	*next;

	current = stack->top;
	while (current)
	{
		next = current->next;
		free(current);
		current = next;
	}
	free(stack);
}

void	push_bottom(t_stack *stack, int value)
{
	t_node	*new_node;
	t_node	*current;

	new_node = (t_node *)malloc(sizeof(t_node));
	if (!new_node)
		return ;
	new_node->value = value;
	new_node->next = NULL;
	if (is_empty(stack))
		stack->top = new_node;
	else
	{
		current = stack->top;
		while (current->next)
			current = current->next;
		current->next = new_node;
	}
	stack->size++;
}

int	pop_bottom(t_stack *stack)
{
	t_node	*current;
	t_node	*prev;
	int		value;

	if (is_empty(stack))
		return (0);
	if (stack->size == 1)
		return (pop(stack));
	current = stack->top;
	prev = NULL;
	while (current->next)
	{
		prev = current;
		current = current->next;
	}
	value = current->value;
	free(current);
	prev->next = NULL;
	stack->size--;
	return (value);
}
