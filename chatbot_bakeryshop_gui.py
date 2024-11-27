import tkinter as tk
from tkinter import scrolledtext

# Bakery Shop Chatbot Responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    if 'menu' in user_input or 'items' in user_input:
        return "We have a variety of fresh bread, cakes, cookies, and pastries."
    elif 'hours' in user_input or 'open' in user_input:
        return "We are open from 8 AM to 8 PM every day."
    elif 'location' in user_input or 'address' in user_input:
        return "We are located at Bakery Town, Bangalore"
    elif 'order' in user_input:
        return "You can place an order by visiting our shop or calling us at (555) 123-4567."
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome! Anything else I can help with?"
    else:
        return "I'm sorry, I didn't understand that. Can you please ask something else?"

# Function to handle user input and display chatbot response
def send_message():
    user_input = user_entry.get()
    if user_input.strip():
        chat_window.insert(tk.END, "You: " + user_input + '\n')
        response = chatbot_response(user_input)
        chat_window.insert(tk.END, "Bot: " + response + '\n\n')
        user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Bakery Shop Chatbot")

# Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='normal')
chat_window.grid(column=0, row=0, padx=10, pady=10)
chat_window.config(state='normal')

# Entry box for user input
user_entry = tk.Entry(root, width=40)
user_entry.grid(column=0, row=1, padx=10, pady=10)

# Send button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(column=1, row=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
