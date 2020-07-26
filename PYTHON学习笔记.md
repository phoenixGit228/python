# PYTHON学习笔记

[TOC]

## 基础知识

### 设置代码格式

- python改进提案（Python Enhancement Proposal）
- [PEP8](https://python.org/dev/peps/pep-0008/)是最古老的PEP之一
- 缩进建议每级4个空格（PEP8）
- 每行代码长度不建议超过80个字符（PEP8）
- 空行是为了组织代码结构，不宜滥用空行

### 变量命名规则

- `数字`、`字母`、`下划线`

- 可以以字母和下划线打头

- 不可以使用空格

- 不要将Python关键字和函数名用作变量名——即不要使用Python保留用于特殊用途的单词

- 应简短又具有描述性

- 慎用小写字母`l`和大写字母`O`，因为它们可能被人错看成数字`1`和`0`



### 内置函数

| 函数    | 描述     |
| :------ | :------- |
| len()   | 类型长度 |
| sort(x) | 类型排序 |
| type()  | 变量类型 |



### 字符串

- 使用单引号`'...'`，`"..."`，`'''...'''`

#### 方法

| 方法                                              | 描述                                                         | 说明                                                         |
| :------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| str.capitalize()                                  | 返回副本，首字母大写，其他小写                               |                                                              |
| str.title()                                       | 其中每个单词第一个字母为大写，其余字母为小写                 |                                                              |
| str.lower()                                       | 全部转为小写                                                 |                                                              |
| str.upper()                                       | 全部转为大写                                                 |                                                              |
| str.swapcase()                                    | 其中大写字符转换为小写，反之亦然                             |                                                              |
| str.casefold()                                    | 返回福门，消除大小写，全部小写                               |                                                              |
| str.center(*width*[, *fillchar*])                 |                                                              |                                                              |
| str.count(*sub*[, *start*[, *end*]])              | 返回字符串，开始到结束（出现的次数）                         |                                                              |
| str.encode(*encoding="utf-8"*, *errors="strict"*) | 返回原字符串编码为字节串对象的版本。 默认编码为 utf-8。      | *errors* 的默认值为 `'strict'`，表示编码错误会引发 [`UnicodeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#UnicodeError)。 其他可用的值为 `'ignore'`, `'replace'`, `'xmlcharrefreplace'`, `'backslashreplace'` 以及任何其他通过 [`codecs.register_error()`](https://docs.python.org/zh-cn/3/library/codecs.html#codecs.register_error) 注册的值 |
| str.endswith(suffix*[, start[, end]]*)            | 如果字符串以指定的 *suffix* 结束返回 `True`，否则返回 `False`。 |                                                              |
| str.startswith(prefix*[, start[, end]]*)          | 如果字符串以指定的 *prefix* 开始则返回 `True`，否则返回 `False` |                                                              |
| str.expandtabs(*tabsize=8*)                       | 返回字符串的副本，其中所有的制表符会由一个或多个空格替换，具体取决于当前列位置和给定的制表符宽度。 | 每 *tabsize* 个字符设为一个制表位（默认值 8 时设定的制表位在列 0, 8, 16 依次类推）。`直接写数字即可` |
| str.find(sub*[, start[, end]]*)                   | 子字符串 *sub* 在 `s[start:end]` 切片内被找到的最小索引。如果找不到，返回-1 | 用于查找sub在字符串中的位置时才用；如果用于查找字符是否在str中时，使用`in` |
| str.rfind(sub[, start[, end]])                    | 子字符串 *sub* 在字符串内被找到的最大（最右）索引            |                                                              |
| str.rindex(sub[, start[, end]])                   | 类似于 [`rfind()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.rfind)，但在子字符串 *sub* 未找到时会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError) |                                                              |
| str.format(*args, **kwargs)                       | 调用此方法的字符串可以包含字符串字面值或者以花括号 `{}` 括起来的替换域 | 格式化字符串                                                 |
| str.lstrip([chars])                               | 移除其中的前导字符。 *chars* 参数为指定要移除字符的字符串。  | 如果省略或为 `None`，则 *chars* 参数默认移除空格符。实际上 *chars* 参数并非指定单个前缀；而是会移除参数值的所有组合 |
| str.strip([chars])                                | 移除其中的前导和末尾字符。 *chars* 参数为指定要移除字符的字符串。 | 如果省略或为 `None`，则 *chars* 参数默认移除空格符。comment_string = '#....... Section 3.2.1 Issue #32 .......!'，comment_string.strip('.#! ')，则会删除`.#! `中的所有字符 |
| str.rstrip([chars])                               | 移除其中的末尾字符。 *chars* 参数为指定要移除字符的字符串。  | 方法同上                                                     |
| str.rsplit(sep=None, *maxsplit=-1*)               | 移除其中的末尾字符。 *chars* 参数为指定要移除字符的字符串。  | 如果给出了 *maxsplit*，则最多进行 *maxsplit* 次拆分，从 *最右边* 开始。 如果 *sep* 未指定或为 `None`，任何空白字符串都会被作为分隔符。 |
| str.split(sep=None, *maxsplit=-1*)                | 返回一个由字符串内单词组成的列表，使用 *sep* 作为分隔字符串。 | 如果给出了 *maxsplit*，则最多进行 *maxsplit* 次拆分          |
| str.splitlines([keepends])                        | 在行边界的位置拆分。 结果列表中不包含行边界                  |                                                              |
| str.replace(old, new[, count])                    | 其中出现的所有子字符串 *old* 都将被替换为 *new*。            | 如果给出了可选参数 *count*，则只替换前 *count* 次出现。      |
| str.ljust(width[, fillchar])                      | 原字符串在其中靠左对齐。 使用指定的 *fillchar* 填充空位      | 如果 *width* 小于等于 `len(s)` 则返回原字符串的副本          |
| str.rjust(width[, fillchar])                      | 原字符串在其中靠右对齐                                       | 方法同上                                                     |
| str.partition(sep)                                | 在 *sep* 首次出现的位置拆分字符串，返回一个 3 元组，         | 其中包含分隔符之前的部分、分隔符本身，以及分隔符之后的部分。如果分隔符未找到，则返回的 3 元组中包含字符本身以及两个空字符串。 |
| str.rpartition(sep)                               | *sep* 最后一次出现的位置拆分字符串，返回一个 3 元组          | 方法同上                                                     |



