def mk_star(n, temp):
    temp_rec = []
    if n == 3:
        return temp
    else:
        for i in temp:
            temp_rec.append(i*3)
        for i in temp:
            temp_rec.append((i + ' '*len(temp) + i))
        for i in temp:
            temp_rec.append(i*3)

        return mk_star(n//3, temp_rec)


star = ['***', '* *', '***']
n = int(input())
stars = mk_star(n, star)

for i in stars:
    print(i)