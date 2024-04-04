with open('input.txt') as f:
  chunks = f.read().split('\n\n')
  calorieCounts = [sum(tuple(map(int, chunk.split()))) for chunk in chunks]

  topThree = (0, 0, 0)

  for count in calorieCounts:
    if (count > topThree[2]):
      topThree = topThree[1], topThree[2], count
    elif (count > topThree[1]):
      topThree = topThree[1], count, topThree[2]
    elif (count > topThree[0]):
      topThree = count, topThree[1], topThree[2]
  
  print(sum(topThree))