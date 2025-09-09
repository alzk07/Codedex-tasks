#Source: Python practice task from Codedex

 # Haven't learnt yet how to run loop in descending order,hence this is not an efficient code #

for i in range(100):
    if i != 99:
        num = (99 - i)
        new_num = (99 - (i + 1))
        print(f' {num} bottles of bear on the wall, {num} bottles of bear,Take one down,pass it around, {new_num} bottles of bear on the wall')
