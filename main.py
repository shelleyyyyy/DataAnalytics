

def computerWeightedAvg(w, x):
    sum_one = 0
    
    for i in range(len(w)):
        add_on = w[i] * x[i]
        sum_one = sum_one + add_on
        
    sum_two = 0
    
    for i in w:
        sum_two = sum_two + i
        
    final = sum_one / sum_two
    
    return final


x = [1, 2, 3, 4, 5, 6, 7]
w = [1, 2, 3, 4, 5, 6, 7]

print(computerWeightedAvg(x, w))

w = [1, 2, 3, 4, 5, 6, 7]

def show_loop():
    for i in w:
        print(i)
        
show_loop()