import pandas as pd
import shutil
import os


# Creating a class that will hold the info from the users in the form of a dictionary:
class InfoUsers(object):
    def __init__(self, dict_info_users_class):
        self.dict_info_users_class = dict_info_users_class


print("In this program we will work with a csv file. We will first need that you insert the name of "
      "your csv file, then the path where it is located, and then copy this file to a location of your "
      "choice. Lastly, we will print the initials of the row information in the first column of your "
      "file, and then the first 3 characters of the row information in the second column.")
_ = input("Ready? Press any key to continue: ")

user_input_csv_file = input("Please insert the name of your csv file, including the extension: ")
print("\n \nTip: If you are using Windows, your path will probably be something like this:"
      "\n \t C:\\Users\\YourUserName\\YourPath1\\YourPath2\\YourPathETC\\yourcsvfile.csv"
      "\n \nIf you are on Linux or Mac, your path will probably be something like this:"
      "\n \t /home/YourUserName/YourPath1/YourPath2/YourPathETC/yourcsvfile.csv")
print()
user_input_initial_path = input("Now insert the current path to your csv file: ")
user_input_new_path = input("Lastly, insert the path to where you would like this file to be "
                            "copied: ")

with open(user_input_initial_path) as csv_file:  # Opening the user's chosen csv file
    shutil.copy(user_input_initial_path, user_input_new_path)  # Copying this file to a new location

# Creating a new location by joining the path the csv file was copied to with the name of the csv file:
new_location = os.path.join(user_input_new_path, user_input_csv_file)

dict_info_users = {}
list_rows = []
# Opening the file from the new location:
with open(user_input_initial_path, 'r') as csv_file_2:
    csv_reader = pd.read_csv(csv_file_2)
    count_key_new_dict = 0
    count_value_new_dict = 0
    for index, row in csv_reader.iterrows():
        list_rows.append(row)
    while len(dict_info_users.values()) <= len(list_rows):
        if count_value_new_dict >= len(list_rows):
            break
        count_key_new_dict += 1
        dict_info_users["Dictionary key number {}".format(count_key_new_dict)] = list_rows[count_value_new_dict]
        count_value_new_dict += 1
        info_users_1 = InfoUsers(dict_info_users)

print()
print("-" * 80)
print()

# Printing all the information from the csv file:
print(f"Ok, here is all the information we've found in your csv file:"
      f"\n {info_users_1.dict_info_users_class}")
print("IMPORTANT! If, for some reason, you wouldn't like to display your users' complete information, "
      "feel free to delete or comment the above line of code (the print statement on lines 56 and 57).")

print()
print("-" * 80)
print()

print("And here are the initials from the information in the first column and the first 3 characters "
      "of the information located in the second column: ")

# Printing some information from the first 2 columns of the created object:
for key, value in info_users_1.dict_info_users_class.items():
    # From the first column we will print the first character from each word in the string:
    list_first_column = value[0].split(sep=" ")
    new_dict = {}
    new_list = []
    for complete_info in list_first_column:
        new_list.append(complete_info[0])
    print('.'.join(new_list).upper())
    # From the second column we will print the first 3 characters in the string:
    new_info_sec_row = value[1][:3]
    for char in value[1][3:]:
        replacing_numbers = ""
        if char.isalnum():
            char = "*"
            new_info_sec_row += char
        else:
            new_info_sec_row += char
    print(new_info_sec_row)