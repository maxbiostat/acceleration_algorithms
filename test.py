import math
from acceleration import Aitken_tranform, Richardson_transform, Epsilon_transfom, G_transform

def square_serie(n: int) -> list:
    serie = [1.0]

    for i in range(2, n+1):
        serie.append(serie[-1] + 1/(i)**2)
    
    return serie

if __name__ == "__main__":
    for i in range(1, 6):
        initial_serie = abs(math.pi**2 / 6 - square_serie(10**i)[-1])
        acceration_serie = abs(math.pi**2 / 6 - Aitken_tranform(square_serie(10**i))[-1])

        print(f"Error in initial serie with n={10**i}: {initial_serie}")
        print(f"Errro in acceleration serie with n={10**i}: {acceration_serie}")
        print("\n")

    print(Epsilon_transfom(square_serie(10)))