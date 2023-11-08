## LCM-GCD-and-Divisors

#### Hi I am Ardhendu Shekhare , This is a small programme to find out the LCM and GCD of 2 or more than two numbers, also we can get all the divisors of every numbers.

---
**Code:-**
```JS
##################################
# FOR ENTER THE LIST OF NUMBERS. #
##################################
​
print("\n")
nos=int(input("Enter no of values : "))
print("\n")
data=[]
while len(data) < nos :
    numbers=int(input("Enter the number : "))
    data.append(numbers)

​
#######################################################
# FINDING THE DIVISORS OF EACH NUMBERS FROM THE LIST. #
#######################################################
​
for k in range(len(data)) :
    div=[]
    num=data[k]
​
    for i in range(1,num+1) :
        if num % i == 0 :
            div.append(i)
​
    print(f"\n\nDivisors of {num} are : {div}")
​
###########################################
# FINDING THE GCD OF THE LIST OF NUMBERS. # 
###########################################
​
for gcd in range(min(data),0,-1) :
    for b in range(1,len(data)+1) :
        if data[b-1] % gcd != 0 :
            break
    else :
        print(f"\n\nThe G.C.D. of {data} is {gcd}.")
        break
​
###########################################
# FINDING THE LCM OF THE LIST OF NUMBERS. #
###########################################
​
lcm=max(data)
while True :
    for a in range(1,len(data)+1) :
        if lcm % data[a-1] != 0 :
            lcm+=1
            break
    else :
        print(f"\n\nThe L.C.M. of {data} is {lcm}.")
        break
​
#############################################
# THANKS FROM ARDHENDU SHEKHAR (@asbpintu). # 
#############################################
```
### *Result:-*
```
Enter no of values : 3


Enter the number : 12
Enter the number : 24
Enter the number : 36


Divisors of 12 are : [1, 2, 3, 4, 6, 12]


Divisors of 24 are : [1, 2, 3, 4, 6, 8, 12, 24]


Divisors of 36 are : [1, 2, 3, 4, 6, 9, 12, 18, 36]


The G.C.D. of [12, 24, 36] is 12.


The L.C.M. of [12, 24, 36] is 72.
```

_**Thank you !!!**_
**Visit Again**
