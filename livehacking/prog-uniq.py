def uniq_generator(numbers):
    '''filters the stream of numbers into and equally ordered, but duplicate-free, output stream'''

    have = set()
    for elem in numbers:
        if elem in have:
            continue
        yield elem
        have.add(elem)

def uniq_tricky(numbers):
    '''filters the stream of numbers into and equally ordered, but duplicate-free, output stream'''

    return dict.fromkeys(numbers).keys()

def uniq_naive(numbers):
    '''filters the stream of numbers into and equally ordered, but duplicate-free, output stream'''

    uniq_list = []
    have = set()
    for elem in numbers:
        if elem in have:
            continue
        uniq_list.append(elem)
        have.add(elem)
    return uniq_list

input_stream = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_stream = uniq_generator(input_stream)   # or one of the others

for element in output_stream:
    print(element)
