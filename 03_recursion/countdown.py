def countdown_descending(i):
  print(i)

  if i == 0:
    return
  else:
    countdown_descending(i - 1)

def countdown_ascending(i):
  if i == 0:
    return
  else:
    countdown_ascending(i - 1)
  
  print(i)

    
if __name__ == "__main__":
  print('countdown_descending')
  countdown_descending(10)
  
  print('countdown_ascending')
  countdown_ascending(10)
