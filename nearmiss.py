"""
Title : Calculate Fermat's Last Theorem Near Misses
Filename : nearmiss.py
Necessary files : N/A
Created external files : nearmiss.exe, it is an executable for windows platform
Name : Vamshi Kamal Eligeti
Email : VamshiKamalEligeti@lewisu.edu
Course, Sections : Software Engineering- 003
Date : 11/21/2022
Explanation : An interactive user search for near misses using Farmat's Last Theorem formula
    of the form (x, y, z, n, k) in the formula x^n + y^n = z^n, where x, y, z, n, k
    are positive integers, 2< n <12, 10 <= x <= k, and 10 <= y <= k
Resource : N/A
Language used : Python, Version : 3.10
"""

def calculate_miss(n, k):
    # Calculate near misses using the Fermat's Last Theorem formula
    # x^n + y^n = z^n, and then display the minimum miss on the screen
    # to the user
 
    # initialize relative miis variable with value of -1 when there is no miss calculated 
    relative_miss = -1
    # loop for first variable x of function x^n + y^n = z^n
    for x in range(10, k):
        # loop for the second variable y of function x^n + y^n = z^n
        for y in range(10, k):
            # calculate (x^n + y^n) using in pow method
            xysum_pow = pow(x, n) + pow(y, n)
            # get z and z+1 and their power
            z = int(pow(xysum_pow, 1/n))
            z_pow = pow(z, n)
            z1_pow = pow(z+1, n)
            # calculate miss and get the relative miss from the miss
            miss = min( xysum_pow - z_pow, z1_pow - xysum_pow)
            relative_miss2 = miss / xysum_pow

            # dsiplay to the screen for every small relative miss
            if relative_miss == -1 or relative_miss > relative_miss2: 
                # get the minimum relative miss
                relative_miss = relative_miss2
                print(f"[x] : {x}      [y] : {y}      [z] : {z}       [Miss] : {miss}      [Relative Miss] : {round(relative_miss*100,2)}%")
    
    # display the final result
    print("\nFinal Near Miss : \n") 
    print(f"[x] : {x}     [y] : {y}      [z] : {z}       [Miss] : {miss}      [Relative Miss] : {round(relative_miss*100,2)}%")

def near_miss():
    print("# Calculate near misses with formula x^n + y^n = z^n #\n")
    n = int(input("\nEnter Exponent value, n : "))
    while n>11 or n<3:
            # check if exponent value is between 2 and 12
        n = int(input("Re-enter the Exponent value in between 2 and 12 : "))

    k = int(input("Enter Limit value of x and y, k : "))
    while(k<11):
        # check if Limit value is bigger than 10
        k = int(input("Re-enter the Limit Value(k) bigger than 10 : "))
    calculate_miss(n, k)

    # wait
    w = input("\nEnter any key for Exit : ")

# start the program by calling the near_miss function
near_miss()