FILE = "b.txt"

def getInput():
    file = open(FILE, "r")

    bike_size_line = file.readline()
    bike_sizes = list(map(int, bike_size_line.split()))

    kid_size_line = file.readline()
    kid_sizes = list(map(int, kid_size_line.split()))

    return (bike_sizes, kid_sizes)

def min_diff(bike_sizes, kid_sizes):
    return abs(sum(bike_sizes) - sum(kid_sizes))

def calc_size_diff(pairs): 
    diff_score = 0
    pairs = tuple(pairs)
    for (a, b) in list(pairs):
        diff_score += abs(a - b)
    return diff_score

# Main Alg
def opt_sizes(bike_sizes, kid_sizes):
    bike_sizes.sort()
    kid_sizes.sort()
    pairs = zip(bike_sizes, kid_sizes)
    return pairs    


def main():
    print("hello, world!")
    bike_sizes, kid_sizes = getInput()
    print("Min Diff: ", min_diff(bike_sizes, kid_sizes))

    pairs = tuple(opt_sizes(bike_sizes, kid_sizes))
    print("Pairs: ", pairs)
    print("Alg Diff: ", calc_size_diff(pairs))

main()