/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_format.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 13:01:30 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/14 12:31:13 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putstr_fd(char *s, int fd)
{
	int	count;
	int	ret;

	count = 0;
	if (!s)
		return (ft_putstr_fd("(null)", fd));
	while (*s)
	{
		ret = ft_putchar_fd(*s, fd);
		if (ret == -1)
			return (-1);
		count += ret;
		s++;
	}
	return (count);
}

int	ft_puthex_fd(unsigned long n, char format, int fd)
{
	int	count;
	int	ret;

	count = 0;
	if (n >= 16)
	{
		ret = ft_puthex_fd(n / 16, format, fd);
		if (ret == -1)
			return (-1);
		count += ret;
	}
	if (format == 'X')
		ret = ft_putchar_fd("0123456789ABCDEF"[n % 16], fd);
	else
		ret = ft_putchar_fd("0123456789abcdef"[n % 16], fd);
	if (ret == -1)
		return (-1);
	return (count + ret);
}

int	ft_putptr_fd(unsigned long ptr, int fd)
{
	int	count;
	int	ret;

	count = 0;
	if (!ptr)
		return (ft_putstr_fd("(nil)", fd));
	ret = ft_putstr_fd("0x", fd);
	if (ret == -1)
		return (-1);
	count += ret;
	if (ptr == 0)
	{
		ret = ft_putchar_fd('0', fd);
		if (ret == -1)
			return (-1);
		return (count + ret);
	}
	ret = ft_puthex_fd(ptr, 'x', fd);
	if (ret == -1)
		return (-1);
	return (count + ret);
}

int	ft_format_checker(char format, va_list args, int fd)
{
	int	count;

	count = 0;
	if (format == 'c')
		count = ft_putchar_fd(va_arg(args, int), fd);
	else if (format == 's')
		count = ft_putstr_fd(va_arg(args, char *), fd);
	else if (format == 'd' || format == 'i')
		count = ft_putnbr_fd(va_arg(args, int), fd);
	else if (format == 'u')
		count = ft_putunsigned_fd(va_arg(args, unsigned int), fd);
	else if (format == 'x' || format == 'X')
		count = ft_puthex_fd(va_arg(args, unsigned int), format, fd);
	else if (format == 'p')
		count = ft_putptr_fd(va_arg(args, unsigned long), fd);
	else if (format == 'f')
		count = ft_putdouble_fd(va_arg(args, double), fd);
	else if (format == '%')
		count = ft_putchar_fd('%', fd);
	return (count);
}
