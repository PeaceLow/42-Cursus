/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 10:06:33 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/04 16:04:50 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*temp;
	int				i;

	i = 0;
	temp = (unsigned char *) s;
	while (n > 0)
	{
		temp[i] = (unsigned char) c;
		i++;
		n--;
	}
	return (s);
}

// int main(void)
// {
//     char text[5] = "abcd";
//     ft_memset(text, 'x', 4);
//     printf("%s\n", text);
//     return (0);
// }
