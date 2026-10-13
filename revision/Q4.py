from numpy import number


def process(numbers):
    result = [x for x in numbers if x>20]

    double = lambda x : x*2
    result = [double(x) for x in result]

    return result

numbers = [10,25,15,40,35,12,50]
print(process(numbers))
