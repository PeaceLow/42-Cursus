/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 16:40:39 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/04 16:50:32 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putendl_fd(char *s, int fd)
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
	write(fd, "\n", 1);
}
// int	main(void)
// {
// 	int	fd;

// 	ft_putend1_fd("test sur la sortie terminal\n", 1); 

// 	fd = open("test_putend1.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
// 	if (fd == -1)
// 	{
// 		perror("Erreur ouverture fichier");
// 		return (1);
// 	}

// 	ft_putend1_fd("Hi !", fd);

// 	close(fd);
// 	printf("Le fichier 'test_putend1.txt' a été créé");

// 	return (0);
// }
/*
#include "libft.h"

int main(void)
{
    ft_putendl_fd("Bonjour", 1);
    return (0);
}
*/
