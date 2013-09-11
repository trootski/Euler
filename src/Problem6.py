import math

square_sum = 0
for i in range(1, 101):
    print i
    square_sum = square_sum + math.pow(i, 2)

sum_square = 0
for i in range(1, 101):
    sum_square = sum_square + i
sum_square = math.pow(sum_square, 2)

square_diff = sum_square - square_sum

print "The difference is %s" % square_diff
