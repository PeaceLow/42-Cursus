/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/06 18:17:20 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/06 22:51:41 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

int	*stack_to_array(t_stack *stack)
{
	int		*arr;
	t_node	*curr;
	int		i;

	arr = malloc(sizeof(int) * stack->size);
	if (!arr)
		return (NULL);
	curr = stack->top;
	i = 0;
	while (curr)
	{
		arr[i++] = curr->value;
		curr = curr->next;
	}
	return (arr);
}

int	*sort_table(int *arr, int size)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	while (i < size)
	{
		j = i + 1;
		while (j < size)
		{
			if (arr[i] > arr[j])
			{
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
			j++;
		}
		i++;
	}
	return (arr);
}

static int	get_rank(int *arr, int size, int val)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (arr[i] == val)
			return (i);
		i++;
	}
	return (0);
}

void	convert_to_ranks(t_stack *stack)
{
	int		*arr;
	t_node	*curr;

	arr = stack_to_array(stack);
	if (!arr)
		return ;
	arr = sort_table(arr, stack->size);
	curr = stack->top;
	while (curr)
	{
		curr->value = get_rank(arr, stack->size, curr->value);
		curr = curr->next;
	}
	free(arr);
}

int	ft_sqrt(int number)
{
	int	i;

	if (number < 0)
		return (0);
	if (number == 0 || number == 1)
		return (number);
	i = 2;
	while (i * i <= number)
		i++;
	return (i - 1);
}
