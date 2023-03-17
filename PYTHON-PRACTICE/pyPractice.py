""" 
'''
def something(a):
    return str(a) + "hello"

myList=["1","Hello",1]

b=map(something,myList)

print(b)

print(list(b))
'''
'''
x = 5 6
12 13 14'''
 
'''y=x.split('\n')

'''

# Zipped in python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Zipped in python - Hacker Rank Solution START
N, X = input().split()

io = []

for _ in range(int(X)):
    ip = map(float, input().split())
    io.append(ip)
""" 
""" print(type(io))


print(list(zip(*io)))
print("here") 
for i in zip(*io): 
    print( sum(i)/len(i) )  """
# Zipped in python - Hacker Rank Solution END  


f = open("../artifacts.txt",'a')

#print(f.read(100))

f.write("add this content")

f = open("../artifacts.txt",'r')
print(f.read())