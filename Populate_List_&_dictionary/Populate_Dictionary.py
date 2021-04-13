stu={}

i=int(input("enter no of student"))

for a in range(i):
    name =raw_input("enter the name")
    roll =raw_input("enter the roll_number")
    stu[name]=roll

    print "added"

print stu
