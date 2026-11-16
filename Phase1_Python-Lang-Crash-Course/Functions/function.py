def square(num):
    return num * num

print(square(4))
print(square(10))


def last_element(l):
    if l:
        return l[-1]
    return None

print(last_element([1,2,4,5,7,9,2]))

def single_letter_count(string, letter):
    return string.lower().count(letter.lower())

print(single_letter_count("Abracadabra", "a"))