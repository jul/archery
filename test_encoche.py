from archery.barrack import bowyer
from archery.bow import Hankyu, Daikyu
bowyer(Hankyu,{ 1 : 2, 3 : { 1 : 3, 4: { 5 : 1 }}})
# OUT:   File "<input>", line 1
# OUT:     encoche(f,{ 1 : 2, 3 : { 1 : 3, 4, { 5 : 1 }}})
# OUT:                                      ^
# OUT: SyntaxError: invalid syntax
bowyer(Hankyu,{ 1 :  2, 3 : { 1 : 3 , 4 : { 5 : 1 }}})
# OUT: defaultdict(<type 'int'>, {1: 2, 3: defaultdict(<type 'int'>, {1: 3, 4: defaultdict(<type 'int'>, {5: 1})})})
a = bowyer(Hankyu,{ 1 :  2, 3 : { 1 : 3 , 4 : { 5 : 1 }}})
print a
print a[3] + Hankyu( { 1 : 3 } ) 
c= Hankyu({'foo': ['bar', 'baz']})
d=c+c
a+=1
c["foo"][0]="bo"
print d
print a
a = bowyer(Hankyu,{ 1 :  [2], 3 : { 1 : 3 , 4 : { 5 : 1 }}})
#a = bowyer(Hankyu,{ 1 :  [2], 3 : { 1 : 3 , 4 : { 5 : 1 }}})
print a+{1:[3]}
a+=bowyer(Hankyu,{1:[3], 3: { ("toto",) :  "tata" }})
print a+a
print Daikyu( toto="toto") * 0
# OUT: defaultdict(<type 'int'>, {1: 3, 3: defaultdict(<type 'int'>, {1: 4, 4: defaultdict(<type 'int'>, {5: 2})})})
