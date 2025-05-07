

def right_rotation(arr,s, queries):
    
    for j in range(s):
        tmp = arr.copy()
        arr[0] = tmp[-1]
        for i in range(len(arr)-1):
            arr[i+1] = tmp[i]
    
    res = []
    for q in queries:
        res.append(arr[q])
        
    
    return res


# --- CHAT GPT FAST AND SMART VERSION --- #

# def right_rotation(arr, s, queries):
#     n = len(arr)
#     s = s % n  # Optimize the number of rotations
#     rotated_arr = arr[-s:] + arr[:-s]
#     return [rotated_arr[q] for q in queries]
        


# Sample Test Cases for Circular Array Rotation

# Test Case 1: Basic rotation
print(right_rotation([1, 2, 3], 2, [0, 1, 2]))  # Expected output: [2, 3, 1]

# Test Case 2: Single element array
print(right_rotation([5], 10, [0]))  # Expected output: [5]

# Test Case 3: Full rotation (k is a multiple of n)
print(right_rotation([1, 2, 3, 4], 4, [0, 1, 2, 3]))  # Expected output: [1, 2, 3, 4]

# Test Case 4: Rotations larger than array size
print(right_rotation([4, 5, 6], 5, [0, 1, 2]))  # Expected output: [5, 6, 4]

# Test Case 5: All elements queried
print(right_rotation([10, 20, 30, 40, 50], 3, [0, 1, 2, 3, 4]))  # Expected output: [30, 40, 50, 10, 20]

# Test Case 6: Array with duplicate elements
print(right_rotation([1, 2, 3, 3, 2, 1], 2, [0, 1, 2, 3, 4, 5]))  # Expected output: [2, 1, 1, 2, 3, 3]

# Test Case 7: No rotations
print(right_rotation([10, 20, 30, 40], 0, [0, 2]))  # Expected output: [10, 30]

# Test Case 8: Single rotation
print(right_rotation([8, 6, 7, 5, 3, 0, 9], 1, [0, 6]))  # Expected output: [9, 0]

# Test Case 9: Maximum possible rotation
print(right_rotation([1, 2, 3], 100000, [0, 1, 2]))  # Expected output: [3, 1, 2]

# Test Case 10: Large input array
print(right_rotation(list(range(1, 101)), 50, [0, 99]))  # Expected output: [51, 50]