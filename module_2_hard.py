import random
def rebus():
    code = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice (code)
    return n
n = rebus()
print(n)
code_2 = []
for two in range (1, 20):
    for three in range (1, 20):
        if n % (two+three) == 0 and two != three and two < three:
            code_2.extend([two,three])
    else:
        pass
print('result: ', *code_2)
