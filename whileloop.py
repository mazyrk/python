class Test:
    def main():
        x=20
        while(x<=30):
            print(x,end=" ")
            x+=1
    def main_2():
        i=1
        while i<=10:
            print(i,end=" ")
            if(i==12):
                break
            i+=1   
    def main_3():
        i=0
        while i<=6:
            i+=1
            if i==3:
                continue
            print(i,end=" ")        
# obj=Test.main()
# obj=Test.main_2()
obj=Test.main_3()