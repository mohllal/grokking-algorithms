def largest_square(width, height):
  minimum = min(width, height)
  maximum = max(width, height)
  
  if maximum % minimum == 0:
    return minimum
  
  return largest_square(minimum, maximum - minimum)

if __name__ == "__main__":
  print('largest square of 1680 width and 640 height =', largest_square(1680, 640))
  print('largest square of 2800 width and 210 height =', largest_square(2800, 210))
