def total_inc_dec(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    
    increasing = [1] * 9
    decreasing = [1] * 9
    result = 10
    
    for i in range(2, n + 1):
        new_increasing = [0] * 9
        new_decreasing = [1] * 9
        inc_sum = 0
        dec_sum = 0
        
        for j in range(9):
            dec_sum += decreasing[j]
            new_decreasing[j] += dec_sum
            result += new_decreasing[j]
        
        for j in range(8, -1, -1):
            inc_sum += increasing[j]
            new_increasing[j] += inc_sum
            result += new_increasing[j]
        
        result -= 9
        increasing, new_increasing = new_increasing, increasing
        decreasing, new_decreasing = new_decreasing, decreasing
    
    return result
