'''
#3
t_bool, f_bool = True, False
res = t_bool and f_bool + t_bool ** (t_bool - f_bool)
print(not res)
#4
print((lambda *args : print(args[0], args[-1], sep="##"))(1,2,3))
#5
lst = [1,2,3]
lst[1:] = lst[:-2]
print(lst)
#6
int lef, def=25, 33
print(type(lef + def) == int)
#7
lst1 = [1,2,3,4]
lst2 = lst1
lst2[0] = 500
print(lst1[0], lst2[0])
#8
my_tup = (3,) + (4,)
my_tup = my_tup + my_tup
print(len(my_tup))
#9
def input(*args, **kwargs) -> None:
    print(args, kwargs)
input(2,3,a=2,b=3)
#10
val = 20
val++
print(val)
'''
