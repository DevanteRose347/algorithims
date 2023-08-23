### Exercise #1 <br>
# Reverse the list below in-place using an in-place algorithm.

def swap(alist, l, t, x, y, z):
    alist[l], alist[t], alist[x], alist[y], alist[z]= alist[z], alist[y], alist[x], alist[t], alist[l]
    return alist
words = ['this' , 'is', 'a', 'sentence', '.']

print(f"Before swap: {words}")
swap(words, 0, 1, 2, 3, 4,)
print(f"After swap: {words}")

### Exercise #2 <br>
# Create a function that counts how many distinct
# words are in the string below,then outputs a dictionary 
# with the words as the key 
# and the value as the amount of times that word appears 
# in the string.
# Should output:{'a': 5,
#  'abstract': 1,
#  'an': 3,}

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

word_D = {}
my_W_list = a_text.split()
num_of_words = len(my_W_list)
print(num_of_words)

for name in my_W_list:
    if name not in word_D:
        word_D[name] = 1
    else:
        word_D[name] += 1

    

print(word_D)


