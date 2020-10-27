def initialize(top:int)->list:
    first: int = 0
    second: int = 1
    third: int = 1
    ct: int = 3
    fib_seq: list = [first, second]
    while ct <= top:
        temp: int = second + third
        fib_seq.append(temp)
        second = third
        third = temp
        ct+=1
    return fib_seq

def is_fib(check:int,fib:list)->(list,bool):
    if check <= fib[-1]:
        return (fib, check in fib)
    else:
        a:int=fib[-2]
        b:int=fib[-1]
        temp:int = a+b
        fib.append(temp)
        while temp <= check:
            temp = a+b
            fib.append(temp)
            a = b
            b = temp
        return (fib, check in fib)

    


if __name__=='__main__':
    play_again: bool = True
    top: int = 10
    fib = initialize(top)
    print(fib)
    while play_again:
        print("Enter a positive integer to see if it is part of the Fibonacci sequence:\t")
        check: int = int(input())
        fib, result = is_fib(check,fib)
        if result:
            print(f"{check} is a Fibonacci number!")
        else:
            print(f"{check} is not a Fibonacci number.")
        print("Try another number? [Y/N]")
        decision: str = input()
        if decision == 'N' or decision == 'n':
            play_again = False