#### 修改大小写

- 首字母大写`.title()`

	```python
	name = "ada lovelace"
	print(name.title())
	```

	Ada Lovelace

- 全部大写`.upper()`，全部小写`.lower()`

	```python
	name = "Ada Lovelace"
	print(name.upper())
	print(name.lower())
	```

	ADA LOVELACE
	ada lovelace

#### 合并、拼接字符串

- 直接使用`+`连接两个字符串

#### 转义字符

`转义字符补充`

| 转义字符 | 说明   | 备注 |
| -------- | ------ | ---- |
| \t       | 制表符 |      |
| \n       | 换行符 |      |
|          |        |      |

使用字符串时，注意中间字符被转义，可使用字符`\`

#### 删除空白字符

```python
favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
> 'python '
> 'python'
```



> 删除右空白字符`.rstrip()`，删除左空白字符`.lstrip()`，删除前后空白字符`.strip()`

### 数字

#### 整数

运算符 `+，-，*，/，//(整除)，%（求余）,**(乘方)`

#### 浮点数

带小数点

#### 类型转换

- 转为字符型 `str()`

- 转为整型 `int()`

- 转为浮点型 `float()`

	

### 注释

- 单行注释 `# `

- 多行注释 `''' 注释内容   '''`或者 `"""  注释内容 """`

	```python
	'''
	这是两条注释
	这是两条注释
	'''
	```

### 输出

> python 2，可以不用`()`，直接使用`print 变量`, python 3必须使用`()`，格式为`print(输出内容)`

- 输出格式化

  ```python
  # 字符串连接输出
  print("AAA"+"BBB"+str())
  
  # 字符，数字连接，需要注意变量格式
  print("%s, %.2d, %.1f" %(a, b, c))
  
  # 无需注意变量格式，且变量可复用
  print("计算结果为：{0},{1},{0}" .format(a,b))
  ```

- 输出排版

	`内容补充`

	```python
	for i in values:
	    # 默认print最后end="\n",如果改为end = ' ',则是不换行输出
	    print(i, end=" ")
	```
	

### 输入

`input()`

