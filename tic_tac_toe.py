from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()

titlelabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 30), bg="blue", fg="white")
titlelabel.pack()

frame2 = Frame(root)
frame2.pack()

turn = "x"

buttons = [[None for _ in range(3)] for _ in range(3)]  # 3x3 grid


def check_winner():
    """Checks if there is a winner and displays a message box."""
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] and buttons[i][0]["text"] != "":
            messagebox.showinfo("Game Over", f"{buttons[i][0]['text']} won!")
            reset_game()
            return
        # Check columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] and buttons[0][i]["text"] != "":
            messagebox.showinfo("Game Over", f"{buttons[0][i]['text']} won!")
            reset_game()
            return

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] and buttons[0][0]["text"] != "":
        messagebox.showinfo("Game Over", f"{buttons[0][0]['text']} won!")
        reset_game()
        return
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] and buttons[0][2]["text"] != "":
        messagebox.showinfo("Game Over", f"{buttons[0][2]['text']} won!")
        reset_game()
        return

    # Check for draw
    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_game()


def reset_game():
    """Resets the board for a new game."""
    global turn
    turn = "x"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""


def play(event):
    """Handles button clicks and updates the game board."""
    global turn
    button = event.widget
    if button["text"] == "":
        button["text"] = turn
        check_winner()
        turn = "0" if turn == "x" else "x"


# Creating buttons for the Tic Tac Toe board
for i in range(3):
    for j in range(3):
        button = Button(frame2, text="", width=4, height=2, font=("Algerian", 25), bg="black", fg="lime",relief=RAISED, borderwidth=5)
        button.grid(row=i, column=j)
        button.bind("<Button>", play)
        buttons[i][j] = button  # Store the button in the 2D list

root.mainloop()
