
# Bubble sort implementation using python
def bubble_sort(sequence):
     l=len(sequence)
     for i in range (l-1,0,-1):
         for j in range(i):
             if sequence[j] > sequence[j+1]:
                 temp=sequence[j]
                 sequence[j]=sequence[j+1]
                 sequence[j+1]=temp


sequence = [9,4,3,7,1,5,2]
bubble_sort(sequence)
print(sequence)

                 
