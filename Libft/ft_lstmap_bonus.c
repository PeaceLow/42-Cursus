/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:42:18 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 09:24:04 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_list;
	t_list	*new_elem;
	void	*new_content;

	if (!lst || !f)
		return (NULL);
	new_list = NULL;
	while (lst)
	{
		new_content = f(lst->content);
		new_elem = ft_lstnew(new_content);
		if (!new_elem)
		{
			if (del)
				del(new_content);
			ft_lstclear(&new_list, del);
			return (NULL);
		}
		ft_lstadd_back(&new_list, new_elem);
		lst = lst->next;
	}
	return (new_list);
}

// static void *duplicate(void *ptr)
// {
//     return (ft_strdup((char *)ptr));
// }

// static void del_content(void *ptr)
// {
//     free(ptr);
// }

// int main(void)
// {
//     t_list *list = ft_lstnew(ft_strdup("one"));
//     ft_lstadd_back(&list, ft_lstnew(ft_strdup("two")));
//     t_list *mapped = ft_lstmap(list, duplicate, del_content);
//     printf("%s\n", (char *)mapped->content);
//     ft_lstclear(&list, del_content);
//     ft_lstclear(&mapped, del_content);
//     return (0);
// }
