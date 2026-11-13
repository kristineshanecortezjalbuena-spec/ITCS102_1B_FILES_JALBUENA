box = 7
for x in range(box):
  for y in range(box):
    if x == box - 1 or x == 0 or y == box - 1 or y == 0:
      print("*", end=" ")
    else:
      print(" ", end=" ")  
  print()
