width = int(input())
length = int(input())

count_pieces = width * length

input_line = input()
no_more_pieces = False

while input_line != "STOP":
    pieces = int(input_line)

    count_pieces -= pieces
    if count_pieces <= 0:
        no_more_pieces = True
        break

    input_line = input()

if no_more_pieces:
    print(f"No more cake left! You need {abs(count_pieces)} pieces more.")
else:
    print(f"{count_pieces} pieces are left.")
