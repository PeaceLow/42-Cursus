# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: avauclai <avauclai@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/23 08:55:16 by avauclai          #+#    #+#              #
#    Updated: 2026/01/23 09:30:04 by avauclai         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(name, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(name, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(name, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")
