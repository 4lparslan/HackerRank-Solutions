def print_formatted(number):
    ps = len(bin(number)[2:])
    for i in range(1, number+1):
        print(f"{str(i).rjust(ps, ' ')} {format(i, 'o').rjust(ps, ' ')} {hex(i)[2:].upper().rjust(ps, ' ')} {bin(i)[2:].rjust(ps, ' ')}")
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
