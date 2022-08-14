# ------------------------------- #
# Title: Assignment06
# Dev: RSar
# Desc: Module0a - Read file, Display data
# ChangeLog: (date,name,change)
#            2022/08/13, RSar, Created module to complete Assignment06
# ------------------------------- #


# Data ----------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
row_dic = {}  # A row of data separated into elements of a dictionary
# {Task,Priority}
list_of_rows = []  # List of dictionary rows
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


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
            task, priority = line.split(",")
            row_dic = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row_dic)

        file.close()
        print("\n\tfile_name = " + file_name)  # temp_debugging
        return list_of_rows


# Presentation (Input/Output)  ----------------------------------- #
class IO:

    # noinspection PyDecorator
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


# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str,
                              list_of_rows=table_lst)  # Read file

# Step 2 - Display a menu of choices to the user


# Step 3 Show current data
IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show \
# current data in the list/table
IO.output_menu_tasks()  # Shows menu
choice_str = IO.input_menu_choice()  # Get menu option

# Step 4 - Process user's menu choice
