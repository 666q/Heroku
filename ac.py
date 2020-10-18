not_p = []
e = []
lim = 541


def primo(num):
    if num != 1:
        t = True
        for i in range(2, num):
            if num % i == 0:
                t = False
                break
        return t

 
for num in range(2, lim + 1):
    test = primo(num)
    if (test):
        e.append(num)
    else:
        not_p.append(num)

print("Números primos: ", e)
