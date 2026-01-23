# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 08:22:06 by avauclai          #+#    #+#              #
#    Updated: 2026/01/23 09:15:40 by avauclai         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if day > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
