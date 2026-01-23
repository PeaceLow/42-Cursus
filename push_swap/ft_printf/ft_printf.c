/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:53:04 by zakburak          #+#    #+#             */
/*   Updated: 2026/01/14 12:31:10 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		i;
	int		count;
	int		ret;

	va_start(args, format);
	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			ret = ft_format_checker(format[i], args, 1);
		}
		else
			ret = ft_putchar_fd(format[i], 1);
		if (ret == -1)
			return (va_end(args), -1);
		count += ret;
		i++;
	}
	va_end(args);
	return (count);
}

int	ft_dprintf(int fd, const char *format, ...)
{
	va_list	args;
	int		i;
	int		count;
	int		ret;

	va_start(args, format);
	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			ret = ft_format_checker(format[i], args, fd);
		}
		else
			ret = ft_putchar_fd(format[i], fd);
		if (ret == -1)
			return (va_end(args), -1);
		count += ret;
		i++;
	}
	va_end(args);
	return (count);
}
