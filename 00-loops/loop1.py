def loop1():

    # While loop
    count = 0
    while (count < 3):        
        count += 1
        print(count)

    #w While else loop
    count1 = 0
    while (count1 < 3):
        count1 += 1
        print('chonk')
    else:
        print('not chonk')

     # for in loop
    n = 4
    for i in range(0, n):
        print(i)   

def loop2():
    # Iterating over a list
    print('---LIST ITERATION---')
    l = ['chonk', 'chonky', 'sichonky']
    for i in l:
        print(i)

    # iterating over a tupe (immutable)
    print("\n TUPPLE ITERATION")
    t = ('chonk', 'chonky', 'sichonky')
    for i in t:
        print(i)

    # iteraitng over a string
    print('\n String iteration')
    s = 'sichonky'
    for i in s:
        print(i)
    
    # iterating over dictionary
    print('\n DICTIONARY ITERATION')
    d = dict()
    d['xyz'] = 123
    d['abc'] = 321
    for i in d:
        print('%s %d' % (i, d[i]))

def loop3():
    # ITERATING BY INDEX
    listy = ['si', 'chonky', 'sichonky']
    for i in range(len(listy)):
        print(listy[i])

loop3()