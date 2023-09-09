import tkinter as tk
import random

# Create the main application window
window = tk.Tk()
window.title('Password Generator')
window.geometry('600x400+500+20')

# Function to handle button click to generate a password
def button_clicked():
    # Get the desired password length from the entry widget
    length_of_letters = int(entry_pass_len.get())
    length_of_special = int(entry_pass_len.get())
    length_of_numbers= int(entry_pass_len.get())
    # Define the characters to generate the password from
    generate_from = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Generate a random password
    password = []
    for char in range(1, length_of_letters + 1):
        password += random.choice(generate_from)

    for char in range(1, length_of_special + 1):
        password += random.choice(special_char)
    
    for char in range(1, length_of_numbers + 1):
        password += random.choice(numbers)
    

    # Shuffle the password to make it random
    random.shuffle(password)

    # Create the final generated password from the shuffled characters
    password_generated = ''.join(password)

    # Display the generated password in the label
    entry_the_pass['text'] = password_generated

# Create and place the widgets in the application window
label = tk.Label(master=window, text='PASSWORD GENERATOR',font ="bold, 15", fg='#212F3C')
label.pack()

user_name = tk.Label(window, text='Enter User Name:')
user_name.place(relx=0.1, rely=0.1)

entry_user_name = tk.Entry(window)
entry_user_name.place(relx=0.4, rely=0.1, relwidth=0.5)

length_of_password = tk.Label(window, text='How many Alphabets:')
length_of_password.place(relx=0.1, rely=0.2)

entry_pass_len = tk.Entry(window)
entry_pass_len.place(relx=0.4, rely=0.2, relwidth=0.5)

length_of_special = tk.Label(window, text = "How many special charectors:")
length_of_special.place(relx = 0.1, rely = 0.3)

entry_pass_special = tk.Entry(window)
entry_pass_special.place(relx =0.4, rely = 0.3, relwidth=0.5)

length_of_numbers = tk.Label(window, text = "How many numbers:")
length_of_numbers.place(relx=0.1, rely = 0.4)

entry_pass_num = tk.Entry(window)
entry_pass_num.place(relx = 0.4, rely = 0.4, relwidth=0.5)

generate = tk.Label(window, text='Generate Password:')
generate.place(relx=0.1, rely=0.5)

entry_the_pass = tk.Label(window, bg='white', fg='black')
entry_the_pass.place(relx=0.4, rely=0.5, relwidth=0.5)

button = tk.Button(window, text='Generate Password', bg='#229954', command=button_clicked)
button.place(relx=0.4, rely=0.6)


window.mainloop()