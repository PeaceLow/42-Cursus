/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   put_hex_upper.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:51:23 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 12:46:44 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	put_hex_upper(unsigned long n)
{
	char	*base;
	char	buf[16];
	int		i;
	int		len;

	base = "0123456789ABCDEF";
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
