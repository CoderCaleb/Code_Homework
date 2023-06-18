def find_divisible_numbers():
    lower_limit = int(input("Enter lower range limit: "))
    upper_limit = int(input("Enter upper range limit: "))
    number_to_divide = int(input("Enter the number to be divided by: "))

    print("Numbers divisible by", number_to_divide, "in the range", lower_limit, "to", upper_limit, "are:")

    for i in range(lower_limit, upper_limit + 1):
        if i % number_to_divide == 0:
            print(i)

find_divisible_numbers()