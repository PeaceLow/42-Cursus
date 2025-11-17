/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 12:45:21 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/04 16:03:13 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	char	*dest_tmp;
	char	*src_tmp;
	size_t	count;

	if (!dest && !src)
		return (0);
	dest_tmp = (char *) dest;
	src_tmp = (char *) src;
	count = 0;
	if (dest_tmp > src_tmp)
		while (n-- > 0)
			dest_tmp[n] = src_tmp[n];
	else
	{
		while (count < n)
		{
			dest_tmp[count] = src_tmp[count];
			count++;
		}
	}
	return (dest);
}
/*
#include "libft.h"
#include <stdio.h>

int main(void)
{
    char text[] = "12345";
    ft_memmove(text + 1, text, 4);
    printf("%s\n", text);
    return (0);
}
*/
