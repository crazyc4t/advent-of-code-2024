# https://adventofcode.com/2024/day/1
# Said Neder
# crazyc4t.xyz

# Enter each list from the puzzle set into a python list
# Then find the smallest item in each list, substract them and add the remainder for total distance

# Open the puzzle input
f = open("puzzle_input.txt", "r")

# Create both lists and total distance
list1 = []
list2 = []
total_distance = 0
similarity_score = 0

# read each line, split them, trim it and save it to their chosen lists
for line in f:
    left, right = line.split()  # split at space
    list1.append(int(left.strip()))  # remove whitespace
    list2.append(int(right.strip()))


# Find min of list 1 and list 2, substract them
# Use selection sort
# assign index i = 0, loop through i < len(list), find smallest element in list[i:], swap the smallest element with list[i], increase i by 1
def swap(L, in1, in2):
    temp = L[in1]
    L[in1] = L[in2]
    L[in2] = temp


def selection_sort(L):
    for i in range(len(L)):
        index = i
        for j in range(i + 1, len(L)):
            if L[j] < L[index]:
                index = j
        swap(L, i, index)


# Sort both lists
selection_sort(list1)
selection_sort(list2)

for i in range(len(list1)):
    total_distance += abs(list1[i] - list2[i])  # calculate total distance

print(f"The total distance is: {total_distance}")

# Part 2
# Count how many times an element a from list 1 appears in list 2, how many elements b are equal to element a
# Searching algorithm, sequential search
for a in list1:
    temp_count = 0  # count how many a's are in b, then reset it after moving to the next a element
    for b in list2:
        if a == b:
            print(f"Match! {a} is equal to {b} increase temp count by one")
            temp_count += 1
    # calculate similarity score of element a after traversing through all list2
    similarity_score += a * temp_count

print(f"The similarity score is: {similarity_score}")
