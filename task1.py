import os

def selection_sort(numbers):
    for i in range(len(numbers)):
        min = i
        for j in range(i+1,len(numbers)):
            if numbers[min] > numbers[j]:
                min = j
        numbers[i], numbers[min] = numbers[min], numbers[i]


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


if __name__ == "__main__":
    method = os.getenv("METHOD")
    numbers = os.getenv("LIST_NUMBERS").split(",")
    numbers = [int(i) for i in numbers]
    if int(method) == 1:
        selection_sort(numbers)
    elif int(method) == 2:
        insertion_sort(numbers)
    print(numbers)
    