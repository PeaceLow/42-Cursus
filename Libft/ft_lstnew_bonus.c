/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 09:26:20 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 09:24:05 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*new_node;

	new_node = (t_list *)malloc(sizeof(t_list));
	if (!new_node)
		return (NULL);
	new_node->content = content;
	new_node->next = NULL;
	return (new_node);
}
// int main(void)
// {
// 	t_list *node = ft_lstnew("Hello, World!");
// 	if (node)
// 	{
// 		printf("Node content: %s\n", (char *)node->content);
// 		printf("Node next: %p\n", (void *)node->next);
// 		free(node);
// 	}
// 	return (0);
// }