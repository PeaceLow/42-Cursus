/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 16:34:11 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/04 16:50:27 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putstr_fd(char *s, int fd)
{
	int	i;

	i = 0;
	if (!s)
		return ;
	while (s[i])
	{
		write(fd, &s[i], 1);
		i++;
	}
}

// int	main(void)
// {
// 	int	fd;

// 	ft_putstr_fd("test sur la sortie terminal\n", 1); 

// 	fd = open("test_putstr.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
// 	if (fd == -1)
// 	{
// 		perror("Erreur ouverture fichier");
// 		return (1);
// 	}

// 	ft_putstr_fd("Hi !", fd);

// 	close(fd);
// 	printf("Le fichier 'test_putstr.txt' a été créé");

// 	return (0);
// }
/*
#include "libft.h"

int main(void)
{
    ft_putstr_fd("Hello", 1);
    ft_putchar_fd('
', 1);
    return (0);
}
*/
