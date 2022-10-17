test_1={
    "name":"helloworld",
    "age":40,
    "address":"Kolkata",
    "college":"MIT",
    "100":35626,
    "gender":"Male",
    20+3j:"test",
    30.3:False,
}
# x=test_1[30.3]
# print(x)
# y=test_1.get("gender")
# print(y)
# z=test_1.keys()
# z_1=test_1.values()
# print(z,"\n",z_1)
# print(test_1)
# print(test_1.items())
# test_1["country"]="india"
# print(test_1.items())





# import pprint as pt
# class Test:
#     def main():
#         n=int(input("ENTER THE LENGTH OF THE DICTIONARY -> "))
#         d=dict(input("Enter key and value -> ").split() for _ in range(n))
#         p=pt.PrettyPrinter(width=10)
#         p.pprint(d)
# obj=Test
# obj.main()

        
        
        
#   U S E R   I N P U T   D I C T I O N A R Y 

class Test:
    def main():
        n=int(input("ENTER THE LENGTH OF THE DICTIONARY -> "))
        d=dict(input("Enter key and value -> ").split() for _ in range(n))
        for x,y in d.items():
            print("\n",x,":",y)
obj=Test
obj.main()



# dict_1={
#     "name":"Mainak",
#     "age":"33",
#     "roll":9999,
#     "city":"Kolkata",
#     "Subject":"Python",
#     "Year":2000,
#     # "Year":1900, 
# }
# print(type(dict_1))
# print("\n")
# for x,y in dict_1.items():
#     print(x,":",y)







# test_2={
#     "a":50,
#     "b":60,
#     "c":100,
# }
# x=test_2["a"]+test_2["b"]+test_2["c"]
# print(x)





#NUMPY ARRAY MERGING

# import numpy as np
# arr_1=np.array([2,3,6,5])
# arr_2=np.array([20,3,6,64])
# arr=np.concatenate((arr_1,arr_2))
# print(arr)


# import numpy as np
# arr=np.array([1,3,6,16,1,61,56,1,222,5])
# arr_1=np.array(5)
# print(arr.ndim)
# print(arr_1.ndim)
# arr_2=np.array([[1,2,3],[5,6,7]])
# print(arr_2, arr_2.ndim)





# import numpy as np
# arr_1=np.array([2,4,6,8,10,12])
# arr_2=np.array([1,3,5,7,9,11])
# x=arr_1[2]
# y=arr_2[3]
# print("Elements addition -> ",x+y)




# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# # y=arr[3]
# arr_1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# z=arr_1[1,1]
# print(z)



# import numpy as np
# arr=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
# arr_1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# abc=arr[0,1,2]
# xyz=arr[1,1,1]
# print(abc)
# print(xyz)
# print("\n")
# print(arr.ndim,"D"," ",arr.shape)
# print(arr_1.ndim,"D"," ",arr_1.shape)







# x={
#     "a":23,
#     "b":56,
#     "c":100,
#     "car":"BMW",
#     "college":"MSIT",
# }
# print(x)








































