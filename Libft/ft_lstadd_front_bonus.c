/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 09:35:43 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 09:23:53 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (lst && new)
	{
		new->next = *lst;
		*lst = new;
	}
}

// int main(void)
// {
// 	t_list *list = NULL;
// 	t_list *new_node1 = ft_lstnew("Node 1");
// 	t_list *new_node2 = ft_lstnew("Node 2");
// 	ft_lstadd_front(&list, new_node1);
// 	ft_lstadd_front(&list, new_node2);
// 	t_list *current = list;
// 	while (current)
// 	{
// 		printf("Node content: %s\n", (char *)current->content);
// 		current = current->next;
// 	}
// 	current = list;
// 	t_list *next_node;
// 	while (current)
// 	{
// 		next_node = current->next;
// 		free(current);
// 		current = next_node;
// 	}
// 	return (0);
// }