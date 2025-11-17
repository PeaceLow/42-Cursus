/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 11:35:36 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/04 11:04:24 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	char	*temp;
	int		i;

	i = 0;
	temp = (char *) s;
	while (n > 0)
	{
		temp[i] = '\0';
		i++;
		n--;
	}
}
// int main(void)
// {
//     char test[6] = "hello";
//     ft_bzero(test + 2, 3);
//     for (int i = 0; i < 5; i++)
//         printf("%d ", test[i]);
//     printf("\n");
//     return (0);
// }
