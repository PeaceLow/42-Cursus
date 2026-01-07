/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_adaptive.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 02:18:57 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/06 22:57:27 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sort.h"

void	sort_adaptive(t_stack *a, t_stack *b, t_bench *bench)
{
	double	disorder;

	disorder = get_ratio_disordered(a);
	if (disorder < 0.2)
		sort_selection(a, b, bench);
	else
		sort_chunk(a, b, bench);
}
