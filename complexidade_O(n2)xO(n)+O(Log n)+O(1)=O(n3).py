def exemplo_complexidade_cubica(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[j] > arr[k]:
                    arr[j], arr[k] = arr[k], arr[j] 
    log_operacao = 0
    l = 1
    while l < n:
        l *= 2
        log_operacao += 1 
    if n > 0:
        print("Operação_Realizada")
    return arr
exemplo_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_arr = exemplo_complexidade_cubica(exemplo_arr)
sorted_arr