- 所有的输入默认都是`str`
- 如需转为int, float，使用`int(input(...)) `或`float(input(...))`
- 使用单独的一行input()，可以作为提示下一步操作
- 如果使用python2，应使用`raw_iput()`



## 列表list

- 列表`list`使用`[]`，使用`，`进行分隔
- 使用`[x for x in iterable]`创建
- 使用`list( )`创建

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
> ['trek', 'cannondale', 'redline', 'specialized']
# 使用`[x for x in iterable]`创建
list1 = [x for x in range(5)]
list1
> [0, 1, 2, 3, 4]

# 使用list()创建
list1 = list('abc')
list1
> ['a','b','c']
list1 = list((1,2,3))
list1
> [1,2,3]
```

### 索引

像大多数编程语言一样， 从`0`开始，`-1`最后一个

### 列表基本操作

| 操作                   | 结果                                                         | 说明                                                         |
| :--------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| x in s                 | 如果x在s列表中，返回True，否则返回False                      |                                                              |
| x not in s             | 如果x不在s列表中，返回True，否则返回False                    |                                                              |
| s[i]                   | 列表s中的特定元素                                            |                                                              |
| s[i:j]                 | 切片，从i到j，                                               | 如果i大于len(s)，则产生空列表，如果i或j为负，相当于len(s)+i，或者len(s)+j |
| s[i:j:k]               | 切片，从i开始到j，k为步长                                    |                                                              |
| len(s)                 | 列表s长度                                                    |                                                              |
| min(s)                 | 列表s最小值                                                  |                                                              |
| max(s)                 | 列表s最大值                                                  |                                                              |
| s`.index`(x[, i[, j]]) | 列表s中x最先出现的位置，i或j可选，用于确定从i开始之后，到j之前的出现次数 |                                                              |
| s.count(x)             | 列表s中x出现次数                                             |                                                              |

注：

- 两个列表也可进行判断是否相等，条件是元素必须都相同，且元素顺序相同



### 可变列表操作

| 操作                    | 结果                                                         | 说明                                                         |
| :---------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| s[i] = x                | 列表s中i位置元素赋值                                         |                                                              |
| s[i:j] = t              | 列表s中从i到j统一修改为t                                     | t必须是可迭代的，可以是列表、元组、字典                      |
| del s[i:j]              | 列表s中从i到j元素删除                                        |                                                              |
| s[i:j:k] = t            | 列表s从i到j，步长为k的元素替换为t                            | t必须是可迭代的，可以是列表、元组、字典                      |
| del s[i:j:k]            | 列表s从i到j，步长为k的元素删除                               |                                                              |
| s.append(x)             | 列表s添加元素x，该方法最快                                   | 添加的元素保留原有的格式                                     |
| s.extend(t)` or `s += t | 相当于s.append(t)，但与append又有不同。`该方法会消耗更多的内存，可以使用.append(), .extend(), .insert()代替` | `t不能为int或者float`，可以是字符串，列表，元组，字典。只是将t中的元素添加到s中。如果s为字符串列表，使用str.join(s)，可产生一个新的字符串 |
| s.clear()               | 删除列表所有元素，相当于del s[:]                             |                                                              |
| s.copy()                | 拷贝一个列表s，方法等同于s[:]                                |                                                              |
| s *= n                  | 相当于将s重复n次，得到一个新的列表s                          |                                                              |
| s.insert(i, x)          | 在列表s的i位置，插入一个新的元素x                            | 插入元素保留原有的格式，若x为列表、元组、字典，则仍为原类型  |
| s.pop([i])              | 这里的i可选，删除对应的元素，同时取到这个元素。如果为空，删除最后的元素 |                                                              |
| s.remove(x)             | 删除列表s中最先出现的x，如果需要删除所有的x，需要使用for...in...循环 |                                                              |
| s.reverse()             | 反转整个列表                                                 |                                                              |




### 修改元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
> ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles)
> ['ducati', 'yamaha', 'suzuki']
```

### 添加

`.append()`

```python
motorcycles.append('ducati')
print(motorcycles)
> ['honda', 'yamaha', 'suzuki', 'ducati']
```

### 插入

