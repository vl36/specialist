import home_task_1_1
import home_task_1_2
import home_task_1_3
import home_task_1_4


def main():
    current_task = input("Choose home_task: ")
    if current_task == "1":
        home_task_1_1.task_1_1()
    if current_task == "2":
        home_task_1_2.task_1_2()
    if current_task == "3":
        home_task_1_3.task_1_3()
    if current_task == "4":
        home_task_1_4.task_1_4()
    else:
        print("Exit")
        exit()


if __name__ == '__main__':
    main()
