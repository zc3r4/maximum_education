import tkinter
import customtkinter
import os
import json

with open('users.json', 'r') as j:
    text_into_to_json = j.read()
    list_with_users = json.loads(text_into_to_json)

def on_close():
     os._exit(0)

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

autorization = customtkinter.CTk()
autorization.title('My App')
au_width_resolution = autorization.winfo_screenwidth()
au_height_resolution = autorization.winfo_screenheight()
autorization.geometry(f'400x300+{au_width_resolution // 2 - 200}+{au_height_resolution // 2 - 150}')

def register_in_program():
     global reg_password_1_entry, reg_password_2_entry, reg_login_entry, register_window, reg_button, registration_sucsessful, reg_email_entry
     autorization.destroy()
     register_window = customtkinter.CTk()
     register_window.title('My App | Registration')
     reg_width_resolution = register_window.winfo_screenwidth()
     reg_height_resolution = register_window.winfo_screenheight()
     register_window.geometry(f'500x300+{reg_width_resolution // 2 - 250}+{reg_height_resolution // 2 - 150}')

     reg_label = customtkinter.CTkLabel(master=register_window, text='Регистрация', bg_color='transparent', font=('Arial', 16))
     reg_label.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

     reg_login_entry = customtkinter.CTkEntry(master=register_window, placeholder_text='Логин')
     reg_login_entry.place(relx=0.5, rely=0.32, y=5, anchor=tkinter.CENTER)
     reg_password_1_entry = customtkinter.CTkEntry(master=register_window, placeholder_text='Пароль')
     reg_password_1_entry.place(relx=0.5, rely=0.42, y=10, anchor=tkinter.CENTER)
     reg_password_2_entry = customtkinter.CTkEntry(master=register_window, placeholder_text='Повторите пароль')
     reg_password_2_entry.place(relx=0.5, rely=0.52, y=15, anchor=tkinter.CENTER)

     reg_button = customtkinter.CTkButton(master=register_window, text='Зарегистрироваться', command=registration_confirm)
     reg_button.place(relx=0.5, rely=0.62, y=20, anchor=tkinter.CENTER)

     registration_sucsessful = customtkinter.CTkLabel(master=register_window,
     text='', bg_color='transparent', font=('Arial', 16))
     registration_sucsessful.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

     register_window.resizable(False, False)
     register_window.protocol('WM_DELETE_WINDOW', on_close)
     register_window.mainloop()

def registration_confirm():
     global reg_password_1_entry, reg_password_2_entry, reg_login_entry, register_window, reg_button, registration_sucsessful
     
     registration_sucsessful.destroy()

     if len(reg_password_1_entry.get()) < 6 and len(reg_password_2_entry.get()) < 6:
          registration_sucsessful = customtkinter.CTkLabel(master=register_window,
          text='Пароль должен содержать не менее 6 символов',
          bg_color='transparent', font=('Arial', 16))
          registration_sucsessful.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
     
     elif reg_password_1_entry.get() != reg_password_2_entry.get():
          registration_sucsessful = customtkinter.CTkLabel(master=register_window,
          text='Пароли не совпадают',
          bg_color='transparent', font=('Arial', 16))
          registration_sucsessful.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

     elif len(reg_login_entry.get()) < 6:
          registration_sucsessful = customtkinter.CTkLabel(master=register_window,
          text='Логин должен содержать не менее 6 символов',
          bg_color='transparent', font=('Arial', 16))
          registration_sucsessful.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
     
     elif len(reg_login_entry.get()) >= 6:
          pass

     elif len(reg_password_1_entry.get()) >= 6 and len(reg_password_2_entry.get()) >= 6:
          pass

     elif reg_password_1_entry.get() == reg_password_2_entry.get():
          pass
     
     elif (reg_login_entry.get() == '' or reg_password_1_entry.get() == '' and reg_password_2_entry.get() == '') or (reg_login_entry.get() == '' and reg_password_1_entry.get() == '' and reg_password_2_entry.get() == ''):
          registration_sucsessful = customtkinter.CTkLabel(master=register_window,
          text='Заполните все поля',
          bg_color='transparent', font=('Arial', 16))
          registration_sucsessful.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

     if reg_password_1_entry.get() == reg_password_2_entry.get() and len(reg_password_1_entry.get()) >= 6 and len(reg_password_2_entry.get()) >= 6 and len(reg_login_entry.get()) >= 6:
          registration_sucsessful = customtkinter.CTkLabel(master=register_window,
          text='Вы успешно зарегистрировались!\nПерезайдите в программу!',
          bg_color='transparent', font=('Arial', 16))
          registration_sucsessful.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
          reg_button.destroy()

          # Запись в файл
          new_user_write_in_dict = {'login': reg_login_entry.get(), 
          'password': reg_password_1_entry.get()} # {login: password}
          list_with_users.append(new_user_write_in_dict)
          with open('users.json', 'w') as j:
               text_to_write_register_users = json.dumps(list_with_users)
               j.write(text_to_write_register_users)

def main_menu_program():
     main_menu = customtkinter.CTk()
     main_menu.title('My App')
     width_resolution = main_menu.winfo_screenwidth()
     height_resolution = main_menu.winfo_screenheight()
     main_menu.geometry(f'800x500+{width_resolution // 2 - 400}+{height_resolution // 2 - 250}')
     main_menu.resizable(False, False)

     label = customtkinter.CTkLabel(master=main_menu, text='Prog Name', bg_color='transparent', font=('Arial', 16))
     label.place(relx=0.01, rely=0.001)
     main_menu.protocol('WM_DELETE_WINDOW', on_close)
     main_menu.mainloop()

def login_in_program():
     for user_dict in list_with_users:
          if user_dict['login'] == login_entry.get():
               if user_dict['password'] == password_entry.get():
                    autorization.destroy()
                    return main_menu_program()
          elif user_dict['login'] != login_entry.get() or user_dict['password'] != password_entry.get():
               wrong_autorization = customtkinter.CTkLabel(master=autorization, text='Неверный логин или пароль',
               bg_color='transparent', font=('Arial', 16))
               wrong_autorization.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)


welcome_label = customtkinter.CTkLabel(master=autorization, text='Здравствуйте', bg_color='transparent', font=('Arial', 16))
welcome_label.place(relx=0.5, rely=0.22, anchor=tkinter.CENTER)

login_entry = customtkinter.CTkEntry(master=autorization, placeholder_text='Логин')
login_entry.place(relx=0.5, rely=0.32, y=5, anchor=tkinter.CENTER)

password_entry = customtkinter.CTkEntry(master=autorization, placeholder_text='Пароль')
password_entry.place(relx=0.5, rely=0.42, y=10, anchor=tkinter.CENTER)

login_entry_button = customtkinter.CTkButton(master=autorization, text='Войти', command=login_in_program)
login_entry_button.place(relx=0.5, rely=0.52, y=15, anchor=tkinter.CENTER)

register_button = customtkinter.CTkButton(master=autorization, text='Регистрация', command=register_in_program)
register_button.place(relx=0.5, rely=0.62, y=20, anchor=tkinter.CENTER)

autorization.protocol('WM_DELETE_WINDOW', on_close)
autorization.mainloop()