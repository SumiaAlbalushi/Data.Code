def is_even(L):
    evenList = []
    for num in L:
        if num%2 == 0:
            evenList.append(num)
        return evenList
numbers = [10, 2, 3, 14, 17, 29, 19, 18,22,26]
evens = is_even(numbers)
print("numbers:" , numbers)
print("even numbers:" , evens)

evenUsingFilter = list(filter(lambda n: n%2==0 , numbers))
print("filtered evens:" , evenUsingFilter)
