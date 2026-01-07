/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 19:38:10 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/05 16:34:54 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "parser.h"
#include "stack.h"
#include "utils.h"

static int	set_strategy(t_args *args, t_strategy value)
{
	if (args->strategy > 0)
		return (-1);
	args->strategy = value;
	return (1);
}

static int	handle_strategy(char *arg, t_args *args)
{
	if (ft_strcmp(arg, "--simple") == 0)
		return (set_strategy(args, SIMPLE));
	if (ft_strcmp(arg, "--medium") == 0)
		return (set_strategy(args, MEDIUM));
	if (ft_strcmp(arg, "--complex") == 0)
		return (set_strategy(args, COMPLEX));
	if (ft_strcmp(arg, "--adaptive") == 0)
		return (set_strategy(args, ADAPTIVE));
	return (0);
}

int	is_option(char *arg, t_args *args)
{
	int	ret;

	if (ft_strcmp(arg, "--bench") == 0)
	{
		if (args->bench != 0)
			return (-1);
		return (args->bench = 1, 1);
	}
	ret = handle_strategy(arg, args);
	if (ret != 0)
		return (ret);
	return (0);
}

int	parse_args(int argc, char **argv, t_args *arguments)
{
	int	i;
	int	value;

	i = 0;
	while (++i < argc)
	{
		if (is_option(argv[i], arguments) < 0)
			return (-1);
		else if (is_option(argv[i], arguments) == 0)
			break ;
	}
	while (i < argc)
	{
		if (!is_int(argv[i]))
			return (-1);
		value = (int)ft_atoi(argv[i]);
		if (stack_contains(arguments->stack_a, value))
			return (-1);
		push(arguments->stack_a, value);
		i++;
	}
	if (arguments->stack_a->size == 0)
		return (-1);
	return (1);
}

void	init_args(t_args *args)
{
	args->bench = 0;
	args->strategy = DEFAULT;
	args->stack_a = create_stack();
	args->stack_b = create_stack();
}
