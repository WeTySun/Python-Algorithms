"""Selection sort start by finding minimum value and put it beginning sorted list, when algorithm repeats."""

def selection_sort(input_l):
    for i in range(len(input_l)):
        min_i = i
        for j in range(i + 1, len(input_l)):
            if input_l[min_i] > input_l[j]:
                min_i = j


        input_l[i], input_l[min_i] = input_l[min_i], input_l[i]


l = [8,9,6,5,7,4,3,1,2]
selection_sort(l)
print(l)
