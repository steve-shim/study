array = [7,5,9,0,3,1]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            print(f"{array[min_index]} -> min_index ({min_index})")
    print("SWAP! min_index", min_index)
    array[i], array[min_index] = array[min_index], array[i] # 스와프
    print(array)
print(array)