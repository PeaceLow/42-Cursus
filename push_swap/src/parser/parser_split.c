/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser_split.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 14:30:00 by avauclai          #+#    #+#             */
/*   Updated: 2026/01/12 15:41:16 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "parser.h"
#include "utils.h"
#include <stdlib.h>

static int	count_words(char *str)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*str)
	{
		if (*str != ' ' && *str != '\t' && !in_word)
		{
			in_word = 1;
			count++;
		}
		else if ((*str == ' ' || *str == '\t') && in_word)
			in_word = 0;
		str++;
	}
	return (count);
}

static int	word_len(char *str)
{
	int	len;

	len = 0;
	while (str[len] && str[len] != ' ' && str[len] != '\t')
		len++;
	return (len);
}

static char	*extract_word(char *str, int len)
{
	char	*word;
	int		i;

	word = malloc(len + 1);
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

static void	free_split(char **split)
{
	int	i;

	if (!split)
		return ;
	i = 0;
	while (split[i])
	{
		free(split[i]);
		i++;
	}
	free(split);
}

char	**ft_split(char *str)
{
	char	**result;
	int		words;
	int		i;
	int		len;

	words = count_words(str);
	result = malloc(sizeof(char *) * (words + 1));
	if (!result)
		return (NULL);
	i = 0;
	while (*str && i < words)
	{
		while (*str == ' ' || *str == '\t')
			str++;
		len = word_len(str);
		result[i] = extract_word(str, len);
		if (!result[i++])
			return (free_split(result), NULL);
		str += len;
	}
	result[i] = NULL;
	return (result);
}
