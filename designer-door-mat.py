# Enter your code here. Read input from STDIN. Print output to STDOUT

# N -> height
# M -> width
N, M = map(int, input().split())

c = '-'
txt = "WELCOME"
r = '.|.'

# top
for i in range(int((N-1)/2)):
    print(r.center(M,c))
    r+= '.|..|.'
    
# middle
print(txt.center(M, c))

r = '.|.'
# bottom
for i in range(int((N-1)/2), 0, -1):
    a = 1 + (i - 1) * 2
    print((r*a).center(M, c))
