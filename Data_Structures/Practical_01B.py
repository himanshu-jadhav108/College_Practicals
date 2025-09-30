#Binary Search

def binary_search(rno, target):
    left = 0
    right = len(rno) - 1
    while left <= right:
        mid = ( left + right ) // 2
        if rno[mid] == target:
            return True
        elif rno[mid] < target :
            left = mid + 1
        else:
            right = mid - 1
    return False 

n = int(input("Enter the Number of Students attended the training program : "))
rno = []
print("Enter the Student Roll Numbers who attended the the training program : ")
print("-"*27)

for i in range(n):
    r = int(input(f"Roll Number {i+1} : "))
    rno.append(r)
    rno.sort()
print("-"*27)

search_student = int(input("Enter the Roll Number of Student to be searched : "))
print("-"*27)

if binary_search(rno, search_student):
    print(f"Roll Number {search_student} attended the training program.")
else:
    print(f"Roll Number {search_student} did not attend the training program.")

