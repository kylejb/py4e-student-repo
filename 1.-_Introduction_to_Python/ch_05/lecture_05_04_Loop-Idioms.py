## Chapter 05 | Coursera Lecture
#  Copied code from lecture to attempt answering the following question before lecture reveals answer
## QUESTION:
#    How to find the smallest value?


smallest_so_far = None
print("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num <= smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print("After", smallest_so_far)

