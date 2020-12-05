
sum = 2020

def run():
    with open("input", "r") as input:
        numbers = input.read().split("\n")[:-2]
        numbersLen = len(numbers)

        seenNumbers = dict()

        for i in range(numbersLen):
            n1 = int(numbers[i])

            for j in range (numbersLen):
                n2 = int(numbers[j])
                nn = n1 + n2
            
                diff = sum - nn
                
                if diff in seenNumbers:
                    print(f"Solution: {(n1 * n2 * diff)}")
                    print(f"{n1} + {n2} + {diff} = {(n1 + n2 + diff)}")
                    print(f"{n1} * {n2} * {diff} = {(n1 * n2 * diff)}")
                    return
                else:
                    seenNumbers[n1] = True


if __name__ == "__main__":
    run()
