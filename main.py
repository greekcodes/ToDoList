import os
# let user input the task they want, the date and time they want to do it
# user should be able to edit or delete task
# algorithm - 

#Great Job! I would use this
#how about marking a task complete? oh never mind that is option 2, you may want to change the wording to Mark a task complete
def menu():
  print("Welcome to your Todo List!")
  print("Enter 1 to create a new task.")
  print("Enter 2 to complete a task.")
  print("Enter 3 to view all tasks.")
  print("Enter 4 clear all tasks!")
  print("Enter 5 to exit out of the program. ")
  while True:
    try:
      user_choice = int(input("Your choice: ").strip())
      if user_choice not in [1, 2, 3, 4, 5]:
        raise ValueError
    except ValueError:
      print("Please enter a valid interger. 1, 2, 3, 4, or 5")
      continue
    else:
      os.system("clear")
      return user_choice
  

file_name = "incomplete_tasks"
with open(f"{file_name}.txt", "a+") as fobj:
  pass
  

# f2 = open("completed.txt", "w")
def time():
  print("Format - 0:00")



def tasks():
  # f = open("tasks.txt", 'w')
  all_tasks = []
  amount_tasks = int(input("How many tasks do you want to complete?"))
  return all_tasks, amount_tasks


def get_info(all_tasks, amount_tasks):
  all_tasks = []
  amount_tasks = int(input("How many tasks do you want to complete?"))
  
  for i in range (0, amount_tasks):
    task_time = input("Time you want task done: ")
    task = input("What task do you want to do?")
      
    all_tasks.append(task_time,task)
    print(all_tasks)

  return task_time, all_tasks, amount_tasks

def complete_task():
  
  
  pass


def run(all_tasks, amount_tasks):
  while True:
    user_choice = menu()
    if user_choice == 1:
      tasks()
      get_info(all_tasks, amount_tasks)
    elif user_choice == 2:
      pass
    elif user_choice == 3:
      pass
    elif user_choice == 4:
     pass 
    elif user_choice == 5:
      quit
  
  
  
    
menu()


run(all_tasks, amount_tasks)


  