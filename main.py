# возвращает самое длинное слово
def longWord(a):
    l = list(a.split(' '))
    m = l[0]
    for i in l:
        if len(i)>len(m):
            m=i
    return m

# выводит уникальные эл-ты
def unique(a):
    c = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i]==a[j]:
                break
        else:
            c.append(a[i])
    return c

# палиндромы
def palindrom(a):
    b = a[::-1]
    if a == b:
        print('Palindrom')
    else:
        print('Not palindrom')

if __name__ == '__main__':
    # условие 1
    # a = input()
    # print(longWord(a))

    # условие 2
    # n = int(input())
    # a = []
    #
    # for i in range (n):
    #     a.append(int(input()))
    #
    # print(unique(a))

    # условие 3
    a = input()
    palindrom(a)