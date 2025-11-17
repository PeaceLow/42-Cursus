/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 09:49:55 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 16:36:31 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (lst == NULL)
		return (NULL);
	while (lst->next != NULL)
		lst = lst->next;
	return (lst);
}
// int main(void)
// {
// 	t_list *node1 = ft_lstnew("Node 3");
// 	t_list *node2 = ft_lstnew("Node 2");
// 	t_list *node3 = ft_lstnew("Node 1");
// 	node1->next = node2;
// 	node2->next = node3;
// 	t_list *last_node = ft_lstlast(node2);
// 	if (last_node)
// 	{
// 		printf("Last node content: %s\n", (char *)last_node->content);
// 	}
// 	free(node1);
// 	free(node2);
// 	free(node3);
// 	return (0);
// }