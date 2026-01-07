/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 13:00:15 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 18:13:15 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <stdarg.h>
# include <unistd.h>

int		ft_printf(const char *format, ...);
int		ft_putchar_fd(char c, int fd);
int		ft_putstr_fd(char *s, int fd);
int		ft_putnbr_fd(int n, int fd);
int		ft_putunsigned_fd(unsigned int n, int fd);
int		ft_puthex_fd(unsigned long n, char format, int fd);
int		ft_putptr_fd(unsigned long ptr, int fd);
int		ft_putdouble_fd(double n, int fd);
int		ft_format_checker(char format, va_list args);	

#endif
