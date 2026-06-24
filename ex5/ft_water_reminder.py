def ft_water_reminder():
    days_last = int(input("Days since last watering: "))
    if days_last > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
