name_of_book = input()

input_line = input()
count = 0
isFound = False

while input_line != "No More Books":

    if input_line == name_of_book:
        isFound = True
        break

    count += 1
    input_line = input()

if isFound:
    print(f"You checked {count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {count} books.")