`.instert()`，使用方法insert()可在列表的`任何位置`添加新元素。需要指定新元素的`索引`和`值`。

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
> ['ducati', 'honda', 'yamaha', 'suzuki']
```



### 删除

- `.pop()`

	要将元素从列表中删除，并接着使用它的值。留空，删除最后的值；知道索引位置，可弹出列表任意位置元素。

	```python
	motorcycles = ['honda', 'yamaha', 'suzuki']
	print(motorcycles)
	> ['honda', 'yamaha', 'suzuki']
	
	popped_motorcycle = motorcycles.pop()
	print(motorcycles)
	print(popped_motorcycle)
	> ['honda', 'yamaha']
	> suzuki
	
	# 知道索引位置，可删除列表任意位置元素
	first_owned = motorcycles.pop(0)
	```

- `del()`

	```python
	motorcycles = ['honda', 'yamaha', 'suzuki']
	print(motorcycles)
	> ['honda', 'yamaha', 'suzuki']
	
	del motorcycles[0]
	print(motorcycles)
	> ['yamaha', 'suzuki']
	```

- `.remove()`

	不必知道元素所处的位置，根据值删除元素

	```python
	motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
	motorcycles.remove('ducati')
	```

	> 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。

### 排序

- `.sort()`，修改原列表，默认正序，逆序排列`.sort(reverse = True)`

	```python
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	# 正序排列
	cars.sort()
	print(cars)
	> ['audi', 'bmw', 'subaru', 'toyota']
	
	# 逆序排列
	cars.sort(reverse=True)
	print(cars)
	> ['toyota', 'subaru', 'bmw', 'audi']
	```

- `sorted()`

	返回按特定顺序排列的新列表，同时不影响原列表，默认正序排列，逆序排列可使用`reverse=True`

	```python
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	print(cars)
	> ['bmw', 'audi', 'toyota', 'subaru']
	print(sorted(cars)) # 正序排列
	> ['audi', 'bmw', 'subaru', 'toyota']
	print(cars)
	> ['bmw', 'audi', 'toyota', 'subaru']
	print(sorted(cars, reverse=True)) # 逆序排列
	> ['toyota', 'subaru', 'bmw', 'audi']
	```

### 反转列表顺序

要反转列表元素的排列顺序，可使用方法`.reverse()`，该方法永久性地修改列表元素的排列顺序，恢复到原来的排列顺序，只需对列表再次调用reverse()即可。

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
> ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)
> ['subaru', 'toyota', 'audi', 'bmw']
```

### 列表长度

`len()`

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
```

### 遍历列表

使用`for 临时变量 in 列表:`

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
> alice
david
carolina
```

### 创建数值列表

#### 使用`range()`

```python
# 默认从0开始
for value in range(5):
    print(value,end=" ")
> 0 1 2 3 4

# 不包含最后的尾数
for value in range(1,5):
print(value, end=" ")
> 1 2 3 4
```

#### 使用range()创建数字列表

```python
numbers = list(range(1,6))
print(numbers)
> [1,2,3,4,5]

# 指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)
> [2, 4, 6, 8, 10]

# 列表解析
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
# 请注意，这里的for语句末尾没有冒号
squares = [value**2 for value in range(1,11)]
print(squares)
> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 对数值列表简单统计

统计函数有：`min(), max(), sum()`

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
> 0
max(digits)
> 9
sum(digits)
> 45
```

### 切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。

