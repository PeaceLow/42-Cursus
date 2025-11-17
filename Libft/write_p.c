/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   write_p.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:45:19 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 09:29:53 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	write_p(va_list *ap)
{
	unsigned long	ptr;
	int				len;
	int				tmp;
	ssize_t			ret;

	ptr = (unsigned long)va_arg(*ap, void *);
	if (!ptr)
	{
		ret = (write(1, "(nil)", 5));
		if (ret == -1)
			return (-1);
		return (5);
	}
	ret = write(1, "0x", 2);
	if (ret == -1)
		return (-1);
	len = 2;
	tmp = put_hex(ptr);
	if (tmp == -1)
		return (-1);
	return (tmp + len);
}
