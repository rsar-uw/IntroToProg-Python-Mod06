# ------------------------------- #
# Title: Assignment06
# Dev: RSar
# Desc: Module01 - Add data
# ChangeLog: (date,name,change)
#            2022/08/13, RSar, Created module to complete Assignment06
# ------------------------------- #


# Data ----------------------------------------------------------- #
# Declare variables and constants
row_dic = {}  # A row of data separated into elements of a dictionary \
# {Task,Priority}
list_of_rows = []  # List of dictionary rows
table_lst = []  # A list that acts as a 'table' of rows


# Processing  ---------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    # noinspection PyDecorator
    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row_dic = {"Task": str(task).strip(),
                   "Priority": str(priority).strip()}
        # TODO: Add Code Here!
        list_of_rows.append(row_dic)
        print("\n\tAdded task: '" + task + " (" + priority + ")'")
        print("\n\tProcessor.add_data_to_list(list_of_rows) = " +
              str(list_of_rows))  # temp_debugging
        return list_of_rows


# Presentation (Input/Output)  ----------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    # noinspection PyDecorator
    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (task, priority) with task and priority
        """
        task = str(input("\nWhat is the task? - "))
        priority = str(input("What is the priority? - "))
        print("\n\tIO.input_new_task_and_priority(task) = " + task)  # \
        # temp_debugging
        print("\tIO.input_new_task_and_priority(priority) = " +
              priority)  # temp_debugging
        return task, priority  # TODO: Add Code Here!


# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.


# Step 2 - Display a menu of choices to the user


# Step 3 Show current data


# Step 4 - Process user's menu choice
# Add a new Task

print("\n\tUser selected: \tOption 1 - 'Add a new task'")
# temp_debugging

while True:  # temp_debugging
    print("\n\tCall 1: \t\tIO.input_new_task_and_priority()")
    # temp_debugging
    task, priority = IO.input_new_task_and_priority()

    print("\n\tCall 2: \t\tProcessor.add_data_to_list()")
    # temp_debugging
    table_lst = Processor.add_data_to_list(task=task,
                                           priority=priority,
                                           list_of_rows=table_lst)

    print("\n\ttable_lst = " +
          str(table_lst))  # temp_debugging
