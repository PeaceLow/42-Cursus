/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:52:55 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/14 13:26:31 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "bench.h"

char	*set_complexity_label(t_bench *bench)
{
	if (bench->strategy_used == SIMPLE)
		return ("O(n^2)");
	else if (bench->strategy_used == MEDIUM)
		return ("O(n√n)");
	else if (bench->strategy_used == COMPLEX)
		return ("O(n log n)");
	else if (bench->strategy_used == DEFAULT
		|| bench->strategy_used == ADAPTIVE)
	{
		if (bench->length <= 3)
			return ("O(n)");
		else if (bench->disorder < 0.2)
			return ("O(n^2))");
		else if (bench->disorder < 0.5)
			return ("O(n√n)");
		return ("O(n log n)");
	}
	return ("Unknown");
}

char	*get_strategy_name(t_strategy strategy)
{
	if (strategy == SIMPLE)
		return ("Simple");
	if (strategy == MEDIUM)
		return ("Medium");
	if (strategy == COMPLEX)
		return ("Complex");
	if (strategy == DEFAULT || strategy == ADAPTIVE)
		return ("Adaptive");
	return ("Unknown");
}

void	init_bench(t_bench *bench, t_args *args)
{
	bench->sa = 0;
	bench->sb = 0;
	bench->ss = 0;
	bench->pa = 0;
	bench->pb = 0;
	bench->ra = 0;
	bench->rb = 0;
	bench->rr = 0;
	bench->rra = 0;
	bench->rrb = 0;
	bench->rrr = 0;
	bench->total_ops = 0;
	bench->disorder = get_ratio_disordered(args->stack_a);
	bench->length = args->stack_a->size;
	bench->strategy_used = args->strategy;
	bench->complexity = set_complexity_label(bench);
	bench->active = 1;
	bench->verbose = 1;
}

void	print_bench(t_bench *bench)
{
	if (!bench->active)
		return ;
	ft_dprintf(2, "[bench] disorder: %f%%\n", bench->disorder * 100);
	ft_dprintf(2, "[bench] strategy: %s / %s\n",
		get_strategy_name(bench->strategy_used), bench->complexity);
	ft_dprintf(2, "[bench] total_ops: %d\n", bench->total_ops);
	ft_dprintf(2, "[bench] sa: %d  sb: %d  ss: %d  pa: %d  pb: %d\n", bench->sa,
		bench->sb, bench->ss, bench->pa, bench->pb);
	ft_dprintf(2, "[bench] ra: %d  rb: %d  rr: %d  rra: %d  rrb: %d  rrr: %d\n",
		bench->ra, bench->rb, bench->rr, bench->rra, bench->rrb, bench->rrr);
}

double	get_ratio_disordered(t_stack *stack)
{
	t_node	*current_i;
	t_node	*current_j;
	int		mistakes;
	int		total_count;

	if (!stack || stack->size < 2)
		return (0.0);
	mistakes = 0;
	total_count = 0;
	current_i = stack->top;
	while (current_i)
	{
		current_j = current_i->next;
		while (current_j)
		{
			if (current_i->value > current_j->value)
				mistakes++;
			total_count++;
			current_j = current_j->next;
		}
		current_i = current_i->next;
	}
	return ((double)mistakes / (double)total_count);
}
