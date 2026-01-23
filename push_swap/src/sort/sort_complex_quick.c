/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_complex_quick.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 12:05:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/01/14 13:04:04 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

static void	quick_b(t_stack *a, t_stack *b, int len, t_bench *bench);

static void	quick_a(t_stack *a, t_stack *b, int len, t_bench *bench)
{
	int	counts[3];
	int	i;

	if (is_sorted(a, len, 1))
		return ;
	if (len <= 2)
	{
		if (len == 2 && a->top->value > a->top->next->value)
			sa(a, bench);
		return ;
	}
	counts[0] = len;
	partition_a(a, b, counts, bench);
	i = -1;
	while (++i < counts[2] && counts[2] != a->size)
		rra(a, bench);
	quick_a(a, b, counts[2], bench);
	quick_b(a, b, counts[1], bench);
}

static void	quick_b(t_stack *a, t_stack *b, int len, t_bench *bench)
{
	int	counts[3];
	int	i;

	if (is_sorted(b, len, 0))
	{
		while (len--)
			pa(a, b, bench);
		return ;
	}
	if (len <= 2)
	{
		if (len == 2 && b->top->value < b->top->next->value)
			sb(b, bench);
		while (len--)
			pa(a, b, bench);
		return ;
	}
	counts[0] = len;
	partition_b(a, b, counts, bench);
	i = -1;
	while (++i < counts[2] && counts[2] != b->size)
		rrb(b, bench);
	quick_a(a, b, counts[1], bench);
	quick_b(a, b, counts[2], bench);
}

void	sort_complex_quick(t_stack *a, t_stack *b, t_bench *bench)
{
	convert_to_ranks(a);
	quick_a(a, b, a->size, bench);
}
