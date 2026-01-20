##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x100")

#authentification frame
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

#login frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack()

#username and password
username = 'yolo'
password = 'yolo'

#login button
def test_my_button():
  user_entry = ent_username.get()
  user_pass = ent_password.get()
  if (user_entry == username and user_pass == password):
    frame_auth.tkraise()

btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack(pady=5)

#screen methods
root.mainloop()