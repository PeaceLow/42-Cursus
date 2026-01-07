/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 20:48:36 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 19:41:53 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PARSER_H
# define PARSER_H

# include "stack.h"

typedef enum e_strategy
{
	DEFAULT = 0,
	SIMPLE = 1,
	MEDIUM = 2,
	COMPLEX = 3,
	ADAPTIVE = 4
}				t_strategy;

typedef struct s_args
{
	int			bench;
	t_strategy	strategy;
	t_stack		*stack_a;
	t_stack		*stack_b;
}				t_args;

void			init_args(t_args *args);
int				parse_args(int argc, char **argv, t_args *arguments);
#endif