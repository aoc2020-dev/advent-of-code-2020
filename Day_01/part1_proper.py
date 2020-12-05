
sum = 2020

def run():
    with open("input", "r") as input:
        numbers = input.read().split("\n")

    seenNumbers = dict()

    for numberStr in numbers:
        number = int(numberStr)
        diff = sum - int(number)
        
        if diff in seenNumbers:
            print(f"Solution: {(diff * number)} ({diff} * {number} = {diff * number} | {diff} + {number} = {sum})")
            return
        else:
            seenNumbers[int(number)] = True
    
    


if __name__ == "__main__":
    run()
