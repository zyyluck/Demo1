# 求N个数字的平均值
N = 10
sum = 0
count = 0
print("please input 10 number:")
while count<N:
    number = float(input())
    sum = sum + number
    count +=1
average = sum/N
print("N = {},sum= {}".format(N,sum))
print("Average = {:.2f}".format(average))
