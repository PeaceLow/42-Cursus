/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 12:20:09 by avauclai          #+#    #+#             */
/*   Updated: 2025/10/30 16:19:59 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f) (unsigned int, char))
{
	unsigned int	i;
	size_t			len;
	char			*res;

	if (!s || !f)
		return (NULL);
	len = ft_strlen(s);
	res = malloc((len + 1) * sizeof(char));
	if (!res)
		return (NULL);
	i = 0;
	while (i < len)
	{
		res[i] = (*f)(i, s[i]);
		i++;
	}
	res[i] = '\0';
	return (res);
}
// char	to_upper_even(unsigned int i, char c)
// {
// 	if (i % 2 == 0)
// 		return (ft_toupper((unsigned char)c));
// 	return (c);
// }

// int	main(void)
// {
// 	char	*str = "Hello World !";
// 	char	*result;

// 	result = ft_strmapi(str, to_upper_even);
// 	if (!result)
// 		return (1);

// 	printf("Chaîne originale : %s\n", str);
// 	printf("Chaîne transformée : %s\n", result);

// 	free(result);
// 	return (0);
// }
/*
#include "libft.h"
#include <stdio.h>

static char inc_ascii(unsigned int i, char c)
{
    (void)i;
    return (c + 1);
}

int main(void)
{
    char *res = ft_strmapi("abc", inc_ascii);
    if (res)
    {
        printf("%s\n", res);
        free(res);
    }
    return (0);
}
*/
