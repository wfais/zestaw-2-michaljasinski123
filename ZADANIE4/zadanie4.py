import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    # Funkcja oblicza częściową sumę przybliżenia liczby pi metodą prostokątów.
    # Argumenty:
    #     pocz, kon - zakres iteracji (indeksy kroków całkowania),
    #     krok      - szerokość pojedynczego prostokąta (1.0 / LICZBA_KROKOW),
    #     wyniki    - lista, do której należy wpisać wynik dla danego wątku na pozycji indeks,
    #     indeks    - numer pozycji w liście 'wyniki' do zapisania rezultatu.

    # Każdy wątek powinien:
    #   - obliczyć lokalną sumę dla przydzielonego przedziału,
    #   - wpisać wynik do wyniki[indeks].

     # zaimplementuj obliczanie fragmentu całki dla danego wątku
    suma = 0.0
    for i in range(pocz,kon):
        x = (i+0.5)*krok
        suma+= 4.0/(1+x**2)
    wyniki[indeks] = suma


def main():
    print(f"Python: {sys.version.split()[0]}  (tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    # Wstępne uruchomienie w celu stabilizacji środowiska wykonawczego
    krok = 1.0 / LICZBA_KROKOW
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    w.start()
    w.join()

    # ---------------------------------------------------------------
    # Tu zaimplementować:
    #   - utworzenie wielu wątków (zgodnie z LICZBY_WATKOW),
    #   - podział pracy na zakresy [pocz, kon) dla każdego wątku,
    #   - uruchomienie i dołączenie wątków (start/join),
    #   - obliczenie przybliżenia π jako sumy wyników z poszczególnych wątków,
    #   - pomiar czasu i wypisanie przyspieszenia.
    # ---------------------------------------------------------------
    czas_1_watek = 0.0
    for watki_liczba in LICZBA_WATKOW:
        t1 = time.perf_counter()
        watki = []
        wyniki = [0.0]*watki_liczba
        liczba_krokow = LICZBA_KROKOW//watki_liczba
        for j in range(watki_liczba):
            poczatek = j*liczba_krokow
            if j == watki_liczba-1:
                koniec = LICZBA_KROKOW
            else:
                koniec = (j+1)*liczba_krokow
            w = threading.Thread(target=policz_fragment_pi, args=(poczatek, koniec, krok, wyniki, j))
            watki.append(w)
            w.start()
        for w in watki:
            w.join()
        pi = sum(wyniki)*krok
        t2 = time.perf_counter() 
        czas = t2-t1
        if watki_liczba == 1:
            czas_1_watek=czas
        print(f"Wątki: {watki_liczba}, Czas: {round(czas, 5)} s, Przyspieszenie: {round(czas_1_watek/czas,3)}, Wartość liczby π: {round(pi,14)}")

if __name__ == "__main__":
    main()
