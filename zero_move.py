def is_zero(v):
    # return is instance(v, int) and v is not False and not v
    # return isinstance(v, int) and not isinstance(v, bool) and not v
    return type(v) in (int, float) and not v

def move_zeros(array):

    for i in reversed(range(len(array))):
        if is_zero(array[i]):
            array.append(array.pop(i))
    return array

print(move_zeros([0, 1, None, 2, False, 1, 0]))


def move_zeros(array):
    # your code here

    for el in array:
        if not isinstance(el, bool):
            if el == 0:
                array.remove(0)
                array.append(0)
    return array


res = move_zeros([0, 1, None, 2, False, 1, 0])
print(res)