def taks():
    tasks = []
    print('-------- Welcome to the Task Management app ----------')

    total_task = int(input('Enter how many task you want to add : '))
    for i in range(1, total_task + 1):
        task_name = input(f'Enter the task {i} : ')
        tasks.append(task_name)


    print(f"Today's Task are\n {tasks}")

    while True:
        operation = int(input('Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/'))
        if operation == 1:
            add =  input('Enter task you want to add : ')
            tasks.append(add)
            print(f'Task {add} has been successfully Added ........ !')

        elif operation == 2:
            updated_value = input('Enter the task name you want to update : ')
            if updated_value in tasks:
                up = input('Enter new task : ')
                ind = tasks.index(updated_value)
                tasks[ind] = up
                print(f'Updated task {up}')


        elif operation == 3:
            delete_value = input('Which Taks you want to delete : ')
            if delete_value in tasks:
                ind = tasks.index(delete_value)
                del tasks[ind]
                print(f'Task {delete_value} has been deleted !')


        elif operation == 4:
            print(f'Total tasks = {tasks}')

        elif operation == 5:
            print('Closing the program !')
            break

        else:
            print('Invalid Inputs ....... ')

taks()