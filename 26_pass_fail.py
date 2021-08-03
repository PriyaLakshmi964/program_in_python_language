sub1 = int(input("enter your sub1 marks in percentage :"))
sub2 = int(input("enter your sub2 marks in percentage :"))
sub3 = int(input("enter your sub3 marks in percentage :"))

total = (sub1+sub2+sub3)/3

if(total>=40 or (sub1>=33 and sub2>=33 and sub3>=33)):
    print("pass")
else:
    print("fail")





