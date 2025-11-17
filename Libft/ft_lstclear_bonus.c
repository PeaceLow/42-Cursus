/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:06:30 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 09:23:56 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*current;
	t_list	*next;

	if (!lst || !del)
		return ;
	current = *lst;
	while (current)
	{
		next = current->next;
		ft_lstdelone(current, del);
		current = next;
	}
	*lst = NULL;
}

// static void del_content(void *ptr)
// {
//     free(ptr);
// }

// int main(void)
// {
//     t_list *list = ft_lstnew(ft_strdup("one"));
//     ft_lstadd_back(&list, ft_lstnew(ft_strdup("two")));
//     ft_lstclear(&list, del_content);
//     printf("list = %p\n", (void *)list);
//     return (0);
// }
