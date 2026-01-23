/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:59:24 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 18:13:12 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar_fd(char c, int fd)
{
	if (write(fd, &c, 1) == -1)
		return (-1);
	return (1);
}

int	ft_putnbr_fd(int n, int fd)
{
	long	nb;
	int		count;
	int		ret;

	nb = n;
	count = 0;
	if (nb < 0)
	{
		if (ft_putchar_fd('-', fd) == -1)
			return (-1);
		nb = -nb;
		count += 1;
	}
	if (nb >= 10)
	{
		ret = ft_putnbr_fd((int)(nb / 10), fd);
		if (ret == -1)
			return (-1);
		count += ret;
	}
	if (ft_putchar_fd((char)(nb % 10 + '0'), fd) == -1)
		return (-1);
	return (count + 1);
}

int	ft_putunsigned_fd(unsigned int n, int fd)
{
	int	count;
	int	ret;

	count = 0;
	if (n >= 10)
	{
		ret = ft_putunsigned_fd(n / 10, fd);
		if (ret == -1)
			return (-1);
		count += ret;
	}
	ret = ft_putchar_fd((char)(n % 10 + '0'), fd);
	if (ret == -1)
		return (-1);
	return (count + ret);
}

int	ft_putdouble_fd(double n, int fd)
{
	long	int_part;
	long	frac_part;
	int		count;

	count = 0;
	if (n < 0)
	{
		count += ft_putchar_fd('-', fd);
		n = -n;
	}
	n += 0.005;
	int_part = (long)n;
	frac_part = (long)((n - int_part) * 100);
	count += ft_putnbr_fd((int)int_part, fd);
	if (frac_part > 0)
	{
		count += ft_putchar_fd('.', fd);
		if (frac_part < 10)
			count += ft_putchar_fd('0', fd);
		count += ft_putnbr_fd((int)frac_part, fd);
	}
	return (count);
}
