#%%
class Dog():
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('yuanyuan', 10)
my_dog.name
my_dog.sit()


#%%
class robot():
    def __init__(self, name):
        self.name = name
        # self.master = input('你好，我是%s，请问你的名字是？' %(self.name))
        print('你好，我是%s,见到你真好' %(self.name))
        
    def say_hello(self, name2):
        self.name2 = name2
        print('你好，{}。我是{}。遇到你真好' .format(self.name2,self.name))
    
    def wish(self,wish):
        print('请你说出一个愿望')
        self.wish = wish
        for i in range(3):
            print(self.wish)


wali = robot('瓦力')
wali.say_hello('xiaohong')
wali.wish('我要学会python')   

#%%
"""类的多重继承"""
class Su:
    born_city = 'Jiangsu'
    wearing = 'thick'  # 穿得较厚

    def diet(self):
        print('我们爱吃甜。')

class Yue:
    settle_city = 'Guangdong'
    wearing = 'thin'  # 穿得较薄

    def diet(self):
        print('我们吃得清淡。')

class Yuesu(Yue,Su):
    pass

xiaoming = Yuesu()
print(xiaoming.wearing) # 就近原则，先去左侧的类属性里找
print(xiaoming.born_city)
xiaoming.diet()



# %%
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# %%
