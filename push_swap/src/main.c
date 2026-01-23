/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 12:13:25 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/22 12:32:49 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "bench.h"
#include "ft_printf.h"
#include "parser.h"
#include "sort.h"
#include "stack.h"
#include "utils.h"

static void	run_strategy(t_args *args, t_bench *bench)
{
	if (is_sorted(args->stack_a, args->stack_a->size, 1))
		return ;
	if (args->strategy == SIMPLE)
		sort_selection(args->stack_a, args->stack_b, bench);
	else if (args->strategy == MEDIUM)
		sort_chunk(args->stack_a, args->stack_b, bench);
	else if (args->strategy == COMPLEX)
		sort_complex_quick(args->stack_a, args->stack_b, bench);
	else if (args->strategy == ADAPTIVE || args->strategy == DEFAULT)
		sort_adaptive(args->stack_a, args->stack_b, bench);
}

static void	execute_sort(t_args *args, t_bench *bench)
{
	t_bench	*bench_ptr;

	bench_ptr = NULL;
	if (args->bench)
	{
		init_bench(bench, args);
		bench_ptr = bench;
	}
	run_strategy(args, bench_ptr);
	free_stack(args->stack_a);
	free_stack(args->stack_b);
	if (args->bench)
		print_bench(bench);
}

int	main(int argc, char *argv[])
{
	t_args	*args;
	t_bench	bench;

	if (argc == 1)
		return (0);
	args = malloc(sizeof(t_args));
	if (!args)
		return (1);
	init_args(args);
	if (parse_args(argc, argv, args) == -1)
		error_exit(args);
	execute_sort(args, &bench);
	free(args);
	return (0);
}
