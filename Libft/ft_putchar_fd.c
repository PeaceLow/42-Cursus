/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 16:27:50 by avauclai          #+#    #+#             */
/*   Updated: 2025/10/30 16:39:45 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putchar_fd(char c, int fd)
{
	write(fd, &c, 1);
}

// int	main(void)
// {
// 	int	fd;

// 	ft_putchar_fd('A', 1); 
// 	ft_putchar_fd('\n', 1);

// 	fd = open("test_putchar.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
// 	if (fd == -1)
// 	{
// 		perror("Erreur ouverture fichier");
// 		return (1);
// 	}

// 	ft_putchar_fd('H', fd);
// 	ft_putchar_fd('i', fd);
// 	ft_putchar_fd('!', fd);
// 	ft_putchar_fd('\n', fd);

// 	close(fd);
// 	printf("Le fichier 'test_putchar.txt' a été créé");

// 	return (0);
// }
/*
#include "libft.h"

int main(void)
{
    ft_putchar_fd('X', 1);
    ft_putchar_fd('
', 1);
    return (0);
}
*/
