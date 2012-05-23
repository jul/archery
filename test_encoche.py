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
c= Hankyu({'foo': ['bar', 'baz']}) + Hankyu({'foo': ['bar', 'baz']})
a+=1
c["foo"][0]="bo"
print c
print a
a = Hankyu({ 1 :  [2], 3 : { 1 : 3 , 4 : { 5 : 1 }}})
#a = bowyer(Hankyu,{ 1 :  [2], 3 : { 1 : 3 , 4 : { 5 : 1 }}})
print a+{1:[3]}
print a+{1:[3]}
print Daikyu( toto="toto") * 0
# OUT: defaultdict(<type 'int'>, {1: 3, 3: defaultdict(<type 'int'>, {1: 4, 4: defaultdict(<type 'int'>, {5: 2})})})
