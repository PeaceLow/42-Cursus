/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:53:04 by zakburak          #+#    #+#             */
/*   Updated: 2025/11/11 10:06:09 by zakburak         ###   ########.fr       */
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
			ret = ft_format_checker(format[i], args);
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
