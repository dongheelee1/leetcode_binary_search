def binary_search_template_1(arr, target): 

  if len(arr) == 0: 
    return -1 
  
  left, right = 0, len(arr)-1 
  
  while left <= right: 
    mid = (left + right)//2
    
    if target == arr[mid]: 
      return mid 
    elif target > arr[mid]: 
      return left = mid + 1
    else: 
      return mid - 1
      
  return -1 
