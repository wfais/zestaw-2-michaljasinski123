def rzymskie_na_arabskie(rzymskie):
    arabskie_sl = {                                   
        "M":1000, "D":500,"C":100,"L":50, "X":10,"V":5, "I":1
    }
    if not isinstance(rzymskie, str) or not rzymskie:
        raise ValueError("Niepoprawna liczba rzymska")

    for i in rzymskie:
        if i not in arabskie_sl or i in ["IIII", "VV","VVVV", "XXXX", "LL","LLLL", "CCCC", "DD", "MMMM"]:
            raise ValueError
        
    wartosc = 0 
    ost_cyfra = 0
    for i in rzymskie[::-1]:
        liczba = arabskie_sl[i]
        if liczba>=ost_cyfra:
            wartosc+=liczba
            ost_cyfra = liczba
        else:
            wartosc-=liczba
    if rzymskie != arabskie_na_rzymskie(wartosc):
        raise ValueError 
    return wartosc

def arabskie_na_rzymskie(arabskie):
    rzymskie_sl = {                                   
        1000: "M",900:"CM", 500: "D",400:"CD", 100: "C",90:"XC",
        50:"L",40:"XL", 10:"X",9:"IX", 5:"V",4:"IV", 1:"I"
    }
    if arabskie>3999 or arabskie<1:
        raise ValueError("Liczba musi być w zakresie 1-3999")
    rzymskie = ""
    reszta = arabskie
    for i in rzymskie_sl.keys():
        if reszta>0:
            mnoznik = i
            rzymska = rzymskie_sl[i]
            ilosc = reszta//mnoznik
            reszta%=mnoznik
            rzymskie+=rzymska*ilosc
    return rzymskie

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        arabska = 1994
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
