# fja vraca niz prvih n clanova fibonacija

def fibonaci(n):
    # izlazni slucaj za rekurziju
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    stari = fibonaci(n-1) # uzima niz iz bazicnog slucaj [0, 1] i pocne da "razvija rekurziu unazad"
    return stari + [stari[-1]+stari[-2]] # dodaje zbir poslednja dva na niz
# fja za neki br n, pravi n-1 listu, doda novi elem.
# zbirom poslednja dva, zatim tu novu listu vraca gore po rekurzivnom steku

n = int(input("Unesite prirodan br veci od 0: ")) # unos br n
if n < 0:
    print("Nije unet prirodan broj veci od nula!") # izbacivanje greske i prekid programa
    exit()

print(fibonaci(n)) # poziv fje i stampa
