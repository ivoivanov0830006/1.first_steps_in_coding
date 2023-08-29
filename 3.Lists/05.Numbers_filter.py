input_number = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(input_number):
    num = int(input())
    if num < 0:
        negative.append(num)
    if num >= 0:
        positive.append(num)
    if num % 2 == 0 or num == 0:
        even.append(num)
    if num % 2 != 0:
        odd.append(num)

command_line = input()
if command_line == "even":
    print(even)
elif command_line == "odd":
    print(odd)
elif command_line == "negative":
    print(negative)
elif command_line == "positive":
    print(positive)

# --------------------------- Another solution ----------------------------
#
# number_lines = int(input())
#
# COMMAND_EVEN = "even"
# COMMAND_ODD = "odd"
# COMMAND_POSITIVE = "positive"
# COMMAND_NEGATIVE = "negative"
#
# args = []
#
# for _ in range(number_lines):
#     current_number = int(input())
#     args.append(current_number)
#
# direction = input()
# filtered_numbers = []
#
# for number in args:
#     filtered_passes = (
#         (direction == COMMAND_EVEN and number % 2 == 0) or
#         (direction == COMMAND_ODD and number % 2 != 0) or
#         (direction == COMMAND_NEGATIVE and number < 0) or
#         (direction == COMMAND_POSITIVE and number >= 0)
#     )
#     if filtered_passes:
#         filtered_numbers.append(number)
#
# print(filtered_numbers)
#
