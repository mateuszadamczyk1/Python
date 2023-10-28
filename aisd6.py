#Quick sort
#Mateusz Adamczyk

import random
import time

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

large_list = generate_random_list(10000)

start_time = time.time()
sorted_list = quick_sort(large_list)
end_time = time.time()


print("Sorted List:")
print(sorted_list[:1000]) 
print(f"Time taken: {end_time - start_time} seconds")


#Czas sortowania dla 1000 losowo wygenerowanych liczb:
#Quick Sort: 0.2 sekundy