- 如果指定最后元素的索引，`不包含最后的元素`。输出元素个数为最后的元素减去第一个元素索引值。
- 如果没有指定开始的索引，从列表开始
- 如果没有指定最后的索引，取到列表最后

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 全部列表
print(players[:])
# 前3个元素
print(players[0:3])
# 前2个元素
print(players[:2])
# 从第二个元素去到末尾
print(players[1:])
# 从第二个元素取到倒数第二个
print(players[1:-1])
```

### 复制列表

- 方法1：使用切片方法，`这样原列表元素改动不会影响新的列表`

	```python
	players = ['charles', 'martina', 'michael', 'florence', 'eli']
	teams = players[:]
	players.append('ada')
	print(players)
	> ['charles', 'martina', 'michael', 'florence', 'eli', 'ada']
	
	print(teams)
	> ['charles', 'martina', 'michael', 'florence', 'eli']
	```

- 方法2：使用`.copy()`方法

	```python
	players = ['charles', 'martina', 'michael', 'florence', 'eli']
	teams = players.copy()
	```
	
	
	
- `错误方法`：直接使用列表赋值，`这种方法无法复制列表，只是两个指向同一个列表`

	```python
	players = ['charles', 'martina', 'michael', 'florence', 'eli']
	# teams和players指向同一个列表
	teams = players
	players.append('ada')
	print(players)
	> ['charles', 'martina', 'michael', 'florence', 'eli', 'ada']
	
	print(teams)
	> ['charles', 'martina', 'michael', 'florence', 'eli', 'ada']
	```

	

## 元组

### 要点

- 列表元素、长度是`可以修改`，元组元素、长度`均不能修改`（内部使用列表除外）

- 列表使用`[]`，元组使用`()`

- 元组可理解为一种特殊的列表

- 使用`a,`或者`(a,)`表示只有一个元素

- 可使用`tuple()`创建，`()`的元素`必须是可迭代`的，否则是一个空的元组，没有任何意义

	```python
	# 该元组中只有两个元素，200,50
	dimensions = (200, 50)
	dimensions[0] = 100
	# 不支持元素修改
	> TypeError: 'tuple' object does not support item assignment
	tuple1 = 'a',
	> ('a',)
	tuple1 = tuple('a')
	> ('a',)
	# 使用tuple创建
	tuple1 = tuple('abc') # 字符串
	> ('a','b','c')
	tuple1 = tuple([1,2,3]) # 列表
	> (1,2,3)
	```

### 修改元组变量
- 使用隐性变量并不能修改元组变量

- 将列表放入元组，通过修改列表来修改元组

- 通过显性的重新对整个元组进行定义，可以修改元组

	```python
	num1 = '100'
	num2 = 50
	tuple1 = (num1, num2)
	print(tuple1)
	> ('100', 50)
	
	num1 = 'abc'
	# 元组变量并未改变
	print(tuple1)
	> ('100', 50)
	
	tuple1 = (100,50)
	# 元组变量发生改变
	print(tuple1)
	> (100, 50)
	
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	dimensions = (200, 50,cars)
	print(dimensions)
	> (200, 50, ['bmw', 'audi', 'toyota', 'subaru'])
	cars.append('benz')
	# 元组长度已改变，未改变的是两个数值和一个列表
	print(dimensions)
	> (200, 50, ['bmw', 'audi', 'toyota', 'subaru', 'benz'])
	```

## 集合 set

### 特点

- 无序
- 去重

```python
set1 = {1,2,3,2,3,2,3,4}
print(set1)
> {2,3,1,4}
set1.add(100)
> {2,100,3,1,4}
```

### 方法

| 方法              | 说明                       |
| :---------------- | :------------------------- |
| set.add(元素)     | 添加元素                   |
| set.remove(元素)  | 删除元素，没有该元素将报错 |
| set.discard(元素) | 删除元素，不会报错         |
| set.pop(元素)     | 方法同list                 |



## 字典

特性：

- 同一个键不能出现两次
- 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
- `列表、元组和字典可以相互嵌套`

字典操作如下

| 操作                | 说明                                                         | 说明                                                         |
| :------------------ | :----------------------------------------------------------- | ------------------------------------------------------------ |
| **list(d)**         | 字典 *d* 中使用的所有键的列表                                |                                                              |
| **key in d**        | 如果 *d* 中存在键 *key* 则返回 `True`，否则返回 `False`      |                                                              |
| **key not in d**    |                                                              |                                                              |
| **len(d)**          | 字典 *d* 中的项数                                            |                                                              |
| **d[key]**          | *d* 中以 *key* 为键的值                                      |                                                              |
| **d[key] = value**  | 将 d[key]赋值 *value*                                        |                                                              |
| **del d[key]**      | 删除键值对                                                   | 如果映射中不存在 *key* 则会引发 [`KeyError`](https://docs.python.org/zh-cn/3/library/exceptions.html#KeyError) |
| **del d**           | 删除字典                                                     |                                                              |
| `d.clear()`         | 删除字典所有元素                                             |                                                              |
| `d.copy()`          | 字典的拷贝                                                   |                                                              |
| `d.get(key)`        | 返回字典key对应的值，用法同d[key]                            | 如果没有，返回`KeyError`                                     |
| `d.items()`         | 返回由字典项 (`(键, 值)` 对) 组成的一个新视图                |                                                              |
| `d.keys()`          | 字典key组成的列表                                            |                                                              |
| `d.values()`        | 字典values组成的列表                                         |                                                              |
| `d.pop(key)`        | 返回字典key对应的值，并从字典中删除键、值对                  | 如果没有，返回`KeyError`                                     |
| `d.popitem()`       | 删除字典最后的键值对                                         | 如果字典为空，返回`KeyError`                                 |
| `d.update(d2)`      | 将字典d2中的内容添加到字典d中，返回新的字典d                 |                                                              |
| `cmp`(dict1, dict2) | 如果两个字典的元素相同返回0，如果字典dict1大于字典dict2返回1，如果字典dict1小于字典dict2返回-1 |                                                              |
| d.has_key(key)      | 如果为真，返回True；否则，返回False                          |                                                              |

### 遍历字典

```python
for key, value in dict.items():
    print(key)
    print(value)
