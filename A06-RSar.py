# ------------------------------- #
# Title: Assignment06
# Dev: RSar
# Desc: Working with functions in a class,
#       When the program starts, load each "row" of data
#       in "ToDoToDoList.txt" into a python Dictionary.
#       Add each dictionary "row" to a python list "table"
# ChangeLog: (date,name,change)
#            2022/01/01, RRoot, Created starter script
#            2022/08/13, RSar, Modified code to complete Assignment06
#            2022/08/14, RSar, Assembled code from modules
#            2022/08/16, RSar, Removed 'shadow global variable' error, Comment out debug
#            code.
# ------------------------------- #


# Data ----------------------------------------------------------- #
# Declare variables and constants
strProgramTitle = "To Do List XP v2.0"  # Program name
file_name_str = "ToDoFile.txt"  # The name of the data file
# file_obj = None  # An object that represents a file
# row_dic = {}  # A row of data separated into elements of a dictionary
# {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
# list_of_rows = []  # List of dictionary rows


# Processing  ---------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")

        for line in file:
            t, p = line.split(",")
            row_dic = {"Task": t.strip(), "Priority": p.strip()}
            list_of_rows.append(row_dic)

        file.close()

        # # debug
        # print("\n\t\\\\file_name = " + file_name)
        # # /debug

        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        # # debug
        # print("\t\\\\Processor.add_data_to_list(task) = " + task +
        #       "\n\t\\\\Processor.add_data_to_list(priority) = " + priority)
        # # /debug

        row_dic = {"Task": str(task).strip(),
                   "Priority": str(priority).strip()}
        # TODO: Add Code Here!
        list_of_rows.append(row_dic)

        # # debug
        # print("\n\t\\\\Processor.add_data_to_list(list_of_rows) = " +
        #       str(list_of_rows))
        # # /debug

        print("\n\tAdded task (priority): '" + task + " (" + priority + ")'")
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        for row_dic in list_of_rows:  # Remove task
            if row_dic["Task"].lower() == task.lower():
                list_of_rows.remove(row_dic)

                # # debug
                # print("\t\\\\Processor.remove_data_from_list(task) = " +
                #       task.lower())
                # # /debug

                print("\n\tRemoved task (priority): '" + row_dic["Task"] +
                      " (" + row_dic["Priority"] + ")'")

        # # debug
        # print("\n\t\\\\Processor.remove_data_from_list(list_of_rows) = " +
        #       str(list_of_rows))
        # # /debug

        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        file_obj = open(file_name, "w")
        for row_dic in list_of_rows:
            file_obj.write(str(row_dic["Task"]) + "," +
                           str(row_dic["Priority"]) + "\n")
        file_obj.close()

        # # debug
        # print("\n\t\\\\Processor.write_data_to_file(list_of_rows)" +
        #       str(list_of_rows))
        # # /debug

        print("\n\tSaved data to file: " + file_name)
        return list_of_rows


# Presentation (Input/Output)  ----------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print("""
\tMenu of Options
\t1) Add a new Task
\t2) Remove an existing Task
\t3) Save Data to File        
\t4) Exit Program
    """)

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to "
                           "perform? [1 to 4] - ")).strip()

        # # debug
        # print("\n\t\\\\IO.input_menu_choice(choice) = " + choice)
        # # /debug

        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n\t******* The current tasks To Do are: *******")
        for row in list_of_rows:
            print("\t" + row["Task"] + " (" + row["Priority"] + ")")
        print("\t*******************************************")

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (task, priority) with task and priority
        """
        task = str(input("\nWhat is the task? - "))
        priority = str(input("What is the priority? - "))

        # # debug
        # print("\n\t\\\\IO.input_new_task_and_priority(task) = " + task +
        #       "\n\t\\\\IO.input_new_task_and_priority(priority) = " +
        #       priority)
        # # /debug

        return task, priority  # TODO: Add Code Here!

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        task = str(input("\nTask to remove?: ")).strip()

        # # debug
        # print("\n\t\\\\IO.input_task_to_remove(task) = " + task)
        # # /debug

        return task


# Main Body of Script  ------------------------------------------- #
print("\nWelcome to " + strProgramTitle + "!"  # Display program name
      "\n\n\tOpened file: '" + file_name_str + "'")

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str,
                              list_of_rows=table_lst)  # Read file data

# Step 2 - Display a menu of choices to the user
while True:

    # # debug
    # print("\n\t\\\\start Menu loop "
    #       "\n\t\\\\Call: \tIO.output_current_tasks_in_list()")
    # # /debug

    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show \
    # current data in the list/table

    # # debug
    # print("\n\t\\\\Call: \tIO.output_menu_tasks()")
    # # /debug

    IO.output_menu_tasks()  # Shows menu

    # # debug
    # print("\t\\\\Global (choice_str) = " + choice_str +
    #       "\n\t\\\\Call: \tIO.input_menu_choice()")
    # # /debug

    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task

        # # debug
        # print("\t\\\\Global (choice_str) = " + choice_str +
        #       "\n\n\t\\\\Global (table_lst) = " + str(table_lst) +
        #       "\n\t\\\\Call: \tIO.input_new_task_and_priority()")
        # # /debug

        _task, _priority = IO.input_new_task_and_priority()

        # # debug
        # print("\t\\\\Call: \tProcessor.add_data_to_list()")
        # # /debug

        table_lst = Processor.add_data_to_list(task=_task,
                                               priority=_priority,
                                               list_of_rows=table_lst)

        # # debug
        #       "\n\n\t\\\\Global (table_lst) = " + str(table_lst))
        # # /debug

        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task

        # # debug
        # print("\t\\\\Global (choice_str) = " + choice_str +
        #       "\n\n\t\\\\Global (table_lst) = " + str(table_lst) +
        #       "\n\n\t\\\\Call: \tIO.input_task_to_remove()")
        # # /debug

        _task = IO.input_task_to_remove()

        # # debug
        # print("\t\\\\Call: \tProcessor.remove_data_from_list()")
        # # /debug

        table_lst = Processor.remove_data_from_list(task=_task,
                                                    list_of_rows=table_lst)

        # # debug
        #       "\n\n\t\\\\Global (table_lst) = " + str(table_lst))
        # # /debug

        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File

        # # debug
        # print("\n\t\\\\Global (choice_str) = " + choice_str +
        #       "\n\n\t\\\\Global (table_lst) = " + str(table_lst) +
        #       "\n\n\t\\\\Call: \tProcessor.write_data_to_file()")
        # # /debug

        table_lst = Processor.write_data_to_file(file_name=file_name_str,
                                                 list_of_rows=table_lst)

        # # debug
        # print("\n\t\\\\Global (table_lst) = " + str(table_lst))
        # # /debug

        continue  # to show the menu

    elif choice_str == '4':  # Exit Program

        # # debug
        # print("\t\\\\Global (choice_str) = " + choice_str)
        # # /debug

        print("\n\tByeeee!")
        input("\n[Press ENTER key to quit.]")
        break  # exit Menu loop
