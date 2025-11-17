/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   write_d.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:45:57 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 09:22:00 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	write_d(va_list *ap)
{
	long	nb;
	int		n;
	int		len;
	int		tmp;
	ssize_t	ret;

	n = va_arg(*ap, int);
	nb = n;
	len = 0;
	if (nb < 0)
	{
		ret = write(1, "-", 1);
		if (ret == -1)
			return (-1);
		len++;
		nb = -nb;
	}
	tmp = putnbr_base10(nb);
	if (tmp == -1)
		return (-1);
	len += tmp;
	return (len);
}
