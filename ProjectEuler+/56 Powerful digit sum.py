def digital_sum(n):
    return sum(int(digit) for digit in str(n))

max_value = 0

x = int(input())

for i in range(1,x):
    for j in range(1, x):
        d_sum = digital_sum(i**j)
        max_value = d_sum if d_sum > max_value else max_value

print(max_value)