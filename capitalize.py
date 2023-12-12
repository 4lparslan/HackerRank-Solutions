# Complete the solve function below.
def solve(s):
    ss = s.split(' ')
    res = ' '.join(word.capitalize() for word in ss)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
