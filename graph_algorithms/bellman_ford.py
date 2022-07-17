def main():
    edge_list = [
        # [to, from, weight]
        ["s", "t", 6],
        ["s", "y", 7],
        ["t", "x", 5], 
        ["t", "z", -4], 
        ["t", "y", 8], 
        ["x", "t", -2], 
        ["y", "x", -3], 
        ["y", "z", 9], 
        ["z", "x", 7], 
        ["z", "s", 2], 
    ]

    print(edge_list)


main()