```

### 遍历所有键

```python
for key in dict.keys():
    print(key)
    
# 按顺序遍历素有键
for key in sorted(dict.keys()):
    print(key)
```

### 遍历所有值

```python
for value in dict.values():
    print(value)
    

```

-  遍历字典所有值，`为避免重复项，可以使用集合set`，集合类似于列表，但`每个元素必须是独一无二的`

	```python
	for value in set(dict.values()):
	    print(value)
	```

## 条件语句

### 判断条件

是否相等 `==, !=, >=, <=, `

多条件 `and, or`

是否包含  `in, not in`

循环语句中

- `break  `跳出循环
- `continue `调过本次循环
- `pass  `条件占位



### if语句

> else 包罗万象，前面不满足的条件都会执行。为避免错误执行，可以省略else，只执行前面满足的条件

```python
if condition1 and(or) condition2:
    语句
elif condition:
    语句
elif condition:
    语句
else:  # else 包罗万象，前面不满足的条件都会执行。为避免错误执行，可以省略else，只执行前面满足的条件
    语句
```

### while

- 注意循环中修改循环条件，防止进入`死循环`

```python
while condition1 and(or) condition2:
    语句
    break
else:
    语句
```

### 选择

- 循环`次数明确`的，使用`for`循环
- 循环`次数不明确`的，使用`while`循环



## 函数

```python
# 形参可以有，也可以没有
def 函数名(形参):
    """函数说明"""  # docstring，使用三个"括起
    语句
```

### 形参

- 形参 - 函数体内的变量，可以有多个

- 形参默认值 - 函数定义时，形参给的默认值。`调用函数时，如果不对该形参赋值，将使用默认值`。

	> 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
	> 这让Python依然能够正确地解读位置实参。

- `使用任意数量的关键字实参`。形参使用两个`**var_name`，并且放到参数列表最后，函数将创建一个var_name的字典

	```python
	def function_name(**var_name):
	    function_body
	    
	function_name('cat', 'dog', 'tiger', 'elephant')
	```

	



### 实参

- 实参 - 传入函数体的变量，可以有多个

- `关键字实参` - 调用函数时，直接给具体的形参赋值，不用担心调用顺序

- 避免实参错误 —— 注意函数形参个数

- `传递任意数量实参`。可以在函数定义时，使用`*var_name`，var_name将会创建一个元组

    ```python
def function_name(*var_name):
        return var_name
    ```

-  `结合使用位置实参和任意数量实参`

	> 如果要让函数接受不同类型的实参，必须在函数定义中`将接纳任意数量实参的形参放在最后`。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

    ```python
   def make_pizza(size, *toppings):
       """概述要制作的比萨"""
       print("\nMaking a " + str(size) +     
             "-inch pizza with the following toppings:")
       for topping in toppings:
       	print("- " + topping)
make_pizza(16, 'pepperoni')
   make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
   
    ```
> Making a 16-inch pizza with the following toppings:
   - pepperoni
   Making a 12-inch pizza with the following toppings:
   - mushrooms
   - green peppers
   - extra cheese
    ```
  
    ```

    ```
    
    ```
    
    ```

### 返回值

- 可使用`return`语句将值返回到调用函数的代码行

### 传递列表

- `对列表的任何修改都是永久性的`
- 如果不想函数修改原列表，在调用函数时，可以使用实参——列表的切片，传入了列表的副本。如`function_name(list_name[:])`
- 除非必要，建议使用原列表，这样更高效

