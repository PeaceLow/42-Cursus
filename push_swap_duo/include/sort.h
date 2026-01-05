/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 02:19:21 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/20 02:23:49 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SORT_H
# define SORT_H
# include "bench.h"
# include "instruction.h"
# include "stack.h"

void	sort_selection(t_stack *a, t_stack *b, t_bench *bench);
#endif