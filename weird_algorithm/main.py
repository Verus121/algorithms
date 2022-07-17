FILE = "f.txt"

def getInputs():
    input_file = open(FILE, "r")

    numbers_line = input_file.readline()
    numbers = list(map(int, numbers_line.split()))

    return numbers

# subsequence start is even, and min size 2.
def weird_alg(numbers, position):
    current_weird = []
    even = True # since we are starting the subsequence at position, it is always set as index 0

    while position + 1 != len(numbers):
        current_weird.append(numbers[position])

        if (even and numbers[position] > numbers[position + 1]) or (not even and numbers[position] < numbers[position + 1]):
            position += 1
            even = not even 
        else:
            break 
    
    position += 1 # on next is end of array or next is not weird.
    return (current_weird, position)

def calc(numbers):
    best_weird = []
    position = 0

    while position != len(numbers):
        next = position + 1
        
        # Treat the last element of the array as an array of size 1. 
        if next == len(numbers):
            current_weird = [numbers[position]]
            if len(current_weird) > len(best_weird):
                best_weird = current_weird
            break 
        
        not_even = numbers[position] < numbers[next] or numbers[position] == numbers[next]
        if not_even:
            print(position, " cant be beginning of seq")
            position += 1

        even = numbers[position] > numbers[next]
        if even: 
            print(position, " can be beginning of seq")
            (current_weird, position) = weird_alg(numbers, position)

            if len(current_weird) > len(best_weird):
                best_weird = current_weird

    return best_weird


def main():
    numbers = getInputs()
    print(calc(numbers))

main() 