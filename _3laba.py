#задача1
import math
n=int(input())
def counter(n):
    k=1
    sum = 0
    while k<=n:
        sum += (-1)*k*((5-k)/factorial(k))
        k+=1
    return(sum)

def factorial(k):
    if k>1:
        return k*factorial(k-1)
    return(k)

print(round(sum(n))

#задача2
def fact(f):
   if f <= 1:
            return 1
   return f * factorial(f - 1)

def sum(n):
    S = 0
    for f in range (1, n + 1):
        S += -1 * f * ((5 - f) / fact(f))
    print(S)

#задача3
list = ["Crime and Punishment", 1, 331, 1866, "The Master and Margarita", 1, 470, 1966, "War and Peace", 4, 1274, 1869, "And Quiet Flows the Don", 4, 1600, 1940]
list = [list[i] for i in range(0, len(list), 4)]

dict={}

for word in list:
    if word in dict:
        dict[word]+=1
    else:
        dict[word] = 1
print(dict)

#задача4

list = ["Bass", "Pike", "Roach", "Catfish", "Trout", "Mackerel", "Salmon", "Zander", "Anchovy"]
new_list=[]
for word in list.split(", "):
    new_list.append(word[-1])
print (sorted(new_list, reverse=True))

#задача5
list = [14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]

dict={}
for x in list:
    if x>0:
        print("x:positive")
    if x<0:
        print("x:negative")
    if x==0:
        print("x:zero")
print(dict)
