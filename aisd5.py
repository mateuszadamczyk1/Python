#Bubble sort
#Mateusz Adamczyk

import random
import time

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

large_list = generate_random_list(10000)

start_time = time.time()
sorted_list = bubble_sort(large_list.copy())  
end_time = time.time()

print("Sorted List:")
print(sorted_list[:1000])  
print(f"Time taken: {end_time - start_time} seconds")


#Czas sortowania dla 1000 losowo wygenerowanych liczb:
#Bubble Sort: 7.2 sekundy