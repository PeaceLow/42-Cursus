/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   write_percent.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:50:05 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 12:30:41 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	write_percent(void)
{
	char	c;
	ssize_t	ret;

	c = '%';
	ret = write(1, &c, 1);
	if (ret == -1)
		return (-1);
	return (ret);
}
