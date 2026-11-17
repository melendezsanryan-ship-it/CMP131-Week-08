def main():
    print("Increasing and Decreasing Patterns")
    print()

    print("Pattern A")
    for i in range(1, 11):  # i = outer loop
        line = ""
        for j in range(i):  # j = inner loop
            line = line + "+"
        print(line)

    print()

    print("Pattern B")
    for i in range(10, 0, -1):  # i = outer loop
        line = ""
        for j in range(i):  # j = inner loop
            line = line + "+"
        print(line)




main()
