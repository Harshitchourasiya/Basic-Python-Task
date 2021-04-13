stu="y"
name=[]
roll_number=[]
count=0
while(stu=="y"):
    name+=[raw_input("enter your name")]
    roll_number+=[raw_input("enter your roll_number")]
    stu=raw_input("want to add more")
    count+=1
print"Data Entered"
print count
if(stu!="y"):
    i=0
    while(i<count):
        print(name[i])
        print(roll_number[i])
        i=i+1

        print"\n"
