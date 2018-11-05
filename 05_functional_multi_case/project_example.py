def pick_job(player1):
  # print out all choices for player to see
  jobs = ['dog trainer: food 100, 02, 100', 'teacher: food 150, 02: 75']
  for j in jobs:
      print(j)

  # get user input for job & save in a variable
  job = input('what job do you want t/d: \n')
  # if/else to assign points based on choice
  if job == 'd':
      player1 = [100,100,100,0]
  elif job == 't':
      player1 = [100,150,75,0]
  else:
      print('nope')
  # return new values
  print('your stats are as follows\n health at', player1[0], '\n time at', player1[-1])
  return player1


def launch(player1):
    launch = False
    l_status = input('the weather is bad. Launch or wait\n type launch or wait: ')

    if l_status == 'wait':
        print('you waited 3 days for a clear launch')
        player1[-1] = 3
        print('it was an easy ride up. Your health is now', player1[0], 'and your time is now', player1[-1], 'days')
        return player1
    elif l_status == 'launch':
        player1[-1] = 1
        player1[0] = player1[0] - 25
        print('it was a rough ride up. Your health is now', player1[0])
        return player1

# main
mars_landing = False

while mars_landing == False:
    # [health, food, 02, time]
    peter = pick_job([100,0,0,0])
    launch_time = launch(peter)
    break
