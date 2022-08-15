# ------------------------------- #
# Title: Assignment06
# Dev: RSar
# Desc: Module03 - Write data to file
# ChangeLog: (date,name,change)
#            2022/08/13, RSar, Created module to complete Assignment
#            2022/08/14, RSar, Prepared module for submission
# ------------------------------- #


# Data ----------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary \
# {Task,Priority}
table_lst = [{'Task': 'write_test_task1', 'Priority': 'p1'},
             {'Task': 'write_test_task2', 'Priority': 'p2'},
             {'Task': 'write_test_task3', 'Priority': 'p3'},
             {'Task': 'write_test_task4', 'Priority': 'p4'}]  # A \
# list that acts as a 'table' of rows - pre-populated values for \
# temp_debugging


# Processing  ---------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

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
        print("\n\tlist_of_rows = " + str(list_of_rows))  # temp_debugging
        print("\n\tSaved to file: " + file_name)
        return list_of_rows

# Presentation (Input/Output)  ----------------------------------- #


# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.


# Step 2 - Display a menu of choices to the user


# Step 3 Show current data


# Step 4 - Process user's menu choice
print("\n\tUser selected: \tOption 3 - 'Save Data to File'"
      "\n\tCall 1: \t\tProcessor.write_data_to_file()")  # temp_debugging

table_lst = Processor.write_data_to_file(file_name=
                                         file_name_str,
                                         list_of_rows=table_lst)
