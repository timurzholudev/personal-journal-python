import string
import os


class Main:

    file_name = 'journal-log.txt'

    def init(self):
        print('Welcome to Personal Journal!')
        self.__run_app()

    def __run_app(self):
        self.__interface(11)

    def __interface(self, options_count):
        print(f'Currently selected file is {Main.file_name}')
        print('1) Select journal')
        print('2) Create new journal')
        print('3) Show all journal logs')
        print('4) Add new log to journal')
        print('5) Add new log to journal at certain position')
        print('6) Rewrite log at certain position')
        print('7) Delete log at certain position')
        print('8) Remove all whitespaces')
        print('Enter "exit" to stop app')
        user_input = ''
        user_input = input('Select Option:')
        if user_input.isdigit() and int(user_input) <= options_count:
            self.__user_input(int(user_input))
        elif user_input != 'exit':
            self.__run_app()
        else:
            print('Thank you for using app')

    def __user_input(self, val):
        if val == 0:
            self.__ui_select_journal()
        elif val == 1:
            self.__ui_create_new_journal()
        elif val == 2:
            self.__ui_show_all_logs()
        elif val == 3:
            self.__ui_add_new_log()
        elif val == 4:
            self.__ui_add_new_log_to_position()
        elif val == 5:
            self.__ui_rewrite_log()
        elif val == 6:
            self.__ui_delete_log()
        elif val == 7:
            self.__ui_remove_whitespaces()
        elif val == 8:
            self.__ui_to_lower()
        elif val == 9:
            self.__ui_to_upper()
        else:
            self.__ui_to_first_cap()

        self.__run_app()

    def __ui_select_journal(self):
        print('Please eneter name of journal with .txt extension')
        user_input = input('Enter journal name: ')
        file_check = self.__check_if_file_exist(user_input)
        if not file_check[1]:
            print('Sorry, journal not found')
        else:
            Main.file_name = file_check[0]

    def __ui_create_new_journal(self):
        print('Please name your journal')
        user_input = input('Enter journal name: ')
        file_check = self.__check_if_file_exist(user_input)
        Main.file_name = file_check[0]
        if file_check[1]:
            print('Journal with such name already exist\'s')
        else:
            print('Journal successfully created')
            self.__create_file()

    def __ui_show_all_logs(self):
        print('Log start >>>>>>>>>>>>>>')
        self.__read_lines()
        print('<<<<<<<<<<<<<<<< Log end')

    def __ui_add_new_log(self):
        print(f'Add new log to {Main.file_name}')
        content = input('Enter new log: ')
        if len(content) > 0:
            self.__add_new_line(content)

    def __ui_add_new_log_to_position(self):
        print(f'Add new log to {Main.file_name}')
        postion = input('Enter position for log (number only): ')
        if postion.isdigit():
            content = input('Enter new log: ')
            if len(content) > 0:
                self.__add_new_line_at_postion(int(postion), content)

    def __ui_rewrite_log(self):
        print(f'Change log in {Main.file_name}')
        postion = input('Enter position of log (number only): ')
        if postion.isdigit():
            content = input('Enter new content: ')
            if len(content) > 0:
                self.__rewrite_line(int(postion), content)

    def __ui_delete_log(self):
        print(f'Delete log in {Main.file_name}')
        postion = input('Enter position of log (number only): ')
        if postion.isdigit():
            self.__delete_line(int(postion))

    def __ui_remove_whitespaces(self):
        self.__format_file()

    def __ui_to_lower(self):
        self.__transform_to_lower_case()

    def __ui_to_upper(self):
        self.__transform_to_upper_case()

    def __ui_to_first_cap(self):
        self.__transform_first_cap()

    # File Manipulation

    def __create_file(self):
        with open(Main.file_name, 'w+') as my_file:
            my_file.write('')

    def __read_lines(self):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.readlines()
            for idx, line in enumerate(lines):
                print("%d) %s" % (idx+1, line))

    def __add_new_line(self, content):
        with open(Main.file_name, 'a+') as my_file:
            my_file.write(f'{content} \r')

    def __add_new_line_at_postion(self, position, content):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.readlines()
        if len(lines) >= position:
            lines[position-1] = f'{content}\r'
            with open(Main.file_name, 'w') as my_file:
                my_file.writelines(lines)
        else:
            print('Exception: line not found')

    def __rewrite_line(self, position, content):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.readlines()

        if len(lines) >= position:
            lines[position-1] = f"{content} \r"
            with open(Main.file_name, 'w') as my_file:
                my_file.writelines(lines)
        else:
            print('Sorry position not found')

    def __delete_line(self, position):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.readlines()

        if len(lines) >= position:
            lines[position-1] = ""
            with open(Main.file_name, 'w') as my_file:
                my_file.writelines(lines)
        else:
            print('Sorry position not found')

    def __format_file(self):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.readlines()
        with open(Main.file_name, 'w') as my_file:
            for line in lines:
                if line.strip():
                    my_file.write(line)

    def __transform_to_lower_case(self):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.read().lower()
        with open(Main.file_name, 'w') as my_file:
            my_file.write(lines)

    def __transform_to_upper_case(self):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.read().upper()
        with open(Main.file_name, 'w') as my_file:
            my_file.write(lines)

    def __transform_first_cap(self):
        with open(Main.file_name, 'r') as my_file:
            lines = my_file.readlines()
        with open(Main.file_name, 'w') as my_file:
            for line in lines:
                line = line.replace(line[0], line[0].upper())
                # print(line[0].upper())
                my_file.write(line)

    def __check_if_file_exist(self, value):
        if value.find('.txt') < 0:
            value += '.txt'
        new_str = f'{value}'
        exists = os.path.isfile(new_str)
        return [value, exists]


main = Main()
main.init()
