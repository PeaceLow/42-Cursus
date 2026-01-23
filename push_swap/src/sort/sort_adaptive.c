/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_adaptive.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 02:18:57 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/21 10:36:19 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

void	sort_adaptive(t_stack *a, t_stack *b, t_bench *bench)
{
	double	disorder;

	if (a->size == 2)
	{
		if (a->top->value > a->top->next->value)
			sa(a, bench);
		return ;
	}
	if (a->size == 3)
	{
		sort_three(a, bench);
		return ;
	}
	if (a->size <= 5)
	{
		sort_selection(a, b, bench);
		return ;
	}
	disorder = get_ratio_disordered(a);
	if (disorder < 0.2)
		sort_selection(a, b, bench);
	else if (disorder < 0.5)
		sort_chunk(a, b, bench);
	else
		sort_complex_quick(a, b, bench);
}
