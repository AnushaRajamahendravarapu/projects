import tkinter as tk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    [r'how are you?', ['I am fine, thank you!', 'Doing well, how about you?']],
    [r'what is your name?', ['I am a bot created by Jayanth.', 'I don’t have a name but you can call me ChatBot.']],
    [r'bye|goodbye', ['Goodbye! Have a nice day!', 'See you later!']]
]

# Reflections for pronoun swapping
reflections = {
    "i am": "you are",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "i am",
    "you were": "i was",
    "you've": "i have",
    "you'll": "i will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to send a message and get a response
def send_message():
    user_input = user_message.get()
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot.respond(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n")
    user_message.set("")

# Create the main window
root = tk.Tk()
root.title("Python ChatBot")

# Create a chat window
chat_window = tk.Text(root, bg="white", width=50, height=8)
chat_window.grid(row=0, column=0, columnspan=2)

# Create an entry widget for user input
user_message = tk.StringVar()
message_entry = tk.Entry(root, textvariable=user_message, width=30)
message_entry.grid(row=1, column=0)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1)

# Run the application
root.mainloop()
