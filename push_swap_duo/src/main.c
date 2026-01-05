/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 12:13:25 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/20 02:50:43 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "parser.h"
#include "ft_printf.h"
#include "stack.h"
#include "bench.h"
#include "sort.h"

static void	run_strategy(t_args *args, t_bench *bench)
{
	double	disorder;

	if (args->strategy == SIMPLE)
		sort_selection(args->stack_a, args->stack_b, bench);
	else if (args->strategy == ADAPTIVE || args->strategy == DEFAULT)
	{
		if (bench)
			disorder = bench->disorder;
		else
			disorder = get_ratio_disordered(args->stack_a);
		if (disorder < 0.2)
			sort_selection(args->stack_a, args->stack_b, bench);
	}
}

int	main(int argc, char	*argv[])
{
	t_args	args;
	t_bench	bench;
	t_bench	*bench_ptr;

	init_args(&args);
	if (parse_args(argc, argv, &args) == -1)
	{
		ft_printf("Error\n");
		return (1);
	}
	bench_ptr = NULL;
	if (args.bench)
	{
		init_bench(&bench, &args);
		bench_ptr = &bench;
	}
	run_strategy(&args, bench_ptr);
	print_stack(args.stack_a);
	free_stack(args.stack_a);
	free_stack(args.stack_b);
	if (args.bench)
		print_bench(&bench);
	return (0);
}
