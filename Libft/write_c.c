/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   write_c.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:42:49 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 11:54:57 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	write_c(va_list *ap)
{
	char	c;
	ssize_t	ret;

	c = (char)va_arg(*ap, int);
	ret = write(1, &c, 1);
	if (ret == -1)
		return (-1);
	return (ret);
}
