/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 10:14:21 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 16:39:30 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	**split_words(const char *s, char c, char **res);
static int	word_count(const char *str, char c);
static char	*fill_word(const char *str, size_t len);
static void	*ft_free(char **strs, size_t count);

char	**ft_split(const char *s, char c)
{
	char	**res;

	if (!s)
		return (NULL);
	res = ft_calloc((word_count(s, c) + 1), sizeof(char *));
	if (!res)
		return (NULL);
	return (split_words(s, c, res));
}

static char	**split_words(const char *s, char c, char **res)
{
	size_t		idx;
	const char	*start;

	idx = 0;
	while (*s)
	{
		while (*s == c)
			s++;
		if (!*s)
			break ;
		start = s;
		while (*s && *s != c)
			s++;
		res[idx] = fill_word(start, (size_t)(s - start));
		if (!res[idx])
			return (ft_free(res, idx));
		idx++;
	}
	return (res);
}

static void	*ft_free(char **strs, size_t count)
{
	size_t	i;

	i = 0;
	while (i < count)
	{
		free(strs[i]);
		i++;
	}
	free(strs);
	return (NULL);
}

static char	*fill_word(const char *str, size_t len)
{
	char	*word;
	size_t	i;

	word = malloc((len + 1) * sizeof(char));
	if (!word)
		return (NULL);
	i = 0;
	while (i < len)
	{
		word[i] = str[i];
		i++;
	}
	word[i] = '\0';
	return (word);
}

static int	word_count(const char *str, char c)
{
	int	count;
	int	x;

	count = 0;
	x = 0;
	while (*str)
	{
		if (*str != c && x == 0)
		{
			x = 1;
			count++;
		}
		else if (*str == c)
			x = 0;
		str++;
	}
	return (count);
}
// void print_split(char **split)
// {
//     int i = 0;

//     if (!split)
//     {
//         printf("(null)\n");
//         return;
//     }

//     while (split[i])
//     {
//         printf("mot[%d] = \"%s\"\n", i, split[i]);
//         i++;
//     }
// }
// void free_split(char **split)
// {
//     int i = 0;
//     if (!split)
//         return;
//     while (split[i])
//         free(split[i++]);
//     free(split);
// }

// int main(void)
// {
//     char **res;

//     printf("=== Test 1 ===\n");
//     res = ft_split("Salut les amis", ' ');
//     print_split(res);
//     free_split(res);

//     printf("\n=== Test 2 ===\n");
//     res = ft_split("  Bonjout   le monde  ", ' ');
//     print_split(res);
//     free_split(res);

//     printf("\n=== Test 3 ===\n");
//     res = ft_split("abc,def,ghi", ',');
//     print_split(res);
//     free_split(res);

//     printf("\n=== Test 4 ===\n");
//     res = ft_split("", ' ');
//     print_split(res);
//     free_split(res);

//     printf("\n=== Test 5 ===\n");
//     res = ft_split("no-separator-here", ',');
//     print_split(res);
//     free_split(res);

//     return 0;
// }
