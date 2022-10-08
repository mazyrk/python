# class Google:
#     def __init__(x,name, title):  #__init__ is used to assign values to the object
#         x.abc=name
#         x.xyz=title
#     def test(x):
#         print(x.abc+" "+x.xyz)
# obj=Google("Mainak", "Deb") 
# #object value modification-----------
# obj.xyz="python"
# obj.abc="Saheb" 
# print("\nAfter Modification-----")     
# obj.test()













#   I N H E R I T E N C E    I N    P Y T H O N

class Main:
    def __init__(self):
        self.abc=str(input("fname -> "))
        self.xyz=str(input("lname -> "))
        
    def test(self):
        print(self.abc + " "+ self.xyz)

class Main_2(Main):
    pass
class Main_3(Main_2):
    pass

obj=Main_3()
obj.test()
    






