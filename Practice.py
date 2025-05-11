#1. Reverse a String

def reverse_string(string_to_reverse):
    result_string = ''
    for i in range(len(string_to_reverse)-1, -1, -1):
        result_string += string_to_reverse[i]
    return result_string


print(reverse_string("Dharni"))

#2. Check if a String is Palindrome


def is_palindrome1(input_string):
    if input_string == input_string[::-1]:
        return True
    else:
        return False


print(is_palindrome1("ABCDEDCBA"))


def is_palindrome2(input_string):
    start = 0
    end = len(input_string)-1
    while start < end:
        if input_string[start] != input_string[end]:
            return False
        start += 1
        end -= 1
    return True


print(is_palindrome2("ABCDEDCBA"))


#3. Find First Non-Repeating Character


def non_repeating(test_string):
    for i in range(len(test_string)):
        count = 0
        for j in range(len(test_string)):
            if test_string[i] == test_string[j]:
                count += 1
        if count == 1:
            return test_string[i]
    return None

print(non_repeating("swiss"))

#febnocci
def febnocci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("Enter any number: "))
febnocci(n)

#count a specific element in a list with list.count()
def countstring(fruits):
    return fruits.count('apple')


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
n = countstring(fruits)
print(n)

#count a specific element in a list without list.count()
def countstring(fruits, fruitcount):
    count = 0
    for fruit in fruits:
        if fruit == fruitcount:
            count+=1
    return count

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
n = countstring(fruits, 'apple')
print(n)

#Second largest:
def secondlargest(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if arr[i] > arr[i + 1]:
            return arr[i + 1]


n = secondlargest([-3, -5, -1, 0, 5, 4, 8, 10])
print(n)

#Replace with Index:
def replacewithindex1(arr):
    i = 0
    for fruit in arr:
        if 'banana' == fruit:
            arr.remove(fruit)
            arr.insert(i, 'papaya')
        i += 1
    return arr



def replacewithindex2(arr):
    for i in range(len(arr)):
        if arr[i] == 'banana':
            arr[i] = 'papaya'
    return arr


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(replacewithindex1(fruits))
print(replacewithindex2(fruits))



