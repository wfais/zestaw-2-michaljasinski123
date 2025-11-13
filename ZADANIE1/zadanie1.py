def dodaj_element(wejscie):
    def najglebsza(lista, poziom=0):
        if isinstance(lista, (list, tuple, dict)):
            max_poziom = -1
            najg = []
            if isinstance(lista, dict):
                lista2 = lista.values()
            elif isinstance(lista, list):
                lista2 = lista
                max_poziom = poziom
                najg = [lista]
            else:
                lista2 = lista
            for i in lista2:
                nowypoziom, podlista = najglebsza(i, poziom+1)
                if not lista2:
                    continue
                if nowypoziom>max_poziom:
                    max_poziom = nowypoziom
                    najg = podlista
                elif nowypoziom == max_poziom:
                    najg+=podlista
            return max_poziom, najg
        else:
            return -1, []
        
    poziom, najbardziej_zagniezdzona = najglebsza(wejscie)
    for najglebsze in najbardziej_zagniezdzona:
        if isinstance(najglebsze, list):
            max_val=0
            jest_liczba = False
            for liczba in najglebsze:
                if isinstance(liczba, int):
                    jest_liczba= True
                    if liczba>max_val:
                        max_val=liczba
            if jest_liczba:
                najglebsze.append(max_val+1)
            else:
                najglebsze.append(1)
    return wejscie 
    


if __name__ == '__main__':
    input_list = [
     1, 2, [3, 4, [5, {"klucz": [5, 6], "tekst": [1, 2]}], 5],
     "hello", 3, [4, 5], 5, (6, (1, [7, 8]))
    ]
    output_list = dodaj_element(input_list)
    print(input_list)  