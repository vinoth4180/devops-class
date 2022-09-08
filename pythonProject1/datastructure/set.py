# #set={}
# # print(type(set))
# # s1={'hello'}
# # s2= set('hello')
# # print(s1)
# # print(s2)

# s1={1,2,3,4,5,6}
# s2={4,5,6,7,8,1,2}
# s3={7,8,9,10,11,12}
# s4=s1.union(s2,s3)  #|-symbols
# s5=s1.intersection(s2,s3) #&
# s6=s1.difference(s2,s3)#-
# s7=s1.symmetric_difference(s2)#^
# print(s4)
# print(s5)
# print(s6)
# print(s7)

# s=set()
# s.add(5)
# s.add(4)
# s.add(5)
# s.add(51)
# s.add(4)
# print(s)

# cust_2012={'a','b','c','d'}
# cust_2013={'b','c','a','c'}
# cust_2014={'z','b','c','a'}
# # print(cust_2012)
# # print(cust_2013)
# # print(cust_2014)
# s1=cust_2012.intersection(cust_2013,cust_2014)
# print(s1)
# s2=cust_2012.difference(cust_2014,cust_2013)
# print(s2)
# s3=cust_2012.symmetric_difference(cust_2013).symmetric_difference(cust_2014)
# print(s3)
#
# mySet = {1, 2, 4, 5}
# print("Old Set Items = ", mySet)
# mySet.update([2, 3, 6, 7])
# print("New Set Items = ", mySet)

print(dir(set))
