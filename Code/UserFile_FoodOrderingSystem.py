#Python program for Food Ordering
import ModuleFile_FoodOrderingSystem as FoodMenu
g=['Paneer Manchurian','Babycorn Manchurian','Gobi Manchurian','Babycorn chilly']
k=['Veg Biriyani','Fried Rice','Gobi Rice','Ghee Rice']
cb=['Mac and cheese Pasta','Veg Maceroni','Penne Alfredo','Red sauce Pasta']
qi=[0,0,0,0]
qk=[0,0,0,0]
qc=[0,0,0,0]
v=0
print('-----------------Food Ordering system-----------------')
print('---------------------Welcome Foody--------------------')
while 1:
    ch=FoodMenu.ServiceMenu()
    if(ch==1):
        v=1
        while 1:
            ch1=FoodMenu.FoodMenu()
            if(ch1==1):
                FoodMenu.StartarsMenu()
                while 1 :
                    ch11=int(input('Enter item number you required = '))
                    if ch11>=1 and ch11<=4:
                        q=int(input('Enter quantity = '))
                        qi[ch11-1]+=q
                    elif(ch11==5):
                        break
                    else:
                        print("Invalid item")
            elif(ch1==2):
                FoodMenu.RiceMenu()
                while 1 :
                    ch11=int(input('Enter item number you required = '))
                    if ch11>=1 and ch11<=4:
                        q=int(input('Enter quantity = '))
                        qk[ch11-1]+=q
                    elif(ch11==5):
                        break
                    else:
                        print("Invalid item")
            elif(ch1==3):
                FoodMenu.PastaMenu()
                while 1 :
                    ch11=int(input('Enter item number you required = '))
                    if ch11>=1 and ch11<=4:
                        q=int(input('Enter quantity = '))
                        qc[ch11-1]+=q
                    elif(ch11==5):
                        break
                    else:
                        print("Invalid item")
            elif(ch1==4):
                break
            else:
                print("Invalid Choice")
    elif(ch==2): 
        if v==0:
            print('First Select the Food Items')
        else:
              print("\n----------------------------Your Bill-----------------------------")
              v1=[150.0,160.0,100.0,170.0]
              v2=[150.0,120.0,150.0,120.0]
              v3=[180.0,150.0,140.0,120.0]
              ci=[0,0,0,0]
              ck=[0,0,0,0]
              cc=[0,0,0,0]
              tcost=0.0
              u=0
              for i in qi:
                  ci[u]+=v1[u]*i            #Grocerry items cost calculating
                  u+=1
              u=0
              for i in qk:
                  ck[u]+=v2[u]*i            #Kitchen items cost calculating
                  u+=1
              u=0
              for i in qc:
                  cc[u]+=v3[u]*i             #Clothes items cost calculating
                  u+=1
              tcost=(ci[0]+ci[1]+ci[2]+ci[3]+ck[0]+ck[1]+ck[2]+ck[3]+cc[0]+cc[1]+cc[2]+cc[3])
              Bill=[]
              a="""------------------------------------------------------------------
{:<20} {:<20} {:<20}
------------------------------------------------------------------\n""".format("Items","Quantity","Cost")
              print(a,end='')
              Bill.append(a)
              u=0
              for i in qi :
                  if i>0.0 :
                      b="{:<20} {:<20} {:<20}\n".format(g[u],qi[u],ci[u])
                      print(b,end='')
                      Bill.append(b)
                  u+=1
              u=0
              for i in qk :
                  if i>0.0 :
                      c="{:<20} {:<20} {:<20}\n".format(k[u],qk[u],ck[u])
                      print(c,end='')
                      Bill.append(c)
                  u+=1
              u=0
              for i in qc :
                  if i>0.0 :
                      d="{:<20} {:<20} {:<20}\n".format(cb[u],qc[u],cc[u])
                      print(d,end='')
                      Bill.append(d)
                  u+=1
              gst=(tcost*5)/100
              e='''------------------------------------------------------------------
                  Total price             {}
                  GST                     {}
------------------------------------------------------------------                  
          Total Cost                      {}
------------------------------------------------------------------'''.format(tcost,gst,(tcost+gst))
              print(e,end='')
              Bill.append(e)
              f=open('Bill.txt','w')
              f.writelines(Bill)
    elif(ch==3):
        print("\nThank You for Ordering :)")
        break
    else:
        print("Invalid Choice...!")
