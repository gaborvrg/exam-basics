# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(numbers_of_list):

    for num in range(len(numbers_of_list)):
         
        if numbers_of_list[num] % 2 == 0:   # even number
            pass
        else:   # odd number
            print(numbers_of_list[num])



odd_average([1,21,3,4,8])