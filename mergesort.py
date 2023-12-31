"""
Merge Sort is one the most popular sorting algorithms that is based one
the principle of Divide and Conquer Algorithm. Here, a problem is divided
into multiple sub-problems. Each sub-problem is solved individually.
Finally, sub-problems are combined to form the final solution.
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr
        
        
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(merge_sort(arr))
    