### 模块

#### 导入模块

```python
import module_name
```

#### 使用as给模块指定别名

```python
import module_name as mn
```

#### 从模块导入特定函数

```python
# 从模块导入函数
from module_name import function_name

# 使用 as 给函数指定别名
from module_name import function_name as fn

# 导入任意数量函数，使用,分割
from module_name import function_0, function_1, function_2

# 导入模块所有函数
from module_name import *
```

> 由于导入了每个函数，`可通过名称来调用每个函数，而无需使用句点表示法`。然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。
>
> `最佳的做法：1）只导入你需要使用的函数；2）导入整个模块并使用句点表示法`。这能让代码更清晰，更容易阅读和理解。

### 函数编写指南

- 给函数指定`描述性名称`，且只在其中使用小写字母和下划线

- 每个函数都应包含`简要地阐述其功能的注释`

- 给`形参`指定默认值时，`等号两边不要有空格`

	```python
	def function_name(parameter_0, parameter_1='default value')
	```

- 对于函数调用中的`关键字实参`，也应遵循这种约定

	```python
	function_name(value_0, parameter_1='value')
	```

- PEP 8（https://www.python.org/dev/peps/pep-0008/）建议代码行的长度不要超过79字符，这样只要编辑器窗口适中，就能看到整行代码。如果形参很多，导致函数定义的长度超过了79字符，可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，从而将形参列表和只缩进一层的函数体区分开来。

	```python
	def function_name(
	        parameter_0, parameter_1, parameter_2,
	        parameter_3, parameter_4, parameter_5):
	    function body...
	```

- 如果程序或模块包含多个函数，可`使用两个空行将相邻的函数分开`，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始。

- `所有的import语句都应放在文件开头`，`唯一例外`的情形是，在`文件开头使用了注释来描述整个程序`。

## 类

```python
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
```

### 要点

- 类名，`首字母大写`
- 后面的`()`为空，说明从空白创建类；python 2.7中需要使用`class Class_Name(object):`
- 类有属性、和方法（函数）
- 每个方法都带有`self`形参
- 带有`self.`的变量可以被类中的其他方法直接使用
- `__init__()`是一种特殊的方法，每当根据类创建新的对象时，python都会自动运行它
- 修改属性值方法
	- 方法1：直接修改属性值
	- 方法2：通过方法修改属性值

### 继承

- 定义子类时，父类必须在同一个文件中，且位于子类前面

- 如果使用类的重构，`()`中填入父类的名字

- 子类的方法`super().__init__()`中`super()`是一个特殊的函数，用于将父类和子类联系起来。`父类也称为超类`，因此super得名

- python 2.7中稍有不同，`super(子类名，self)`两个参数

	```python
	class Car():
	    def __int__(self, make, model, year):
	        self.make = make
	        self.model = model
	        self.year = year
	        
	        
	class ElectricCar(Car):
	    def __init__(self, make, model, year):
	        super().__init__(make, model, year)
	        
	my_tesla = ElectricCar('tesla', 'model s', 2016)
	```

- 可对子类添加区别于父类的属性和方法

- 重写父类方法，可在子类中定义一个方法，与要重写的父类方法同名。这样`python将考虑邻近原则，优先选用子类的方法`

- 将实例用作属性

	```python
	class Car():
		--snip--
	    
	class Battery():  # 将电池创建为新的类
		"""一次模拟电动汽车电瓶的简单尝试"""
		def __init__(self, battery_size=70):
	        """初始化电瓶的属性"""
			self.battery_size = battery_size
	        
	    def describe_battery(self):
			"""打印一条描述电瓶容量的消息"""
			print("This car has a " + str(self.battery_size) + "-kWh battery.")
	        
	class ElectricCar(Car):
		"""电动汽车的独特之处"""
		def __init__(self, make, model, year):
			"""
			初始化父类的属性，再初始化电动汽车特有的属性
			"""
			super().__init__(make, model, year)
			self.battery = Battery()  # 创建了电池属性，同时又属于Battery类
	        
	my_tesla = ElectricCar('tesla', 'model s', 2016)
	my_tesla.battery.describe_battery()
	```

- 从一个模块中导入一个类
- 从一个模块中导入多个类