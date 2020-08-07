'''
The fibonacci sequence is a series of numbers created by 
adding the previous two numbers to form the next number in 
the series. 0 and 1 are the first numbers in the series.
'''
def fibonacci_sequence(num):
    if num==0:
        fibo=[0]
    else:
        fibo=[0,1]
        for i in range(2,num+1):
            next_fibo=fibo[i-2]+fibo[i-1]
            fibo.append(next_fibo)
    return fibo
try:
    n=int(input("Enter a number:"))
    #to raise an assertion error if the number is less than zero
    assert n>=0
    print(f"The Fibonacci sequence for {n} is {fibonacci_sequence(n)}")
#to catch all errors including the assertion error
except:
    print("Invalid input.")
