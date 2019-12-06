original = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]


for noun in range(100):
    for verb in range(100):
        input2 = original.copy()
        i = 0
        input2[1] = noun
        input2[2] = verb
        
        while input2[i] != 99:
            op = input2[i]
            a = input2[input2[i+1]]
            b = input2[input2[i+2]]
            if op == 1:
                input2[input2[i+3]] = a + b
            elif op == 2:
                input2[input2[i+3]] = a * b
            i += 4
            if input2[0] == 19690720:
                print(input2[1])
                print(input2[2])
                print(100 * input2[1] + input2[2])
        




        

