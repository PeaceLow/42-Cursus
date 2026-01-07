/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 02:19:21 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/06 22:56:46 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SORT_H
# define SORT_H
# include "bench.h"
# include "instruction.h"
# include "stack.h"

void	sort_selection(t_stack *a, t_stack *b, t_bench *bench);
void	convert_to_ranks(t_stack *stack);

int		*sort_table(int *arr, int size);
int		*stack_to_array(t_stack *stack);
int		get_index_in_array(int *arr, int size, int value);
int		min_stack_index(t_stack *stack);
void	index_to_top(t_stack *stack, int index, t_stack_id id, t_bench *bench);
void	sort_chunk(t_stack *a, t_stack *b, t_bench *bench);
int		ft_sqrt(int number);
int		get_optimal_range(int size);
void	sort_adaptive(t_stack *a, t_stack *b, t_bench *bench);
#endif