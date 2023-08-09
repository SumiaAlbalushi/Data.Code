def insertion_sort_dictionary(arr,stype):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key[stype] > arr[j][stype]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Test case
def main():
    
    students = [

        {"name": "Alice", "age": 20, "gpa": 3.9},

        {"name": "Bob", "age": 22, "gpa": 3.7},

        {"name": "Charlie", "age": 21, "gpa": 4.0},

        {"name": "David", "age": 19, "gpa": 3.5},

        ]
    
    print("orignal students:", students)
    
    for students in students:
        print(students)
        
        print("--------------------")
        insertion_sort_dictionary(students,"name")

        print("sorted dictionary:",students)
    
    

main()