#taking valuefrom user
voltage=int(input("enter voltage(V):"))
resistance=int(input("enter resistance(ohm):"))
current=voltage/resistance
if(resistance<=0):
        print("invalid resistance")
else:
        print(current)

if(current>2):
    print("fuse will blow")
   
else:
    print("circuit is safe")
