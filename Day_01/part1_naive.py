
sum = 2020

def run():
    with open("input", "r") as input:
        numbers = input.read().split("\n")[:-2]
        numbersLen = len(numbers)

    for i in range(numbersLen):
        for j in range(numbersLen):

            n1 = int(numbers[i])
            n2 = int(numbers[j])
            s = n1 + n2 
           
            if s == sum:
                print(f"Solution: {(n1 * n2)} ({n1} * {n2} = {n1 * n2} | {n1} + {n2} = {sum})")
                return 
    


if __name__ == "__main__":
    run()
