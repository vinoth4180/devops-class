# l=dict()
# for a in range(1,11):
#     l[a]=a*a
# print(l)
# print({a:a*a for a in range(1,11)})

# o=[]
# for a in range(1,11):
#     if a%2==0:
#         if a%3==0:
#             o.append(a)
# print(o)
# print([a for a in range(1,11) if a%2==0 if a%3==0])

# a=[]
# for i in range(1,11):
#     if i%2==0:
#         a.append('even')
#     else:
#         a.append('odd')
# print(a)
# print()
# print(['even' if i%2==0 else 'odd' for i in range(1,11)])

#item price in dollars
# old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
#
# dollar_to_pound = 0.76
# new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
# print(new_price)
# new=dict()
# for(item,value) in old_price.items():
#     new[item]=value*dollar_to_pound
# print(new)
# print('-------------------')
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
#
# even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
# print(even_dict)
# even=dict()
# for (k,v) in original_dict.items():
#     if v%2==0:
#         even[k]=v
# print(even)
# print('--------------')
dictionary = dict()
for k1 in range(11, 16):
    dictionary[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print(dictionary)
a=dict()
b=dict()
for k1 in range(11,16):
    a[k1]={}
    for k2 in range(1,6):
        a[k1][k2]=k1*k2

print(a)
# print('----------')
# original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
#
# new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
# print(new_dict)
# a=dict()
# for(k,v) in original_dict.items():
#     if v%2!=0 and v<40:
#         a[k]=v
# print(a)
# print('---------')
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)
a=dict()
for (k,v) in original_dict.items():
    if v>40:
        a[k]='old'
    else:
        a[k]='young'
print(a)