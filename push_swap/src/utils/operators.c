/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operators.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 16:11:38 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 17:44:24 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "operators.h"

int	swap(t_stack *stack)
{
	int	first;
	int	second;

	if (stack->size < 2)
		return (0);
	first = pop(stack);
	second = pop(stack);
	push(stack, first);
	push(stack, second);
	return (1);
}

int	rotate(t_stack *stack)
{
	int	top_value;

	if (stack->size < 2)
		return (0);
	top_value = pop(stack);
	push_bottom(stack, top_value);
	return (1);
}

int	reverse_rotate(t_stack *stack)
{
	int	bottom_value;

	if (stack->size < 2)
		return (0);
	bottom_value = pop_bottom(stack);
	push(stack, bottom_value);
	return (1);
}

int	push_stack(t_stack *from, t_stack *to)
{
	int	value;

	if (is_empty(from))
		return (0);
	value = pop(from);
	push(to, value);
	return (1);
}
