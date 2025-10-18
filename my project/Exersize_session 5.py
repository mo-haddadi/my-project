#          
# data
numbers = []
i = 0
while i <10:
    number = float(input('enter the number:'))
    numbers.append(number)
    i = i + 1
# mean
i = 0
total = 0
while i < 10:
    total = total + numbers[i]
    i = i + 1
mean = total / len(numbers)   
# محاسبه مجموع مجذور اختلافها 
i = 0
sum_diff = 0
while i < 10:
    diff = numbers[i] - mean
    sum_diff = sum_diff + (diff * diff)
    i = i + 1
# محاسبه واریانس
population_variance = sum_diff / len(numbers)
# محاسبه انحراف معیا
SD = population_variance ** 0.5
# محاسبه ماکزیمم و مینیمم
maximum = max(numbers)
minimum = min(numbers)

print('results')
print('numbers:', numbers)
print('mean =', mean)
print('population_variance =', population_variance)
print("standard deviation:" , SD)
print(maximum)
print(minimum)






