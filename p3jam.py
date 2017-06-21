def bathroom(N,K):
    array = [1] + N*[0] +[1]
    storage_array = [-1] + N*[0] + [-1]
    
    for j in range(0,K):
        for i in range(0,N+2):
            if array[i] == 1:
                storage_array[i] = "Occupied"
            if storage_array[i] != "Occupied":
                ls = 0
                left = 1
                rs = 0
                right = 1
                while array[i-left] == 0:
                    left += 1
                    ls += 1
                while array[i+right] == 0:
                    right += 1
                    rs += 1
                storage_array[i] = (ls,rs)
                
        min_array = (N+2)*[-2]
        
        for i in range(0,N+2):
            if storage_array[i] != "Occupied":
                min_array[i] = min(storage_array[i])
                
        maxi = -1
        index_array = []
    
        for i in range(0,N+2):
            
            if min_array[i] > maxi:
                maxi = min_array[i]
                index_array = [i]
            elif min_array[i] == maxi:
                index_array.append(i)

   
                
        if len(index_array) == 1:
            array[index_array[0]] += 1
            if j == K-1:
          
                return max(storage_array[index_array[0]]),min(storage_array[index_array[0]])

        maxj = -1
        multi_index = []
        if len(index_array) > 1:

            for k in index_array:
                if max(storage_array[k]) > maxj:
                    multi_index = [k]
                    maxj = max(storage_array[k])
                elif max(storage_array[k]) == maxj:
                    multi_index.append(k)
            
            array[multi_index[0]] += 1
            
            if j == K-1:
                
                return max(storage_array[multi_index[0]]),min(storage_array[multi_index[0]])
        
        
                
            
            
                            
