/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   write_s.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:44:38 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 09:12:34 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	write_s(va_list *ap)
{
	char	*str;
	int		len;
	ssize_t	ret;

	str = va_arg(*ap, char *);
	if (str == NULL)
		str = "(null)";
	len = ft_strlen(str);
	ret = write(1, str, len);
	if (ret == -1)
		return (-1);
	return ((int)ret);
}
