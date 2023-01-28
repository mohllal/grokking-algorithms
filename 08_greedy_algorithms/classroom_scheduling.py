def classroom_scheduling(classes):
  schedule = []
  current = float("-inf")
  
  for i in range(len(classes)):
    if classes[i][0] >= current:
      schedule.append(classes[i])
      current = classes[i][1]
  
  return schedule
  
if __name__ == "__main__":
  classes = [[9, 10], [10, 11], [9.5, 10.5], [11, 12], [10.5, 11.5]]

  classes.sort(key=lambda element: element[1])
  schedule = classroom_scheduling(classes)
  
  print("schedule for classes: {}: {}".format(classes, schedule))