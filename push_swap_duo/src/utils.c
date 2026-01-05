/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: zakburak <zakburak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 19:42:34 by zakburak          #+#    #+#             */
/*   Updated: 2025/12/19 12:10:55 by zakburak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "utils.h"

long long	ft_atoi(const char *nptr)
{
	int			sign;
	long long	result;
	int			i;

	sign = 1;
	result = 0;
	i = 0;
	while (nptr[i] == ' ' || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	if (nptr[i] == '-' || nptr[i] == '+')
	{
		if (nptr[i] == '-')
			sign = -1;
		i++;
	}
	while (nptr[i] >= '0' && nptr[i] <= '9')
	{
		result = result * 10 + (nptr[i] - '0');
		i++;
	}
	return ((long long)(result * sign));
}

int	is_int(const char *str)
{
	long long	num;
	int			i;

	i = 0;
	while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
		i++;
	if (str[i] == '-' || str[i] == '+')
		i++;
	while (str[i] >= '0' && str[i] <= '9')
		i++;
	if (str[i] != '\0')
		return (0);
	num = ft_atoi(str);
	if (num < -2147483648 || num > 2147483647)
		return (0);
	return (1);
}

int	ft_isdigit(int c)
{
	if (c >= 48 && c <= 57)
	{
		return (c);
	}
	return (0);
}

int	ft_strcmp(const char *s1, const char *s2)
{
	int	i;

	i = 0;
	while (s1[i] && s2[i] && s1[i] == s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}
