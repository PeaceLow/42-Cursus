/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 02:19:21 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/14 11:20:47 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SORT_H
# define SORT_H
# include "bench.h"
# include "instruction.h"
# include "stack.h"

void	sort_selection(t_stack *a, t_stack *b, t_bench *bench);
void	sort_three(t_stack *a, t_bench *bench);
void	convert_to_ranks(t_stack *stack);

int		*sort_table(int *arr, int size);
int		*stack_to_array(t_stack *stack);
int		min_stack_index(t_stack *stack);
void	index_to_top(t_stack *stack, int index, t_stack_id id, t_bench *bench);
void	sort_chunk(t_stack *a, t_stack *b, t_bench *bench);
int		ft_sqrt(int number);
int		get_optimal_range(int size);
void	sort_adaptive(t_stack *a, t_stack *b, t_bench *bench);
void	sort_complex_quick(t_stack *a, t_stack *b, t_bench *bench);
int		get_pivot(t_stack *stack, int len);
void	partition_a(t_stack *a, t_stack *b, int *counts, t_bench *bench);
void	partition_b(t_stack *a, t_stack *b, int *counts, t_bench *bench);
#endif