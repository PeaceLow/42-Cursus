/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 19:38:10 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/12 15:41:16 by avauclai         ###   ########.fr       */
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

int	is_option(char *arg, t_args *args)
{
	if (ft_strcmp(arg, "--bench") == 0)
	{
		if (args->bench != 0)
			return (-1);
		args->bench = 1;
		return (1);
	}
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

int	parse_args(int argc, char **argv, t_args *arguments)
{
	int	i;
	int	opt;

	i = 1;
	opt = 0;
	while (i < argc)
	{
		opt = is_option(argv[i], arguments);
		if (opt <= 0)
			break ;
		i++;
	}
	if (opt < 0)
		return (-1);
	if (i < argc && argc == i + 1)
		return (parse_single_arg(argv[i], arguments));
	return (parse_numbers(i, argc, argv, arguments));
}

void	init_args(t_args *args)
{
	args->bench = 0;
	args->strategy = DEFAULT;
	args->stack_a = create_stack();
	args->stack_b = create_stack();
}
