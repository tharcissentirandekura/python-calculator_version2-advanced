#I import my library and I gonna use it for my calculator 
# I also keep track of the the calculations made so that if the user choose to quit the program
# it will show him/her the previously made calculation!
import my_library

count = 0
total_calculations = []
print("Welcme to my calculator to do some mathematic operations")

my_library.helpMenu()
select_menu = my_library.getUserInput("l")

while select_menu != 'e' and select_menu != 'E':
    answers = my_library.try_calculation(select_menu)
    
    count += 1
    total_calculations.append(str(count) + '  ' + ":" + str(answers))
    
    my_library.helpMenu()
    select_menu = my_library.getUserInput('l')


if count > 0:
    print("To recap, your calculations were:", total_calculations)
else:
    print("Thanks for trusting our calculator!🤝")
    print("Program exiting...")
