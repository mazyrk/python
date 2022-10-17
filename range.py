class Test:
#     def main():
#         a=int(input("Enter starting value -> "))
#         b=int(input("Enter ending value -> "))
#         for x in range(a,b+1):
#             print(x,end=" ")
    def list_1():
        list_1=[]
        n=int(input("Enter no of elements in the list -> "))
        for x in range(0,n):
            y=int(input()) 
            list_1.append(y)
        print("The Final List -> ", list_1)
        # list_1.sort(reverse=True)
        print("Descending Order -> ",list_1.sort())
obj=Test
obj.list_1()

    