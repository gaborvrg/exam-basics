# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

class Average(object):

    def odd_average(self, numbers_of_list):

        nums_of_odd_numbers = 0
        sum_of_odd_numbers = 0

        for num in range(len(numbers_of_list)):
            if numbers_of_list[num] % 2 == 0:   # even number
                pass
            else:   # odd number
                sum_of_odd_numbers += numbers_of_list[num]
                nums_of_odd_numbers += 1

        return sum_of_odd_numbers / nums_of_odd_numbers
        

average = Average()
print(average.odd_average([1,9,3,5,8]))