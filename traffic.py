
print(" Welcome to Smart Traffic Light System")

print("Select Time of Day:\n1. Peak \n2. Regular \n3. Night")
time_choice = input("Enter 1, 2, or 3: ")

if time_choice == "1":
    time_of_day = "peak"
elif time_choice == "2":
    time_of_day = "regular"
else:
    time_of_day = "night"

print("\nSelect Traffic Density:\n1. High \n2. Medium \n3. Low")
traffic_choice = input("Enter 1, 2, or 3: ")

if traffic_choice == "1":
    traffic_density = "high"
elif traffic_choice == "2":
    traffic_density = "medium"
else:
    traffic_density = "low"

print("\nEmergency Vehicle Present? \n select 1. for yes 2. for no")
emergency_choice = input("Enter 1 or 2: ")

if emergency_choice == "1":
    emergency = "yes"
else:
    emergency = "no"


print("\nPedestrian Waiting to Cross? \n select 1. for yes 2. for no")
pedestrian_choice = input("Enter 1 or 2: ")

if pedestrian_choice == "1":
    pedestrian = "yes"
else:
    pedestrian = "no"

# Weather
print("\nWeather Condition: \n1. Clear \n2. Rainy \n3. Fog")
weather_choice = input("Enter 1, 2, or 3: ")

if weather_choice == "1":
    weather = "clear"
elif weather_choice == "2":
    weather = "rainy"
else:
    weather = "fog"

if emergency == "yes":
    print("\n Emergency detected")
    print("Signal: GREEN for emergency route")

else:
    if pedestrian == "yes":
        print("\n Pedestrian crossing active")
        print("Vehicles: RED")
        print("Pedestrians: GREEN")

    else:
        if time_of_day == "peak":
            if traffic_density == "high":
                print("\n Peak Hour + High Traffic")
                print("GREEN = 60 sec")
            elif traffic_density == "medium":
                print("\n Peak Hour + Medium Traffic")
                print("GREEN = 45 sec")
            else:
                print("\n Peak Hour + Low Traffic")
                print("GREEN = 30 sec")

        elif time_of_day == "regular":
            if traffic_density == "high":
                print("\n Regular Time + High Traffic")
                print("GREEN = 50 sec")
            elif traffic_density == "medium":
                print("\n Regular Time + Medium Traffic")
                print("GREEN = 35 sec")
            else:
                print("\n Regular Time + Low Traffic")
                print("GREEN = 25 sec")

        else: 
            print("\nNight Time")
            print("GREEN = 20 sec")

        
        if weather == "rainy" or weather == "fog":
            print(" Bad weather detected, extra GREEN time for safety")

print("\n safety come first")
