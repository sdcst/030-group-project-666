def calculate_fuel(weight_takeoff, flight_time, average_fuel_consumption_rate):
    total_fuel_consumed = average_fuel_consumption_rate * flight_time
    return total_fuel_consumed

<<<<<<< HEAD:1.py
def main():
    print("A330 Fuel Requirements Calculator")
    print("=======================")
=======
def calc():
    print("空客A330飞机油量计算器")
    print("=====================")
    
    # 输入数据并进行验证
>>>>>>> e4624a99ba93a5a793106f1b9e708ec3a70ecaaa:one.py
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