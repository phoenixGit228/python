#%% 
"""全局变量"""
x = 50

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is ', x)


# %%
"""任意多个实参"""
def sum(*num):
    total = 0
    for i in num:
        total += i
    return total

sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# %%
"""成本计算"""
rent = 3000
utilities = int(input('请输入本月的水电费用'))
food_cost = int(input('请输入本月的食材费用'))
variable_cost = utilities + food_cost 
# 以上均为全局变量
print('本月的变动成本是' + str(variable_cost))

def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))

sum_cost()



# %%
