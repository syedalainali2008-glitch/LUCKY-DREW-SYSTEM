import random
input1=str(input("ENTER LUCKYDREW MEMBER 1:"))
input2=str(input("ENTER LUCKYDREW MEMBER 2:"))
input3=str(input("ENTER LUCKYDREW MEMBER 3:"))
input4=str(input("ENTER LUCKYDREW MEMBER 4:"))
lucky_drew=[input1,input2,input3,input4]
print("SO THE WINNNER IS:",random.sample(lucky_drew,k=1))
