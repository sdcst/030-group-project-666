def calculate_fuel(weight_takeoff, flight_time, average_fuel_consumption_rate):
    total_fuel_consumed = average_fuel_consumption_rate * flight_time
    return total_fuel_consumed

def calc():
    print("A330 Fuel Requirements Calculator")
    print("=======================")
    while True:
        try:
            weight_takeoff = float(input("Please enter takeoff weight (kg):"))
            flight_time = float(input("Please enter flight time (hours):"))
            average_fuel_consumption_rate = float(input("Please enter average fuel consumption rate (kg/hour):"))
            break
        except ValueError:
            print("wrong number , please ernter again")
    total_fuel_consumed = calculate_fuel(weight_takeoff, flight_time, average_fuel_consumption_rate)
    
    print("The total amount fuel needed:", total_fuel_consumed, "kg")

if __name__ == "__main__":
    calc()