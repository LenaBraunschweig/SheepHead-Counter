import tkinter as tk

# main window
root = tk.Tk()
wid_width = 700
wid_height = 300
root.geometry(f"{wid_width}x{wid_height}")

#authentification frame
frame_auth = tk.Frame(root, width=wid_width, height=wid_height)
frame_auth.place(relx=0.5, rely=0.5, anchor="center")
frame_auth.pack_propagate(False)
tk.Label(frame_auth, text="Authentication Screen", font=("Arial", 16)).pack()

#start up frame
frame_start = tk.Frame(root, width=wid_width, height=wid_height)
frame_start.place(relx=0.5, rely=0.5, anchor="center")
frame_start.pack_propagate(False)

lbl_username = tk.Label(frame_start, text="Player's Name:")
lbl_username.pack()
ent_username = tk.Entry(frame_start, bd=3)
ent_username.pack(pady=5)

#username
username = 'yolo'

#game button
def test_my_button():
  user_entry = ent_username.get()
  if (user_entry == username):
    frame_auth.tkraise()

btn_login = tk.Button(frame_start, text='Login', command=test_my_button)
btn_login.pack(pady=5)

frame_start.tkraise()
root.mainloop()