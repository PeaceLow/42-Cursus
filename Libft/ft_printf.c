/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 12:26:11 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/13 13:20:35 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	putnbr_base10(long nb)
{
	int		count;
	char	digit;
	int		tmp;

	count = 0;
	if (nb >= 10)
	{
		tmp = putnbr_base10(nb / 10);
		if (tmp == -1)
			return (-1);
		count += tmp;
	}
	digit = '0' + (nb % 10);
	if (write(1, &digit, 1) == -1)
		return (-1);
	count++;
	return (count);
}

int	putnbr_u_base10(unsigned long nb)
{
	int		count;
	char	digit;
	int		tmp;

	count = 0;
	if (nb >= 10)
	{
		tmp = putnbr_u_base10(nb / 10);
		if (tmp == -1)
			return (-1);
		count += tmp;
	}
	digit = '0' + (nb % 10);
	if (write(1, &digit, 1) == -1)
		return (-1);
	count++;
	return (count);
}

int	type_args(char c, va_list *ap)
{
	if (c == 'c')
		return (write_c(ap));
	else if (c == 's')
		return (write_s(ap));
	else if (c == 'p')
		return (write_p(ap));
	else if (c == 'd')
		return (write_d(ap));
	else if (c == 'i')
		return (write_d(ap));
	else if (c == 'u')
		return (write_u(ap));
	else if (c == 'x')
		return (write_x(ap));
	else if (c == 'X')
		return (write_upper_x(ap));
	else if (c == '%')
		return (write_percent());
	return (0);
}

int	ft_printf(const char *format, ...)
{
	va_list	list;
	int		total;
	int		ret;

	total = 0;
	ret = 0;
	va_start(list, format);
	while (format && *format)
	{
		if (*format == '%' && *(format + 1))
		{
			ret = type_args(*(format + 1), &list);
			format += 2;
		}
		else
			ret = write(1, format++, 1);
		if (ret == -1)
			break ;
		total += ret;
	}
	va_end(list);
	if (ret == -1)
		return (-1);
	return (total);
}

// int main(void)
// {
// 	ft_printf("=======test 1=======\n");
// 	char	test1 = 'a';
// 	ft_printf("mon prenom commence par %c\n\n", test1);

// 	ft_printf("=======test 2=======\n");
// 	char	test2[] = "axel";
// 	ft_printf("je m'appelle %s\n\n", test2);

// 	ft_printf("=======test 3=======\n");
// 	int		num = 42;
// 	char	*text = "Hello";
// 	void	*null_ptr = NULL;
// 	ft_printf("Adresse d'un int : %p\n", &num);
// 	printf("Avec printf : %p\n", &num);
// 	ft_printf("Adresse d'une chaîne : %p\n", text);
// 	printf("Avec printf : %p\n", text);
// 	ft_printf("Pointeur NULL : %p\n", null_ptr);
// 	printf("Avec printf : %p\n\n", null_ptr);

// 	ft_printf("=======test 4=======\n");
// 	ft_printf("Nombre positif : %d\n", 42);
// 	ft_printf("Nombre negatif : %d\n", -42);
// 	ft_printf("Nombre NULL : %d\n", 0);
// 	ft_printf("INT_MIN : %d\n", INT_MIN);
// 	ft_printf("INT_MAX : %d\n", INT_MAX);
// 	ft_printf("INT_MIN + 1 : %d\n\n", INT_MIN + 1);

// 	ft_printf("=======meme chose avec i=======\n");
// 	ft_printf("Nombre positif : %i\n", 42);
// 	ft_printf("Nombre negatif : %i\n", -42);
// 	ft_printf("Nombre NULL : %i\n", 0);
// 	ft_printf("INT_MIN : %i\n", INT_MIN);
// 	ft_printf("INT_MAX : %i\n", INT_MAX);
// 	ft_printf("INT_MIN + 1 : %i\n\n", INT_MIN + 1);

// 	ft_printf("=======test 5=======\n");
// 	ft_printf("Nombre positif : %u\n", 42);
// 	ft_printf("Nombre negatif : %u\n", -42);
// 	ft_printf("Nombre NULL : %u\n", 0);
// 	ft_printf("INT_MIN : %u\n", INT_MIN);
// 	ft_printf("INT_MAX : %u\n", INT_MAX);
// 	ft_printf("INT_MIN + 1 : %u\n\n", INT_MIN + 1);

// 	ft_printf("=======test 6=======\n");
// 	ft_printf("Hexa en minuscule : %x\n", 42);
// 	ft_printf("Hexa en minuscule : %x\n", UINT_MAX);
// 	ft_printf("Hexa en majuscule : %X\n", 42);
// 	ft_printf("Hexa en majuscule : %X\n", UINT_MAX);

// 	ft_printf("=======test 7=======\n");
// 	ft_printf("j'affiche un %%\n");
//	}
