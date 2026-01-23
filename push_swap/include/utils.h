/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 20:48:00 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/14 12:57:03 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef UTILS_H
# define UTILS_H

# include "parser.h"

long long	ft_atoi(const char *nptr);
int			is_int(const char *str);
int			ft_isdigit(int c);
int			ft_strcmp(const char *s1, const char *s2);
void		error_exit(t_args *args);

#endif