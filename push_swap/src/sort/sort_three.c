/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_three.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 12:50:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/01/12 12:55:01 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

static void	handle_case_one(t_stack *a, t_bench *bench)
{
	sa(a, bench);
	rra(a, bench);
}

static void	handle_case_two(t_stack *a, t_bench *bench)
{
	sa(a, bench);
	ra(a, bench);
}

void	sort_three(t_stack *a, t_bench *bench)
{
	int	top;
	int	mid;
	int	bot;

	if (!a || a->size != 3)
		return ;
	top = a->top->value;
	mid = a->top->next->value;
	bot = a->top->next->next->value;
	if (top > mid && mid < bot && top < bot)
		sa(a, bench);
	else if (top > mid && mid > bot)
		handle_case_one(a, bench);
	else if (top > mid && mid < bot && top > bot)
		ra(a, bench);
	else if (top < mid && mid > bot && top < bot)
		handle_case_two(a, bench);
	else if (top < mid && mid > bot && top > bot)
		rra(a, bench);
}
