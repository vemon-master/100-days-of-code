row1 =["N", "N", "N"]
row2 =["N", "N", "N"]
row3 =["N", "N", "N"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where you want to put the treasure")
#linus=position
column=int(position[1])
row=int(position[0])

selected_row = map[column - 1]
selected_row[row - 1]= "X"

print(f"{row1}\n{row2}\n{row3}")