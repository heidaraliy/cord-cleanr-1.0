import tkinter as tk
from tkinter import messagebox
import discord

#define client import from discord
client = discord.Client()

#define geometry of applet window
root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=400, bg="#7289DA")
canvas.pack()

frame = tk.Frame(root, bg="#ffffff")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#declaring entry box and greeting
tid_greeting = tk.Label(frame, text="Enter your Discord Token ID:", font=('Times New Roman',14,'bold'), bg="#ffffff")
token_entry = tk.Entry(frame, width=20, borderwidth=2, show='*')

#app structure
tid_greeting.pack(side='top', pady=10)
token_entry.pack(side='top', pady=10)

#1st if-statement to take user token input, user should enter token id here
def validate_token_id():

    msg = ''
    token = token_entry.get()
    tk.StringVar = token_entry.get

    if len(token) == 0:

        msg = 'Token ID cannot be empty.'
        messagebox.showinfo('Error', msg)


    else:

        try:

            if any(ch.isalpha() for ch in token):

                msg = 'Token ID cannot contain letters.'
                messagebox.showinfo('Error', msg)

            elif len(token) > 20:

                msg = 'Token ID is too long.'
                messagebox.showinfo('Error', msg)

            elif len(token) < 5:

                msg = 'Token ID is too short.'
                messagebox.showinfo('Error', msg)

            else:

                tid_validated = tk.Label(frame,
                                         text="Token ID Status: Validated",
                                         font=('Times New Roman', 10, 'bold'),
                                         bg="#ffffff")

                tid_validated.pack(side='top', pady=10)

                whitelist_greeting.pack(side='top', pady=10)
                whitelist_input.pack(side='top', pady= 10)
                btn2.pack(side='top', pady=10)

                btn3.pack(side='top', pady=10)

                btn4.pack(side='top', pady=10)

                token_entry.destroy()
                btn1.destroy()
                tid_greeting.destroy()

                tid_value = tk.Label(frame, textvariable=token_entry.get())

                tid_value.pack(side='top', pady=10)

        except Exception as e:

            msg = 'Error.'
            messagebox.showinfo('Error', msg)


@client.event
async def mass_leave():

    token = token_entry.get()

    for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)

    client.run(token, bot=False)

btn1 = tk.Button(frame, text = 'Submit', command=validate_token_id)
btn1.pack(side='top', pady=10)


#client id entry
tid_input = tk.Entry(frame, width=20, borderwidth=2)
tid_greeting = tk.Label(frame, text="Enter your Discord Token ID first.", font=('Times New Roman',14,'bold'), bg="#ffffff")
whitelist_greeting = tk.Label(frame, text="Enter whitelisted servers, separated by commas.", font=('Times New Roman',11,'bold'), bg="#ffffff")
whitelist_input = tk.Text(frame, width=20, height=1, borderwidth=2)
whitelist = whitelist_input.get

#button row cont.
btn2 = tk.Button(frame, text ='Mass Leave Servers')
btn3 = tk.Button(frame, text ='Clear Chat Logs')
btn4 = tk.Button(frame, text ='Clear Friend Requests')


root.resizable(False, False)
root.mainloop()

