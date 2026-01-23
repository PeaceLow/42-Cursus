/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser_utils.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 14:35:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/01/21 10:54:22 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "parser.h"
#include "stack.h"
#include "utils.h"
#include <stdlib.h>

static void	free_split(char **split)
{
	int	i;

	if (!split)
		return ;
	i = 0;
	while (split[i])
	{
		free(split[i]);
		i++;
	}
	free(split);
}

static int	parse_split_numbers(char **numbers, t_args *arguments)
{
	int	i;
	int	value;

	i = 0;
	while (numbers[i])
	{
		if (!is_int(numbers[i]))
			return (-1);
		value = (int)ft_atoi(numbers[i]);
		if (stack_contains(arguments->stack_a, value))
			return (-1);
		push_bottom(arguments->stack_a, value);
		i++;
	}
	return (1);
}

int	parse_single_arg(char *arg, t_args *arguments)
{
	char	**numbers;
	int		result;

	numbers = ft_split(arg);
	if (!numbers)
		return (-1);
	result = parse_split_numbers(numbers, arguments);
	free_split(numbers);
	return (result);
}

int	parse_numbers(int i, int argc, char **argv, t_args *arguments)
{
	int	value;

	while (i < argc)
	{
		if (!is_int(argv[i]))
			return (-1);
		value = (int)ft_atoi(argv[i]);
		if (stack_contains(arguments->stack_a, value))
			return (-1);
		push_bottom(arguments->stack_a, value);
		i++;
	}
	return (1);
}

void	free_args(t_args **args)
{
	if ((*args)->stack_a)
		free_stack((*args)->stack_a);
	if ((*args)->stack_b)
		free_stack((*args)->stack_b);
	free(*args);
	*args = NULL;
}
