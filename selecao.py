def selection_sort(v):
    for i in range(len(v)):
        min_idx = i
        for j in range(i +1, len(v)):
            if v[min_idx] > v[j]:
                min_idx = j
        
        v[i], v[min_idx] = v[min_idx], v[i]
    return v

if __name__ == '__main__':
    v = [1, 0, 2, 6, 3, 4, 7, 5]
    selection_sort(v)
    print(v)    
