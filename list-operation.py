# week_two_assignment: List Operations

def main():
    # 1. Create an empty list
    my_list = []

    # 2. Append elements: 10, 20, 30, 40
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    # 3. Insert 15 at the second position (index 1)
    my_list.insert(1, 15)

    # 4. Extend with [50, 60, 70]
    my_list.extend([50, 60, 70])

    # 5. Remove the last element
    my_list.pop()

    # 6. Sort in ascending order
    my_list.sort()

    # 7. Find and print the index of 30
    index_30 = my_list.index(30)

    # Output results
    print("Final list:", my_list)
    print("Index of value 30:", index_30)

if __name__ == "__main__":
    main()
