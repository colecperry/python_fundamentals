def EvenOddSort(x):
    even_list = []
    odd_list = []
    for i in range(len(x)):
        if i % 2 == 0:
            even_list.append(x[i])
        else:
            odd_list.append(x[i])
    even_list.extend(odd_list)
    return even_list

def MultipleSort(x,N):
    """ Returns a list obtained by performing N even-odd sorts of the
    list x. The list x is not altered.
    Precondition: x is a list with even length and N is a positive int. """
    sorted_list = list(x) # Create a copy of the original list
    for i in range(N): # Run the EvenOddSort function "N" times
        sorted_list = EvenOddSort(sorted_list) # Run the EvenOddSort function and store answer in variable "sorted_list" to use in the next loop
    return sorted_list

# Answer without making a copy
def MultipleSort2(x,N):
    for i in range(N):
        x = EvenOddSort(x)
    return x



# print(EvenOddSort(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))
print(MultipleSort(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 2))
# print(MultipleSort2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 2))