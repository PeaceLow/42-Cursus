/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 15:21:50 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/04 16:07:34 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t n)
{
	size_t	i;
	size_t	src_len;

	if (n == 0)
	{
		src_len = 0;
		while (src[src_len])
			src_len++;
		return (src_len);
	}
	i = 0;
	while (i + 1 < n && src[i])
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	src_len = i;
	while (src[src_len])
		src_len++;
	return (src_len);
}
/*
#include "libft.h"
#include <stdio.h>

int main(void)
{
    char dst[5];
    size_t len = ft_strlcpy(dst, "Hello", sizeof(dst));
    printf("%s (%zu)\n", dst, len);
    return (0);
}
*/
