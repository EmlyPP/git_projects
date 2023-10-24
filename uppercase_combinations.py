from tkinter import *


def print_input():
    your_word = input_word.get()
    label_your_word = Label(win, text='This is your word:' + your_word)
    label_your_word.pack()


def lower_all(x):
    """Function that changes uppercase letters to lowercase letters in the entered word"""
    if not x.islower():
        x = x.lower()
    return x


def upper_case_change():
    """A program that returns combinations of strings with letters changed to uppercase letters or digits converted
    to special characters"""
    x = str(input_word.get())

    x = lower_all(x)

    char = {'1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
            '!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
    combinations = []

    def upper_all(text):
        for case in text:
            if case in char:
                text = text.replace(case, char[case])
        return text

    for i in range(len(x)):
        for j in range(len(x)):
            ind = x.index(x[i])
            if i == 0 and j > i:
                combinations.append(str(upper_all(x[ind:j + 1].upper()) + x[
                                                                          j + 1:]))  # from first case + j-upper case + lower last case
                for k in range(1, j + 1):
                    combinations.append(str(x[:ind + k] + upper_all(x[ind + k:j + 1].upper()) + x[
                                                                                                j + 1:]))  # from k-case + j-upper case
                # print('------------')
            elif i == 0 and j == 0:
                combinations.append(str(upper_all(x[i].upper()) + x[j + 1:]))  # all upper case except last one
                # print('------------')
            else:
                pass

    def upper_even_odd(x):
        """A function that converts lowercase letters into uppercase ones, alternating between even and odd"""
        for z in range(0, 2):
            comb_even_odd = []
            word = []
            for i in range(0, len(x) + z):
                ind = i + 0
                if ind >= len(x):
                    pass
                elif i % 2 == z:
                    word.append(str(upper_all(x[ind].upper())))
                else:
                    word.append(str(x[ind]))
            comb_even_odd.append(''.join(word))
            for c in comb_even_odd:
                combinations.append(c)

    upper_even_odd(x)

    def no_combinations():
        """A function returning number of unique combinations found"""
        if len(x) > 2:
            return str(len(combinations))
        else:
            return str(len(combinations) - 2)

    # print(combinations)
    sb_combinations = Scrollbar(win)
    your_comb = Text(win, yscrollcommand=sb_combinations.set, width=50, height=10)
    your_comb.pack()
    sb_combinations.place(in_=your_comb, relx=1., rely=0, relheight=1.)
    sb_combinations.config(command=your_comb.yview)
    your_comb.insert(END, 'These are the possible combinations of your word: \n')
    for com in combinations:
        #i = 1
        your_comb.insert(END, str(com + '\n'))
    no_comb_label = Label(win, text='\nNumber of unique combinations found: ' + no_combinations())
    no_comb_label.pack()


win = Tk()
win.geometry("700x350")
win.title('Word combinations')

label_entry_word = Label(win, text="Write the word you want to change: ").pack()
input_word = StringVar()
x = str(input_word.get())
entry_word = Entry(win, textvariable=input_word).pack()
entry_btn = Button(win, text='Submit', command=print_input and upper_case_change).pack()

win.mainloop()
