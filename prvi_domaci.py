# fja vraca niz prvih n clanova fibonacija

def fibonaci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    stari = fibonaci(n-1)
    return stari + [stari[-1]+stari[-2]]


n = int(input("Unesite prirodan br veci od 0: "))
if n < 0:
    print("Nije unet prirodan broj veci od nula!")
    exit()

print(fibonaci(n))
