/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 16:47:27 by avauclai          #+#    #+#             */
/*   Updated: 2025/10/30 16:54:02 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	if (n == -2147483648)
	{
		write(fd, "-2147483648", 11);
		return ;
	}
	if (n < 0)
	{
		write(fd, "-", 1);
		n = n * -1;
	}
	if (n > 9)
	{
		ft_putnbr_fd(n / 10, fd);
		ft_putnbr_fd(n % 10, fd);
	}
	else
	{
		n = n + '0';
		write(fd, &n, 1);
	}
}

// int	main(void)
// {
// 	int	fd;

// 	ft_putnbr_fd(123456, 1); 
// 	write(1, "\n", 1);

// 	fd = open("test_putnbr.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
// 	if (fd == -1)
// 	{
// 		perror("Erreur ouverture fichier");
// 		return (1);
// 	}

// 	ft_putnbr_fd(123456, fd);

// 	close(fd);
// 	printf("Le fichier 'test_putnbr.txt' a été créé");

// 	return (0);
// }
/*
#include "libft.h"

int main(void)
{
    ft_putnbr_fd(12345, 1);
    ft_putchar_fd('
', 1);
    return (0);
}
*/
