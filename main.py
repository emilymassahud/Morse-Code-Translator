from tkinter import *

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..', ' ': '/'
}


def button_clicked():
    text = text_entry.get()
    word_list = list(text.upper())
    morse_message = []
    for letter in word_list:
        try:
            new_charact = morse_dict[letter]
        except KeyError:
            pass
        else:
            morse_message.append(new_charact)
    morse_text = ' '.join(morse_message)
    morse_label = Label(text="The translated message is: ")
    morse_label.grid(column=0, row=3, sticky=N+S+W+E)
    morse_entry = Entry(width=50)
    morse_entry.grid(column=0, row=4)
    morse_entry.insert(0, morse_text)


window = Tk()
window.title('Morse Code Translator')
window.config(padx=20, pady=20)

l1 = Label(text='Please write your message to be translated to Morse code: ')
l1.grid(row=0, column=0)
text_entry = Entry(width=60)
text_entry.grid(row=1, column=0, padx=10, pady=10)
button1 = Button(text='Translate', command=button_clicked)
button1.grid(row=1, column=1)

window.mainloop()
