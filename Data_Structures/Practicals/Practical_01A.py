#Name: Himanshu H. Jadhav
#Roll No. : SE-27
#Batch : S2
#Linear Search

def roll_call_list(rno , target):
    for i in range(len(rno)):
        if rno[i] == target:
            return True
    return False

n = int(input("Enter the Number of Students attended the training program : "))
rno = []
print("Enter the Student Roll Numbers who attended the the training program : ")
print("-"*27)

for i in range(n):
    r = int(input(f"Roll Number {i+1} : "))
    rno.append(r)

search_student = int(input("Enter the Roll Number of Student to be searched : "))

if roll_call_list(rno, search_student):
    print(f"Roll Number {search_student} attended the training program.")
else:
    print(f"Roll Number {search_student} did not attend the training program.")