
def ft_count_harvest_recursive(current_day=1, n=None) -> None:
    if n is None:
        n = int(input("Days until harvest: "))
    if current_day > n:
        print("Harvest time!")
        return
    print("Day", current_day)
    ft_count_harvest_recursive(current_day + 1, n)
