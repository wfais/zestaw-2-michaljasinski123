import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Generowanie wartości x i y przy użyciu eval()
    wielomian, zakres = wejscie.split(", ")
    x0 = int(zakres.split(" ")[0])
    x1 = int(zakres.split(" ")[1])
    x_val = np.linspace(x0, x1, 200)
    y_val = np.array([eval(wielomian.replace("x", f"({str(x)})")) for x in x_val])
    
    # Rysowanie wykresu ale bez show()
    plt.plot(x_val, y_val, label = f"{wielomian}")
    plt.xlabel("x")
    plt.ylabel("f[x]")
    plt.legend()
    plt.title(f"Wykres wielomianu")
    plt.grid()
    plt.legend()

    # Zwracanie wartości na granicach przedziału
    return y_val[0], y_val[-1]
  

# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Definicja symbolu i konwersja do funkcji numerycznej za pomocą SymPy
    # Generowanie wartości x i y przy użyciu funkcji numerycznej
    wielomian, zakres = wejscie.split(", ")
    x0 = int(zakres.split(" ")[0])
    x1 = int(zakres.split(" ")[1])
    x_val_sympy = np.linspace(x0, x1, 200)
    x = symbols('x')
    fn = lambdify(x, sympify(wielomian), "numpy") 
    y_val_sympy = [fn(x) for x in x_val_sympy]
    # Rysowanie wykresu ale bez show()
    plt.plot(x_val_sympy, y_val_sympy, label = f"{wielomian}")
    plt.xlabel("x")
    plt.ylabel("f[x]")
    plt.title(f"Wykres wielomianu")
    plt.grid()
    plt.legend()

    # Zwracanie wartości na granicach przedziału
    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "x**3 + 3*x + 1, -10 10"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)
    
    # Drugie wejście dla funkcji SymPy - bardziej złożona funkcja 
    wejscie2 = "x**4 - 5*x**2 + 3*sin(x), -10 10"  
    
    # Drugi wykres z SymPy
    wynik_sympy = rysuj_wielomian_sympy(wejscie2)
    print("Wynik (SymPy):", wynik_sympy)
    
    # Wyświetlanie obu wykresów
    plt.grid()
    plt.show()