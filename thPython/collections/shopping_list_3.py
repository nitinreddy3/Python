
shopping_list = []

def show_help():
    print("\n Separate each item with comma.")
    print("Type DONE to quit, SHOW to show the current list, HELP to get this "
          "message.")

def show_list():
    count = 1
    for item in shopping_list:
        print("{} : {}".format(count, item))
        count += 1
