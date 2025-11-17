/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 11:38:55 by avauclai          #+#    #+#             */
/*   Updated: 2025/10/30 12:14:05 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_size(long n)
{
	int	count;

	count = 0;
	if (n <= 0)
		count = 1;
	while (n != 0)
	{
		n /= 10;
		count++;
	}
	return (count);
}

char	*ft_itoa(int num)
{
	char	*dst;
	long	n;
	int		len;

	n = num;
	len = count_size(n);
	dst = malloc(sizeof(char) * (len + 1));
	if (!dst)
		return (NULL);
	dst[len] = '\0';
	if (n < 0)
		n = -n;
	if (n == 0)
		dst[0] = '0';
	while (n > 0)
	{
		dst[--len] = (n % 10) + '0';
		n /= 10;
	}
	if (num < 0)
		dst[0] = '-';
	return (dst);
}

// int main(void)
// {
// 	int i = 0;
// 	char	*test ;
// 	test = ft_itoa(10010101);
// 	while (test[i])
// 	{
// 		if (test[i] == '0')
// 			i++;
// 		else
// 		{
// 			printf("%c", test[i]);
// 			i++;
// 		}
// 	}
// }