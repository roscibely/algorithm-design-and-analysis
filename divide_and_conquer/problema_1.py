def tower_of_Hanoi(N , source, destination, auxiliary):
    """
    Args: 
        N: number of disks
        source: source rod
        destination: destination rod
        auxiliary: auxiliary rod

    """
    if N==1:
	    print("Mova o disco 1 da torre",source,"para torre",destination)
	    return
    
    tower_of_Hanoi(N-1, source, auxiliary, destination)
    print("Mova o disco",N,"da torre",source,"para torre",destination)
    tower_of_Hanoi(N-1, auxiliary, destination, source)

if __name__ == "__main__":
    tower_of_Hanoi(3, 'A', 'C', 'B')		
