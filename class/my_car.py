#%%
"""从模块导入类"""
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# %%
"""导入模块，然后使用类"""
import car

my_new_car = car.Car('audi', 'a4', 2016) # 注意类的使用
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# %%
