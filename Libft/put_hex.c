/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   put_hex.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:50:53 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 16:20:06 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	put_hex(unsigned long n)
{
	char	*base;
	char	buf[16];
	int		i;
	int		len;

	base = "0123456789abcdef";
	i = 0;
	if (n == 0)
		buf[i++] = '0';
	while (n > 0)
	{
		buf[i++] = base[n % 16];
		n /= 16;
	}
	len = i;
	while (i--)
	{
		if (write(1, &buf[i], 1) == -1)
			return (-1);
	}
	return (len);
}
