import tkinter as tk
import tkinter.font as f
from tkinter import messagebox
from Solver import Solver, Solver_Exception
from Numbers import Binary_Exception, Hexadecimal_Exception, Decimal_Exception


class MainApp(tk.Frame):
    string = "There are four modes that you can choose from.\n" \
             "Binary: Perform operations with Binary Numbers\n" \
             "Hexadecimal: Perform operations with Hexadecimal Numbers\n" \
             "Decimal (Normal Base 10 Numbers): Perform Operations with Decimal Numbers\n" \
             "Conversion: Convert numbers from on of the three previous types to another\n" \
             "The Buttons at the bottom can be used to add, subtract, multiply, or divide " \
             "(Except in Conversion Mode)\n" \
             "The Top Text Box is where you enter your question and the Bottom box will display your answer\n" \
             "Note: Please use \"*\" for multiplication and \"/\" for division"

    options = ["Binary",
               "Decimal",
               "Hexadecimal"]

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.binary, self.hexadecimal, self.decimal, self.conversion, self.help = False, False, False, False, True
        self.add, self.sub, self.mul, self.div = None, None, None, None
        self.t1, self.t2 = None, None
        self._ex = None
        self._cur_mode = None
        self.menu1, self.menu2, self.drop1, self.drop2 = None, None, None, None
        self.choice1, self.choice2 = tk.StringVar(), tk.StringVar()
        self.draw()

    def _set_B(self):
        self.binary, self.hexadecimal, self.decimal, self.conversion, self.help = True, False, False, False, False
        self.t1.delete('1.0', tk.END)
        self.t2.config(state="normal")
        self.t2.delete('1.0', tk.END)
        self.t2.config(state="disabled")
        self._cur_mode.config(text="Current Mode: Binary")
        self.drop1.config(state='disabled')
        self.drop2.config(state='disabled')

    def _set_H(self):
        self.binary, self.hexadecimal, self.decimal, self.conversion, self.help = False, True, False, False, False
        self.t1.delete('1.0', tk.END)
        self.t2.config(state="normal")
        self.t2.delete('1.0', tk.END)
        self.t2.config(state="disabled")
        self._cur_mode.config(text="Current Mode: Hexadecimal")
        self.drop1.config(state='disabled')
        self.drop2.config(state='disabled')

    def _set_D(self):
        self.binary, self.hexadecimal, self.decimal, self.conversion, self.help = False, False, True, False, False
        self.t1.delete('1.0', tk.END)
        self.t2.config(state="normal")
        self.t2.delete('1.0', tk.END)
        self.t2.config(state="disabled")
        self._cur_mode.config(text="Current Mode: Decimal")
        self.drop1.config(state='disabled')
        self.drop2.config(state='disabled')

    def _set_C(self):
        self.binary, self.hexadecimal, self.decimal, self.conversion, self.help = False, False, False, True, False
        self.t1.delete('1.0', tk.END)
        self.t2.config(state="normal")
        self.t2.delete('1.0', tk.END)
        self.t2.config(state="disabled")
        self._cur_mode.config(text="Current Mode: Conversion")
        self.drop1.config(state='active')
        self.drop2.config(state='active')

    def _help(self):
        self.help = True
        messagebox.showinfo(title="Help", message=MainApp.string)
        self.help = False

    def _addition(self):
        self.t1.insert(tk.END, "+")

    def _subtraction(self):
        self.t1.insert(tk.END, "-")

    def _multiplication(self):
        self.t1.insert(tk.END, "*")

    def _division(self):
        self.t1.insert(tk.END, "/")

    def execute(self):
        c_mode = self._cur_mode.cget("text")[14:]
        s = Solver(c_mode)
        input_s = self.t1.get("1.0", tk.END)
        if len(input_s) > 0:
            while input_s[-1] == "\n":
                input_s = input_s[:-1]
                if input_s == "":
                    break
        if c_mode == "Conversion":
            orig, to = self.menu1.get(), self.menu2.get()
            if orig == "From..." or to == "To...":
                tk.messagebox.showerror("Type Not specified", "You did not specify a type for the conversion.\n"
                                                              "Please select one")
            else:
                if input_s != "":
                    try:
                        answer = s.solve(input_s, orig, to)
                        self.t2.config(state="normal")
                        self.t2.delete('1.0', tk.END)
                        self.t2.insert(tk.END, answer)
                        self.t2.config(state="disabled")
                    except Exception as e:
                        if type(e) == Binary_Exception:
                            tk.messagebox.showerror("Binary Exception", str(e))
                        elif type(e) == Hexadecimal_Exception:
                            tk.messagebox.showerror("Hexadecimal Exception", str(e))
                        elif type(e) == Decimal_Exception:
                            tk.messagebox.showerror("Decimal Exception", str(e))
                else:
                    tk.messagebox.showerror("No Input", "No Input was detected")
        else:
            if input_s != "":
                try:
                    answer = s.solve(input_s)
                    self.t2.config(state="normal")
                    self.t2.delete('1.0', tk.END)
                    self.t2.insert(tk.END, answer)
                    self.t2.config(state="disabled")
                except Exception as e:
                    if type(e) == Binary_Exception:
                        tk.messagebox.showerror("Binary Exception", str(e))
                    elif type(e) == Hexadecimal_Exception:
                        tk.messagebox.showerror("Hexadecimal Exception", str(e))
                    elif type(e) == Decimal_Exception:
                        tk.messagebox.showerror("Decimal Exception", str(e))
                    else:
                        tk.messagebox.showerror("Solver Error", str(e))
            else:
                tk.messagebox.showerror("No Input", "No Input was detected")

    def draw(self):
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='Mode')
        menu_file.add_command(label="Binary", command=self._set_B)
        menu_file.add_command(label="Hexadecimal", command=self._set_H)
        menu_file.add_command(label="Decimal", command=self._set_D)
        menu_file.add_command(label="Conversion", command=self._set_C)
        menu_file.add_command(label="Help", command=self._help)

        self.add = tk.Button(text="Addition", command=self._addition)
        self.sub = tk.Button(text="Subtraction", command=self._subtraction)
        self.mul = tk.Button(text="Multiplication", command=self._multiplication)
        self.div = tk.Button(text="Division", command=self._division)
        self.add.place(x=0, y=380, height=100, width=180)
        self.sub.place(x=180, y=380, height=100, width=180)
        self.mul.place(x=360, y=380, height=100, width=180)
        self.div.place(x=540, y=380, height=100, width=180)

        self._ex = tk.Button(text="Execute", command=self.execute)
        self._ex.place(x=310, y=170, height=40, width=100)
        self._ex['font'] = f.Font(size=15)

        self.t1 = tk.Text(master=self.root, height=10, width=480)
        self.t1.place(x='0', y='0')

        self.t2 = tk.Text(master=self.root, height=10, width=480)
        self.t2.place(x='0', y='215')
        self.t2.configure(state='disabled')

        self._cur_mode = tk.Label(self.root, text="Current Mode: Decimal")
        self._cur_mode.place(x=20, y=175)
        self._cur_mode['font'] = f.Font(size=13)

        self.menu1 = tk.StringVar()
        self.menu1.set("From...")

        self.menu2 = tk.StringVar()
        self.menu2.set("To...")

        self.drop1 = tk.OptionMenu(self.root, self.menu1, *MainApp.options)
        self.drop1.place(x=475, y=175)
        self.drop2 = tk.OptionMenu(self.root, self.menu2, *MainApp.options)
        self.drop2.place(x=600, y=175)
        self.drop1.config(state='disabled')
        self.drop2.config(state='disabled')


if __name__ == "__main__":
    main = tk.Tk()
    main.title("Calculator")
    main.geometry("720x480")
    main.minsize(720, 480)
    main.maxsize(720, 480)
    main.option_add('*tearOff', False)
    MainApp(main)
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    main.mainloop()
