"""
Exercício 1 - Lista 4
Implemente os seguintes algoritmos de ordenação e modifique-os para imprimir
a quantidade de testes e trocas efetuadas durante a ordenação.
"""


def insertion_sort(arr):
    """Insertion Sort - O(n²)"""
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    
    return arr, comparisons, swaps


def selection_sort(arr):
    """Selection Sort - O(n²)"""
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    
    return arr, comparisons, swaps


def bubble_sort(arr):
    """Bubble Sort - O(n²)"""
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    
    return arr, comparisons, swaps


def shell_sort(arr):
    """Shell Sort - O(n log n)"""
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap:
                comparisons += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break
            arr[j] = temp
        gap //= 2
    
    return arr, comparisons, swaps


def merge_sort(arr):
    """Merge Sort - O(n log n)"""
    comparisons = [0]
    swaps = [0]
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                swaps[0] += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        
        return merge(left, right)
    
    sorted_arr = merge_sort_recursive(arr.copy())
    return sorted_arr, comparisons[0], swaps[0]


def quick_sort(arr):
    """Quick Sort - O(n log n)"""
    arr = arr.copy()
    comparisons = [0]
    swaps = [0]
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                if i != j:
                    swaps[0] += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        if i + 1 != high:
            swaps[0] += 1
        return i + 1
    
    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)
    
    quick_sort_recursive(0, len(arr) - 1)
    return arr, comparisons[0], swaps[0]


def heap_sort(arr):
    """Heap Sort - O(n log n)"""
    arr = arr.copy()
    comparisons = [0]
    swaps = [0]
    
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n:
            comparisons[0] += 1
            if arr[left] > arr[largest]:
                largest = left
        
        if right < n:
            comparisons[0] += 1
            if arr[right] > arr[largest]:
                largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps[0] += 1
            heapify(n, largest)
    
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        swaps[0] += 1
        heapify(i, 0)
    
    return arr, comparisons[0], swaps[0]


def counting_sort(arr):
    """Counting Sort - O(n + k)"""
    if not arr:
        return arr, 0, 0
    
    comparisons = 0
    swaps = 0
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Contagem de elementos
    for num in arr:
        count[num - min_val] += 1
        comparisons += 1
    
    # Acumulação
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Construção do array ordenado
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        swaps += 1
    
    return output, comparisons, swaps


def exercicio_1():
    """Exercício 1: Algoritmos de Ordenação com contagem de operações"""
    print("\n" + "="*70)
    print("EXERCÍCIO 1 - LISTA 4")
    print("="*70)
    print("Algoritmos de Ordenação")
    print("Contagem de Comparações e Trocas")
    print("="*70)
    
    # Listas de teste
    test_lists = [
        [12, 42, 83, 25, 67, 71, 3, 4, 94, 53],
        [100, 48, 19, 61, 86, 33, 13, 43, 84, 28],
        [81, 60, 6, 49, 40, 41, 38, 64, 44, 36],
        [45, 27, 11, 89, 63, 39, 9, 58, 52, 17],
        [88, 77, 26, 62, 30, 96, 56, 65, 98, 99],
        [76, 73, 16, 95, 35, 87, 68, 69, 51, 92],
        [37, 75, 90, 82, 8, 18, 23, 93, 57, 10],
        [15, 97, 14, 29, 7, 24, 31, 59, 78, 85],
        [5, 70, 55, 91, 47, 72, 2, 20, 34, 74],
        [50, 66, 32, 22, 54, 79, 21, 1, 80, 46]
    ]
    
    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Selection Sort", selection_sort),
        ("Bubble Sort", bubble_sort),
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort)
    ]
    
    # Executar cada algoritmo em cada lista de teste
    for idx, test_list in enumerate(test_lists, 1):
        print(f"\n{'='*70}")
        print(f"LISTA DE TESTE {idx}: {test_list}")
        print(f"{'='*70}")
        
        for name, algorithm in algorithms:
            sorted_arr, comparisons, swaps = algorithm(test_list)
            print(f"\n{name}:")
            print(f"  Lista ordenada: {sorted_arr}")
            print(f"  Comparações: {comparisons}")
            print(f"  Trocas: {swaps}")
    
    # Sumário comparativo
    print("\n" + "="*70)
    print("SUMÁRIO COMPARATIVO - Média de operações em todas as listas")
    print("="*70)
    
    for name, algorithm in algorithms:
        total_comp = 0
        total_swaps = 0
        
        for test_list in test_lists:
            _, comp, swaps = algorithm(test_list)
            total_comp += comp
            total_swaps += swaps
        
        avg_comp = total_comp / len(test_lists)
        avg_swaps = total_swaps / len(test_lists)
        
        print(f"\n{name}:")
        print(f"  Média de comparações: {avg_comp:.1f}")
        print(f"  Média de trocas: {avg_swaps:.1f}")
        print(f"  Total de operações: {avg_comp + avg_swaps:.1f}")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    exercicio_1()
