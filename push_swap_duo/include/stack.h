/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 20:20:35 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/20 02:52:14 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STACK_H
# define STACK_H
# include "ft_printf.h"
# include <stdlib.h>

typedef struct s_node
{
	int				value;
	struct s_node	*next;
}					t_node;

typedef struct s_stack
{
	t_node			*top;
	int				size;
}					t_stack;

typedef enum e_stack_id
{
	STACK_A,
	STACK_B
}					t_stack_id;

t_stack				*create_stack(void);
void				push(t_stack *stack, int value);
int					is_empty(t_stack *stack);
int					pop(t_stack *stack);
int					peek(t_stack *stack);
int					stack_contains(t_stack *s, int value);
void				free_stack(t_stack *stack);
void				print_stack(t_stack *stack);
void				push_bottom(t_stack *stack, int value);
int					pop_bottom(t_stack *stack);

#endif