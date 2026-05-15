def norms(vector:list):
    # This function calculates the norms of the vector
    l1 = 0
    l2 = 0 
    l3 = 0
    for i in range(len(vector)):
        val = abs(vector[i])
        l1 += val
        l2 += pow(val,2)
        l3 += pow(val,3)

    l2 = pow(l2,1/2)
    l3  = pow(l3,1/3)
    print(f"L1: {l1} L2: {l2} L3: {l3}")
    return 0

def nthnorm(vector:list,order:int):
    value = (sum([x**order for x in vector]))**(1/order)
    return value




vector  = [1,2,3]
norms(vector)

for i in range(3):
    print(f"\n{i+1}th nomalization with list comprehension: {nthnorm(vector,i+1)}", end=" ")
