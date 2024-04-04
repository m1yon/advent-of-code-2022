with open('input.txt') as f:
  calorieCounts = []
  currentCalorieCount = 0

  for line in f:
    if line == "\n":
      calorieCounts.append(currentCalorieCount)
      currentCalorieCount = 0
    else:
      currentCalorieCount += int(line)

  topThree = (0, 0, 0)

  for count in calorieCounts:
    if (count > topThree[2]):
      topThree = topThree[1], topThree[2], count
    elif (count > topThree[1]):
      topThree = topThree[1], count, topThree[2]
    elif (count > topThree[0]):
      topThree = count, topThree[1], topThree[2]
  
  print(sum(topThree))