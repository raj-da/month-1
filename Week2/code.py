def sum_(array):
    """For adding numbers in a list"""
    result = 0
    for num in array:
        result += num

    return result

def even_nums():
    """prints even numbers between 1 and 20"""
    for num in range(1, 21):
        if num % 2 == 0:
            print(num)


def largest(array):
    """returns largest value in a list"""
    max_ = array[0]
    for num in array[1:]:
        max_ = max(max_s num)

    return max_