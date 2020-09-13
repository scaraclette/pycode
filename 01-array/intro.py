# PYTHON ARRAYS

def array1():
    food = ['sushi', 'meatball', 'donut']
    print(food[0])

    # length of array
    print('LENGTH OF ARRAY:', len(food))

    # loop through array
    for x in food:
        print(x)

    # add element to array and remove 
    food.append('chonky chicken')
    print(food)

    # popping, deletes last element
    food.pop()
    print(food)

    # remove deletes first found item
    food.remove('meatball')
    print(food)

    # sort array
    food.sort()
    print(food)

array1()