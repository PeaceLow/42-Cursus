/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/14 10:00:00 by github-copi       #+#    #+#             */
/*   Updated: 2026/01/21 10:51:55 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include "instruction.h"
#include "parser.h"
#include "utils.h"
#include <stdlib.h>
#include <unistd.h>

static void	execute_instruction(char *line, t_args *args, t_bench *bench)
{
	if (!ft_strcmp(line, "sa"))
		sa(args->stack_a, bench);
	else if (!ft_strcmp(line, "sb"))
		sb(args->stack_b, bench);
	else if (!ft_strcmp(line, "ss"))
		ss(args->stack_a, args->stack_b, bench);
	else if (!ft_strcmp(line, "pa"))
		pa(args->stack_a, args->stack_b, bench);
	else if (!ft_strcmp(line, "pb"))
		pb(args->stack_a, args->stack_b, bench);
	else if (!ft_strcmp(line, "ra"))
		ra(args->stack_a, bench);
	else if (!ft_strcmp(line, "rb"))
		rb(args->stack_b, bench);
	else if (!ft_strcmp(line, "rr"))
		rr(args->stack_a, args->stack_b, bench);
	else if (!ft_strcmp(line, "rra"))
		rra(args->stack_a, bench);
	else if (!ft_strcmp(line, "rrb"))
		rrb(args->stack_b, bench);
	else if (!ft_strcmp(line, "rrr"))
		rrr(args->stack_a, args->stack_b, bench);
	else
		error_exit(args);
}

static void	read_and_execute(t_args *args)
{
	char	buffer[5];
	int		i;
	int		ret;
	t_bench	bench;

	bench = (t_bench){0};
	bench.active = 0;
	bench.verbose = 0;
	i = 0;
	ret = read(0, &buffer[i], 1);
	while (ret > 0)
	{
		if (buffer[i] == '\n')
		{
			buffer[i] = '\0';
			execute_instruction(buffer, args, &bench);
			i = -1;
		}
		else if (i >= 3)
			error_exit(args);
		i++;
		ret = read(0, &buffer[i], 1);
	}
}

int	main(int argc, char **argv)
{
	t_args	*args;

	if (argc < 2)
		return (0);
	args = malloc(sizeof(t_args));
	if (!args)
		return (free(args), -1);
	init_args(args);
	if (parse_args(argc, argv, args) < 0)
		error_exit(args);
	read_and_execute(args);
	if (is_sorted(args->stack_a, args->stack_a->size, 1)
		&& args->stack_b->size == 0)
		ft_printf("OK\n");
	else
		ft_printf("KO\n");
	free_args(&args);
	return (0);
}
