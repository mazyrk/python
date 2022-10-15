# test_1={
#     "name":"helloworld",
#     "age":40,
#     "address":"Kolkata",
#     "college":"MIT",
#     "100":35626,
#     "gender":"Male"
# }
# # x=test_1["100"]
# # print(x)
# # y=test_1.get("gender")
# # print(y)
# # z=test_1.keys()
# # z_1=test_1.values()
# # print(z,"\n",z_1)
# # print(test_1)
# print(test_1.items())
# test_1["country"]="india"
# print(test_1)





# import pprint
# class Test:
#     def main():
#         n=int(input("ENTER THE LENGTH OF THE DICTIONARY -> "))
#         d=dict(input("Enter key and value -> ").split() for _ in range(n))
#         p=pprint.PrettyPrinter(width=10)
#         p.pprint(d)
# obj=Test
# obj.main()

        
        
        
#   U S E R   I N P U T   D I C T I O N A R Y 

# class Test:
#     def main():
#         n=int(input("ENTER THE LENGTH OF THE DICTIONARY -> "))
#         d=dict(input("Enter key and value -> ").split() for _ in range(n))
#         for x,y in d.items():
#             print("\n",x,":",y)
# obj=Test
# obj.main()



dict_1={
    "name":"Mainak",
    "age":"33",
    "roll":9999,
    "city":"Kolkata",
    "Subject":"Python",
    "Year":2000,
    # "Year":1900, 
}
print(type(dict_1))
print("\n")
for x,y in dict_1.items():
    print(x,":",y)















































