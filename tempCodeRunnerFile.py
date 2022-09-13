# main function to implement radix sort
def radixSort(inputArray):
    # get maximum element of input array
    max = inputArray[0]
    for i in range(len(inputArray)):
        if inputArray[i] > max:
            max = inputArray[i]

    # apply counting sort fn to sort elements based on each place value
    # '//' is floor division, decimal part gone
    # 405 // 1 = 405 > 0, 405 // 1000 = 0 not > 0
    # place=1's place, 10's place, 100's place, 1000's place . .
    place = 1
    while max // place > 0:
        countingSort(inputArray, place)
        place *= 10


# countingSort function is called to sort elements based on digit places
def countingSort(inputArray, place):
    size = len(inputArray)
    outputArray = [0]*size
    # numbers at particular digit places will always be 0 - 10
    countArray = [0]*10

    # countArray[i] will contain number of times index, i appears at particular digit place of inputArray
    for i in range(size):
        temp = inputArray[i] // place         # 389 // 1=389
        countArray[temp % 10] += 1            # 389 % 10=9

    # countArray[i] will contain number of elements less than or equal to i at particular digit place of inputArray, called cumulative count. Keep the first element intact
    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    # start from end index of inputArray, match respective place's digit of the element at that index with countArray index, decrease the element at the index of countArray by 1, copy respecive element of inputArray to outputArray at sorted position
    for i in range(size-1, -1, -1):
        temp = inputArray[i] // place
        countArray[temp % 10] -= 1
        outputArray[countArray[temp % 10]] = inputArray[i]

    # copy whole outputArray to inputArray
    for i in range(size):
        inputArray[i] = outputArray[i]


A = [389, 405, 8, 32]
radixSort(A)
print(A)            # [8, 32, 389, 405]
