# 1.环境准备
    输入Python到终端

    终端输出：
    Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

# 2.变量、变量类型、作用域

代码示例：
```
    # 变量类型
    name = "Alice"  # str
    age = 20        # int
    grades = [90, 85, 88]  # list
    info = {"name": "Alice", "age": 20}  # dict

    # 类型转换
    age_str = str(age)
    number = int("123")

    # 作用域
    x = 10  # 全局变量
    def my_function():
        y = 5  # 局部变量
        global x
        x += 1
        print(f"Inside function: x={x}, y={y}")

    my_function()
    print(f"Outside function: x={x}")
```

## 输出：
    Inside function: x=11, y=5
    Outside function: x=11

# 3.运算符及表达式

代码示例：
```
    # 算术运算
    a = 10
    b = 3
    print(a + b)  # 13
    print(a // b)  # 3（整除）
    print(a ** b)  # 1000（幂）

    # 逻辑运算
    x = True
    y = False
    print(x and y)  # False
    print(x or y)   # True

    # 比较运算
    print(a > b)  # True
```

## 输出：
    13
    3
    1000
    False
    True
    True

# 4.语句：条件、循环、异常

代码示例：
```
        # 条件语句
    score = 85
    if score >= 90:
        print("A")
    elif score >= 60:
        print("Pass")
    else:
        print("Fail")
    
    # 循环语句
    for i in range(5):
        if i == 3:
            continue
        print(i)
    
    # 异常处理
    try:
        num = int(input("Enter a number: "))
        print(100 / num)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Invalid input!")
    finally:
        print("Execution completed.")
```

## 输出:
    Pass
    0
    1
    2
    4
    Enter a number: 0
    Cannot divide by zero!
    Execution completed.

    Enter a number: a
    Invalid input!
    Execution completed.

    Enter a number: 4
    25.0
    Execution completed.

# 5.函数：定义、参数、匿名函数、高阶函数

代码示例：
```
    # 函数定义
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    print(greet("Alice"))  # Hello, Alice!
    print(greet("Bob", "Hi"))  # Hi, Bob!
    
    # 可变参数
    def sum_numbers(*args):
        return sum(args)
    print(sum_numbers(1, 2, 3, 4))  # 10
    
    # 匿名函数
    double = lambda x: x * 2
    print(double(5))  # 10
    
    # 高阶函数
    def apply_func(func, value):
        return func(value)
    print(apply_func(lambda x: x ** 2, 4))  # 16
```

## 输出:
    Hello, Alice!
    Hi, Bob!
    10
    10
    16

# 6.包和模块：定义模块、导入模块、使用模块、第三方模块

代码示例：
```
    # 主程序
    import mymodule
    print(mymodule.say_hello())
    
    # 导入第三方模块
    import requests
    response = requests.get("https://api.github.com")
    print(response.status_code)  # 200
    print(response)
    
    mymodule.py
    def say_hello():
    return "Hello from module!"
```

## 输出:
    Hello from module!
    200
    <Response [200]>

# 7.类和对象

代码示例：
```
    # 定义类
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
        def introduce(self):
            return f"I am {self.name}, {self.age} years old."
    
    # 继承
    class GradStudent(Student):
        def __init__(self, name, age, major):
            super().__init__(name, age)
            self.major = major
    
        def introduce(self):
            return f"I am {self.name}, a {self.major} student."
    
    # 使用
    student = Student("Alice", 20)
    grad = GradStudent("Bob", 22, "CS")
    print(student.introduce())  # I am Alice, 20 years old.
    print(grad.introduce())     # I am Bob, a CS student.
```

## 输出：
    I am Alice, 20 years old.
    I am Bob, a CS student.

# 8.装饰器

代码示例:
```
    # 简单装饰器
    def my_decorator(func):
        def wrapper():
            print("Before function")
            func()
            print("After function")
        return wrapper
    
    @my_decorator
    def say_hello():
        print("Hello!")
    
    say_hello()
    
    # 带参数的装饰器
    def repeat(n):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    func(*args, **kwargs)
            return wrapper
        return decorator
    
    @repeat(3)
    def greet(name):
        print(f"Hi, {name}!")
    
    greet("Alice")
```

## 输出：
    Before function
    Hello!
    After function
    Hi, Alice!
    Hi, Alice!
    Hi, Alice!

# 9.文件操作

代码示例：
```
    # 写文件
    with open("example.txt", "w") as f:
        f.write("Hello, Python!\n")
    
    # 读文件
    with open("example.txt", "r") as f:
        content = f.read()
        print(content)
    
    # 处理CSV
    import csv
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Alice", 20])
```

##  输出：
    创建了两个文件：data.csv和example.txt

