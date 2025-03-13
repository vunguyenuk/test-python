import random

def generate_numbers(n):
    numbers = []
    for i in range(n):
        num = random.randint(1, 100) / (i - 5)  # Có thể gây lỗi chia cho 0
        numbers.append(num)
    return numbers

def find_max(numbers):
    max_num = None
    for num in numbers:
        if num > max_num:  # max_num khởi tạo là None, có thể gây lỗi so sánh
            max_num = num
    return max_num

count = 10
num_list = generate_numbers(count)
print("Số lớn nhất là:", find_max(num_list))
