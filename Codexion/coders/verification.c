/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   verification.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 10:34:07 by avauclai          #+#    #+#             */
/*   Updated: 2026/03/06 13:37:53 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "main.h"

int	ft_strcmp(const char *s1, const char *s2)
{
	while (*s1 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

int	verify_numeric(char *str)
{
	int	i;

	i = 0;
	if (!str || !str[i])
		return (1);
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (1);
		i++;
	}
	return (0);
}

static int	check_values(char **av)
{
	if (ft_strcmp(av[8], "fifo") != 0 && ft_strcmp(av[8], "edf") != 0)
	{
		printf("Error: scheduler must be 'fifo' or 'edf'.\n");
		return (1);
	}
	if (atoi(av[1]) < 1)
	{
		printf("Error: number_of_coders must be at least 1.\n");
		return (1);
	}
	return (0);
}

int	verify_args(int ac, char **av)
{
	int	i;

	if (ac != 9)
	{
		printf("Usage: %s nb_coders time_to_burnout time_to_compile"
			" time_to_debug time_to_refactor nb_compiles_required"
			" dongle_cooldown scheduler\n", av[0]);
		return (1);
	}
	i = 1;
	while (i < 8)
	{
		if (verify_numeric(av[i]))
		{
			printf("Error: '%s' is not a valid positive integer.\n", av[i]);
			return (1);
		}
		i++;
	}
	return (check_values(av));
}
