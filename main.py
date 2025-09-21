
"""
MaxMin Select (maior e menor simultâneos) por Divisão e Conquista.
"""
from __future__ import annotations
from typing import Iterable, Tuple, List

def max_min_select(arr: Iterable[float]) -> Tuple[float, float]:
    """
    Retorna (menor, maior) de arr usando divisão e conquista.
    - Levanta ValueError se arr estiver vazio.
    - Converte o iterável em lista apenas uma vez.
    """
    lst = list(arr)
    n = len(lst)
    if n == 0:
        raise ValueError("Sequência vazia: forneça ao menos um elemento.")
    return _max_min_dc(lst, 0, n - 1)

def _max_min_dc(a: List[float], lo: int, hi: int) -> Tuple[float, float]:
    """Implementação recursiva: retorna (min, max) no intervalo [lo, hi]."""
    length = hi - lo + 1

    # Caso base 1: um elemento (0 comparações).
    if length == 1:
        x = a[lo]
        return (x, x)

    # Caso base 2: dois elementos (1 comparação para ordenar par).
    if length == 2:
        x, y = a[lo], a[hi]
        if x <= y:  # 1 comparação
            return (x, y)
        else:
            return (y, x)

    # Recursão: divide em duas metades aproximadamente iguais.
    mid = (lo + hi) // 2
    minL, maxL = _max_min_dc(a, lo, mid)
    minR, maxR = _max_min_dc(a, mid + 1, hi)

    # Combinação (2 comparações): compara máximos e mínimos separadamente.
    # 1) maior entre maxL e maxR
    if maxL >= maxR:
        overall_max = maxL
    else:
        overall_max = maxR

    # 2) menor entre minL e minR
    if minL <= minR:
        overall_min = minL
    else:
        overall_min = minR

    return (overall_min, overall_max)

class Counter:
    def __init__(self):
        self.c = 0
    def le(self, x, y):  # x <= y
        self.c += 1
        return x <= y
    def ge(self, x, y):  # x >= y
        self.c += 1
        return x >= y

def max_min_select_with_counter(arr: Iterable[float]) -> Tuple[float, float, int]:
    """
    Igual a max_min_select, mas retorna também o número de comparações
    feitas na etapa de combinação (duas por nó interno).
    """
    lst = list(arr)
    n = len(lst)
    if n == 0:
        raise ValueError("Sequência vazia: forneça ao menos um elemento.")
    ctr = Counter()
    mn, mx = _max_min_dc_count(lst, 0, n - 1, ctr)
    return mn, mx, ctr.c

def _max_min_dc_count(a: List[float], lo: int, hi: int, ctr: Counter) -> Tuple[float, float]:
    length = hi - lo + 1
    if length == 1:
        x = a[lo]
        return (x, x)
    if length == 2:
        x, y = a[lo], a[hi]
        # 1 comparação
        if ctr.le(x, y):
            return (x, y)
        else:
            return (y, x)

    mid = (lo + hi) // 2
    minL, maxL = _max_min_dc_count(a, lo, mid, ctr)
    minR, maxR = _max_min_dc_count(a, mid + 1, hi, ctr)

    # 2 comparações na combinação
    overall_max = maxL if ctr.ge(maxL, maxR) else maxR
    overall_min = minL if ctr.le(minL, minR) else minR
    return (overall_min, overall_max)

if __name__ == "__main__":
    import sys, random

    if len(sys.argv) > 1:
    
        data = [float(x) for x in sys.argv[1:]]
    else:
        
        random.seed(42)
        data = [random.randint(-50, 50) for _ in range(11)]

    mn, mx = max_min_select(data)
    mn2, mx2, comps = max_min_select_with_counter(data)

    print("Entrada:", data)
    print("Min/Max  :", (mn, mx))
    print("Min/Max* :", (mn2, mx2), f" | comparações (combinação) = {comps}")
