/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operators.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/19 17:04:00 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 17:10:26 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef OPERATORS_H
# define OPERATORS_H

# include "stack.h"

int	swap(t_stack *stack);
int	rotate(t_stack *stack);
int	reverse_rotate(t_stack *stack);
int	push_stack(t_stack *from, t_stack *to);
#endif
