to_do_list=[]
def add_list():

        print('if you finish write quit')
        while True:
            x = input("enter your tasks: ")
            if x.lower()=="quit":
                break
            to_do_list.append(x)
            print()
        print(to_do_list)
def show_list():
    print("your current tasks: ")
    if not to_do_list:
        print("your list empty!")
    else:
        len(to_do_list)
        for i in range(len(to_do_list)):
            print(f"{i + 1}-{to_do_list[i]}")
def remove_list():
    if not to_do_list :
        return
    else:
        choice = input("if you want to remove any task write yes....").lower()
        if choice == "yes":
            show_list()
            try:
                index = int(input("enter the number of task you want to remove it: "))-1
                if 0 <= index < len(to_do_list):
                    to_do_list.pop(index )
                    print(f"removed done task {index+1} ")
                    show_list()
                else:
                    print("the nuber incorrect")
            except ValueError:
                print("please enter correct number")

        else:
            return

add_list()
show_list()
remove_list()
