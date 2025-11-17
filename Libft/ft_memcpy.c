/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 11:43:32 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/04 16:00:46 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*s1_tmp;
	unsigned char	*src_tmp;
	int				i;

	i = 0;
	if (dest == (void *) 0 && src == (void *) 0)
		return (dest);
	s1_tmp = (unsigned char *) dest;
	src_tmp = (unsigned char *) src;
	while (n > 0)
	{
		s1_tmp[i] = src_tmp[i];
		i++;
		n--;
	}
	return (dest);
}
/*
#include "libft.h"
#include <stdio.h>

int main(void)
{
    char src[] = "abcd";
    char dest[5];
    ft_memcpy(dest, src, 5);
    printf("%s\n", dest);
    return (0);
}
*/
