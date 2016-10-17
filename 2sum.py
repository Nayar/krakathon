inputs = [3, 5, 2, -4, 8, 11]
sum = 7

def find_sum_1(nums):
    res = []
    for i in range(len(inputs)):
        for j in range(i,len(inputs)-1):
            j = j + 1
            print "checing %d %d %d" % (inputs[i],inputs[j], inputs[i] + inputs[j])
            if((inputs[i] + inputs[j]) == 7):
                res.append([inputs[i],inputs[j]])
    return res
    
print inputs
print find_sum_1(inputs)