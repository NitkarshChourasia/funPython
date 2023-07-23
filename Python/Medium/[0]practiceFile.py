lst = ["Nitkarsh", "Anmol", "Mummy", "Pappa", "Rohit"]


def santa_claus(lst):
    if len(lst) == 1:
        house = lst[0]
        print(house)


    else:
        mid = len(lst) // 2
        first_half = lst[:mid]
        second_half = lst[mid:]
        santa_claus(firstHalf)
        santa_claus(secondHalf)


n = 10


def recursion_sum(current_number, accumulated_sum):
    if current_number == 0:
        return accumulated_sum
    else:
        return recursion_sum(current_number - 1, accumulated_sum + current_number)


# print(recursionSum(n, 0))


def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


# print(list_sum_recursive([1, 2, 3, 4, 5]))


def max_recursive(lst1):
    if len(lst1) == 1:
        return lst1[0]
    else:
        return max(lst1[0], maxRecursive(lst1[1:]))


# print(maxRecursive([1, 2, 3, 4, 99, 5, 6, 7, 8, 9, 10]))


def find_some_patterns():
    num_range = range(0, 100000 + 1)
    lst1 = []
    pattern = "123456789"
    for i in num_range:
        if str(i) in pattern:
            print(i)


find_some_patterns()
