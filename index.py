# Insertion Sort in Python Implementation
def insertion_sort(A):
    for j in range(1, len(A)):
        Key = A[j]

        # insert A[j] into sorted list, A[0, ..., j-1]
        i = j-1
        while i >= 0 and A[i] > Key:
            A[i+1] = A[i]
            i = i-1

        A[i+1] = Key

    print(A)


insertion_sort([6, 5, 3, 1, 8, 7, 2, 4])        # [1, 2, 3, 4, 5, 6, 7, 8]
