# ------------------------------- #
# Title: Assignment06
# Dev: RSar
# Desc: Module02 - Remove data
# ChangeLog: (date,name,change)
#            2022/08/13, RSar, Created module to complete Assignment
# ------------------------------- #


# Data ----------------------------------------------------------- #
# Declare variables and constants
row_dic = {}  # A row of data separated into elements of a dictionary
list_of_rows = []  # List of dictionary rows
table_lst = [{'Task': 'task1', 'Priority': 'p1'},
                {'Task': 'task2', 'Priority': 'p2'},
                {'Task': 'task3', 'Priority': 'p3'},
                {'Task': 'task4', 'Priority': 'p4'}]  # A list that \
# acts as a 'table' of rows {Task,Priority} - pre-populated values \
# for temp_debugging


# Processing  ---------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

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
                print("\n\t'" + row_dic["Task"] +
                      " (" + row_dic["Priority"] + ")' has been removed.")
                list_of_rows.remove(row_dic)
        print("\n\tlist_of_rows = " + str(list_of_rows))
        # temp_debugging
        print("\n\ttable_lst = " + str(table_lst))  # temp_debugging
        return list_of_rows


# Presentation (Input/Output)  ----------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        task = str(input("\nWhich task to remove?: ")).strip()
        return task

# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.


# Step 2 - Display a menu of choices to the user


# Step 3 Show current data


# Step 4 - Process user's menu choice
print("\n\tUser selected: \tOption 2 - 'Remove an existing task'")
# temp_debugging

while True:  # temp_debugging
    print("\n\tlist_of_rows = " + str(list_of_rows))  # temp_debugging
    print("\n\ttable_lst = " + str(table_lst))  # temp_debugging
    print("\n\tCall 1: \t\tIO.input_task_to_remove()")
    # temp_debugging
    task = IO.input_task_to_remove()

    print("\n\tCall 2: \t\tProcessor.remove_data_from_list()")
    # temp_debugging
    table_lst = Processor.remove_data_from_list(task=task,
                                                list_of_rows=
                                                table_lst)
    print("\n\t\\end Option 2 loop.")