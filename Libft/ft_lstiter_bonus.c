/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:40:32 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 09:23:58 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!f)
		return ;
	while (lst)
	{
		f(lst->content);
		lst = lst->next;
	}
}
/*
#include "libft.h"
#include <stdio.h>

static void print_content(void *ptr)
{
    printf("%s\n", (char *)ptr);
}

int main(void)
{
    t_list *list = ft_lstnew("one");
    ft_lstadd_back(&list, ft_lstnew("two"));
    ft_lstiter(list, print_content);
    free(list->next);
    free(list);
    return (0);
}
*/
