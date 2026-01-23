# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 08:22:16 by avauclai          #+#    #+#              #
#    Updated: 2026/01/23 08:22:17 by avauclai         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(current_day=1, n=None):
    if n is None:
        n = int(input("Days until harvest: "))
    if current_day > n:
        print("Harvest time!")
        return
    print("Day", current_day)
    ft_count_harvest_recursive(current_day + 1, n)
