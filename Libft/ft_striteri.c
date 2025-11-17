/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 16:20:26 by avauclai          #+#    #+#             */
/*   Updated: 2025/10/30 16:27:03 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char *))
{
	unsigned int	i;

	if (!s || !f)
		return ;
	i = 0;
	while (s[i])
	{
		(*f)(i, &s[i]);
		i++;
	}
}
// void	to_upper_if_even(unsigned int i, char *c)
// {
// 	if (i % 2 == 0 && *c >= 'a' && *c <= 'z')
// 		*c = *c - 32; // transformer en majuscule
// }

// int	main(void)
// {
// 	char	str[] = "bonjour"; // chaîne modifiable

// 	printf("Avant : %s\n", str);
// 	ft_striteri(str, to_upper_if_even);
// 	printf("Après : %s\n", str);

// 	return (0);
// }
/*
#include "libft.h"
#include <stdio.h>

static void to_upper(unsigned int i, char *c)
{
    (void)i;
    if (*c >= 'a' && *c <= 'z')
        *c -= 32;
}

int main(void)
{
    char text[] = "abc";
    ft_striteri(text, to_upper);
    printf("%s\n", text);
    return (0);
}
*/
