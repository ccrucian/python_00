def ft_count_harvest_recursive():

    def recursive(days):
        if days == 0:
            pass
        else:
            recursive(days - 1)
            print("Day", days)

    days = int(input("Days until harvest: "))
    recursive(days)
    print("Harvest time!")
