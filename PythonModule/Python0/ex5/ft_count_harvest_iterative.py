# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 08:22:12 by avauclai          #+#    #+#              #
#    Updated: 2026/01/23 09:16:56 by avauclai         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    for i in range(1, day + 1):
        print("Day", i)
    print("Harvest time!")
