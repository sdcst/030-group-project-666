def calculate_fuel_required(weight, distance, time):
    # 基础油量比例（假设为飞行时间的5%）
    basic_fuel_ratio = 0.05
    
    # 燃油消耗率（假设为500公斤/小时）
    fuel_consumption_rate = 500  # 公斤/小时
    
    # 计算基础油量
    basic_fuel = time * basic_fuel_ratio
    
    # 计算备降油量（假设为30分钟）
    alternate_fuel = 0.5 / 60 * fuel_consumption_rate
    
    # 预留油量（假设为1000公斤）
    reserve_fuel = 1000  # 公斤
    
    # 总油量
    total_fuel = basic_fuel + alternate_fuel + reserve_fuel
    
    return total_fuel

def main():
    print("空客A330飞机油量计算器")
    print("=====================")
    
    # 输入数据并进行验证
    while True:
        try:
            weight = float(input("请输入起飞重量（公斤）："))
            distance = float(input("请输入飞行距离（公里）："))
            time = float(input("请输入预计飞行时间（小时）："))
            break
        except ValueError:
            print("输入无效，请输入数字。")
    
    # 计算油量
    fuel_required = calculate_fuel_required(weight, distance, time)
    print("空客A330所需油量：", fuel_required, "公斤")

if __name__ == "__main__":
    main()