/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 10:02:56 by avauclai          #+#    #+#             */
/*   Updated: 2025/11/05 09:24:00 by avauclai         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	if (lst && del)
	{
		del(lst->content);
		free(lst);
	}
}

// int main(void)
// {
// 	t_list *node = ft_lstnew("Hello, World!");
// 	if (node)
// 	{
// 		printf("Node content before deletion: %s\n", (char *)node->content
// 		);
// 		ft_lstdelone(node, free);
// 	}
// 	return (0);
// }
