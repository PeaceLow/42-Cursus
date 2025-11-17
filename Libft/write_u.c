/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   write_u.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:48:15 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 12:09:41 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	write_u(va_list *ap)
{
	unsigned int	n;
	unsigned long	nb;
	int				len;
	ssize_t			ret;

	n = va_arg(*ap, unsigned int);
	nb = n;
	len = 0;
	ret = putnbr_u_base10(nb);
	if (ret == -1)
		return (-1);
	len += ret;
	return (len);
}
