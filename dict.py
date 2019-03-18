# -*- coding: utf-8 -*-
print '打印dict元素'
d = {'Adam':95,
    'Lisa':85,
    'Bart':59,
    'Paul':75
}
print d


print '打印几种不可变的key'
e = {
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', 'b'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
print e

# -*- coding: utf-8 -*-
d = {
    95:'Adam',
    85:'Lisa',
    59:'Bart'
}