#Sorting 

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr

n = int(input("Enter number of students: "))
percentages = []

print("Enter first year percentages of students:")
for i in range(n):
    p = float(input(f"Student {i+1}: "))
    percentages.append(p)

sel_sorted = selection_sort(percentages.copy())
print("\nAfter Selection Sort (Ascending):", sel_sorted)
print("Top Five Scores:", sel_sorted[-5:][::-1])

bub_sorted = bubble_sort(percentages.copy())
print("\nAfter Bubble Sort (Ascending):", bub_sorted)
print("Top Five Scores:", bub_sorted[-5:][::-1])  