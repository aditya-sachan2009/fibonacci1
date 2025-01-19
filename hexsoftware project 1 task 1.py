def generate_fibonacci(n):

    fibonacci_seq = [0,1]
    for x in range(2,n):
        next_number = fibonacci_seq[x-1] + fibonacci_seq[x-2]
        fibonacci_seq.append(next_number)
    return fibonacci_seq
while True:
    try:
        #prompt user for input
        number = int(input("enter the number of terms:"))

        #validat the input and promt untill valid
        while number < 1:
            print("invalid input, please enter a positive number greater than 1,")
            number = int(input("enter the number of terms:"))

        while number == 1 :
            print|("1 is too small. please enter a number greater than 1.")
            number = int(input("enter the number of terms:"))

        #generate fibonacci sequence and exit
        outcome = generate_fibonacci (number)
        print(f"fibonacci sequence: {outcome}")
        break 
    except ValueError:
        print("invalid input. please enter a valid integer.")


