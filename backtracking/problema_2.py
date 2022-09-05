def knapSack(maximum_weight,list_of_weights,list_of_values,number_of_items):
    """
    Function that solves the knapsack problem using backtracking

    Agrs:
        maximum_weight: maximum weight knapscak (int)
        list_of_weights:  weights  (list)
        list_of_values:  values          (list)
        number_of_items:  number of items (int)

    Returns:
        maximum value (list)
    """
    
    if(maximum_weight == 0 or number_of_items == 0):
        return [0,[]]
        
    if(list_of_weights[number_of_items-1] > maximum_weight):
        # discard the last item
        return knapSack(maximum_weight,list_of_weights,list_of_values,number_of_items-1)
        
    set1 = knapSack(maximum_weight-list_of_weights[n-1],list_of_weights,list_of_values,number_of_items-1)
    set2 = knapSack(maximum_weight,list_of_weights,list_of_values,number_of_items-1)
    
    if(set1[0]+list_of_values[number_of_items-1] > set2[0]):
        set1[1].append(number_of_items-1)
        set1[0] += list_of_values[number_of_items-1]
        return set1
    else:
        return set2

if __name__ == "__main__":
    maximum_weight = 8
    list_of_weights = [2,3,4,5]
    v = [3,5,6,10]
    n = len(list_of_weights)
    print(knapSack(maximum_weight,list_of_weights,v,n))    