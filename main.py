##################################
# FOR ENTER THE LIST OF NUMBERS. #
##################################

print("\n\n\n\n\n\n\n\n\n")
nos=int(input("Enter no of values : "))
print("\n\n\n\n\n")
data=[]
while len(data) < nos :
    numbers=int(input("Enter the number : "))
    data.append(numbers)
print("\n\n\n\n")
# print(data)

#######################################################
# FINDING THE DIVISORS OF EACH NUMBERS FROM THE LIST. #
#######################################################

for k in range(len(data)) :
    div=[]
    num=data[k]

    for i in range(1,num+1) :
        if num % i == 0 :
            div.append(i)

    print(f"\n\nDivisors of {num} are : {div}")

###########################################
# FINDING THE GCD OF THE LIST OF NUMBERS. #
###########################################

print("\n\n\n")

for gcd in range(min(data),0,-1) :
    for b in range(1,len(data)+1) :
        if data[b-1] % gcd != 0 :
            break
    else :
        print(f"\n\nThe G.C.D. of {data} is {gcd}.")
        break

###########################################
# FINDING THE LCM OF THE LIST OF NUMBERS. #
###########################################

lcm=max(data)
while True :
    for a in range(1,len(data)+1) :
        if lcm % data[a-1] != 0 :
            lcm+=1
            break
    else :
        print(f"\n\nThe L.C.M. of {data} is {lcm}.")
        break
print("\n\n\n\n\n\n\n\n\n")

#############################################
# THANKS FROM ARDHENDU SHEKHAR (@asbpintu). #
#############################################