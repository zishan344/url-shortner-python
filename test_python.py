def feature1(func):
    def wrapper(*args, **kwargs):
        print("Feature1 logic")
        return func(*args, **kwargs)
    return wrapper

def feature2(func):
    def wrapper(*args, **kwargs):
        print("Feature2 logic")
        return func(*args, **kwargs)
    return wrapper

# @feature1
# @feature2
def my_function():
    print("Original function")
# print(my_function())

li = [1, 2, 3, 4, 5]

# print([i for i in li if i % 2 == 0])
# print([i for i in range(0, 11, 2)])
print(li[0:4:1])