# ------------------------------- #
# Title: Assignment06
# Dev: RSar
# Desc: Module00 - Menu and Exit program
# ChangeLog: (date,name,change)
#            2022/08/13, RSar, Created module to complete Assignment06
# ------------------------------- #


# Data ----------------------------------------------------------- #
# Declare variables and constants
choice_str = ""  # Captures the user option selection


# Processing  ---------------------------------------------------- #


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
        return choice


# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.

# Step 2 - Display a menu of choices to the user
while True:

    # Step 3 Show current data
    print("""
\tstart Menu loop 
\t# Show current data in the list/table")
\tCall 1: \t\tIO.output_current_tasks_in_list()""")  # temp_debugging

    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        print("""
\tUser selected: \tOption 1 - 'Add a new task' 
\tCall 1: \t\tinput_new_task_and_priority
\tCall 2: \t\tadd_data_to_list""")  # temp_debugging
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        print("""
\tUser selected: \tOption 2 - 'Remove an existing task' 
\tCall 1: \t\tinput_task_to_remove
\tCall 2: \t\tremove_data_from_list""")  # temp_debugging
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        print("""
\tUser selected: \tOption 3 - 'Save Data to File' 
\tCall 1: \t\tinput_task_to_remove
\tCall 2: \t\twrite_data_to_file""")  # temp_debugging
        print("\n\tData Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("\n\tUser selected: Option 4 - 'Exit program'")
        # temp_debugging
        print("\n\tGoodbye!")
        input("\n[Press ENTER key to quit.]")
        break  # by exiting loop
