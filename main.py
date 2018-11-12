import tkinter as tk
import tkinter.messagebox as tk_mb

import SLAU.generate
import SLAU.matrix
import SLAU.iteration
import SLAU.gauss


class Window:
    def __init__(self, title, geometry):
        self.root = None
        self.title = title
        self.geometry = geometry

        self.TEXT_HEIGHT = 5
        self.TEXT_WIDTH = 28
        self.PAD_X = 2
        self.PAD_Y = 2

        self.n_input = None
        self.n_input_label = None
        self.eps_input = None
        self.eps_input_label = None
        self.x_output = None
        self.x_output_label = None
        self.gauss_output = None
        self.gauss_output_label = None
        self.iter_output = None
        self.iter_output_label = None
        self.zeidel_output = None
        self.zeidel_output_label = None
        self.reverse_output = None
        self.reverse_output_label = None

        self.b_output_label = None
        self.b_output = None
        self.gauss_check_output = None
        self.gauss_check_output_label = None
        self.iter_check_output = None
        self.iter_check_output_label = None
        self.zeidel_check_output = None
        self.zeidel_check_output_label = None
        self.reverse_check_output = None
        self.reverse_check_output_label = None

        self.iter_count_output = None
        self.iter_count_output_label = None
        self.zeidel_count_output = None
        self.zeidel_count_output_label = None

        self.system_output = None
        self.system_output_label = None

        self.button = None
        self.frame = None

        self.n_var = None
        self.eps_var = None
        self.x_var = None
        self.gauss_var = None
        self.iter_var = None
        self.zeidel_var = None
        self.b_var = None
        self.gauss_check_var = None
        self.iter_check_var = None
        self.zeidel_check_var = None
        self.iter_count_var = None
        self.zeidel_count_var = None

    def start(self):
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(self.geometry)
        self.root.resizable(width=False, height=False)

        self.init_vars()
        self.create_widgets()
        self.layout()
        self.loop()

    def init_vars(self):
        self.x_var = tk.StringVar()
        self.n_var = tk.StringVar()
        self.eps_var = tk.StringVar()
        self.gauss_var = tk.StringVar()
        self.iter_var = tk.StringVar()
        self.zeidel_var = tk.StringVar()
        self.b_var = tk.StringVar()
        self.gauss_check_var = tk.StringVar()
        self.iter_check_var = tk.StringVar()
        self.zeidel_check_var = tk.StringVar()
        self.iter_count_var = tk.StringVar()
        self.zeidel_count_var = tk.StringVar()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, height=80, width=200)
        self.frame.grid_propagate(0)

        self.n_input = tk.Entry(self.frame, textvariable=self.n_var, width=self.TEXT_WIDTH)
        self.n_input_label = tk.Label(self.frame, text="n")
        self.eps_input = tk.Entry(self.frame, textvariable=self.eps_var, width=self.TEXT_WIDTH)
        self.eps_input_label = tk.Label(self.frame, text="Точность")

        self.x_output = tk.Entry(self.root, textvariable=self.x_var, width=self.TEXT_WIDTH)
        self.x_output_label = tk.Label(self.root, text="X")
        self.gauss_output = tk.Entry(self.root, textvariable=self.gauss_var, width=self.TEXT_WIDTH)
        self.gauss_output_label = tk.Label(self.root,
                                           text="X по методу Гаусса")
        self.iter_output = tk.Entry(self.root, textvariable=self.iter_var, width=self.TEXT_WIDTH)
        self.iter_output_label = tk.Label(self.root,
                                          text="X по итерационному методу")
        self.zeidel_output = tk.Entry(self.root, textvariable=self.zeidel_var, width=self.TEXT_WIDTH)
        self.zeidel_output_label = tk.Label(self.root,
                                            text="X по методу Зейделя")
        self.reverse_output = tk.Text(self.root, height=self.TEXT_HEIGHT,
                                      width=self.TEXT_WIDTH, wrap=tk.NONE)
        self.reverse_output_label = tk.Label(self.root,
                                             text="Обратная матрица")

        self.b_output_label = tk.Label(self.root, text="B")
        self.b_output = tk.Entry(self.root, textvariable=self.b_var, width=self.TEXT_WIDTH)
        self.gauss_check_output = tk.Entry(self.root,
                                           textvariable=self.gauss_check_var, width=self.TEXT_WIDTH)
        self.gauss_check_output_label = tk.Label(self.root, text="B")
        self.iter_check_output = tk.Entry(self.root,
                                          textvariable=self.iter_check_var, width=self.TEXT_WIDTH)
        self.iter_check_output_label = tk.Label(self.root, text="B")
        self.zeidel_check_output = tk.Entry(self.root,
                                            textvariable=self.zeidel_check_var, width=self.TEXT_WIDTH)
        self.zeidel_check_output_label = tk.Label(self.root, text="B")
        self.reverse_check_output = tk.Text(self.root, height=self.TEXT_HEIGHT,
                                            width=self.TEXT_WIDTH, wrap=tk.NONE)
        self.reverse_check_output_label = tk.Label(self.root, text="A*A^-1")

        self.iter_count_output_label = tk.Label(self.root,
                                                text="Кол-во итераций")
        self.iter_count_output = tk.Entry(self.root,
                                          textvariable=self.iter_count_var, width=self.TEXT_WIDTH)
        self.zeidel_count_output_label = tk.Label(self.root,
                                                  text="Кол-во итераций")
        self.zeidel_count_output = tk.Entry(self.root,
                                            textvariable=self.zeidel_count_var, width=self.TEXT_WIDTH)

        self.system_output = tk.Text(self.root, height=self.TEXT_HEIGHT,
                                     width=self.TEXT_WIDTH, wrap=tk.NONE)
        self.system_output_label = tk.Label(self.root, text="СЛАУ")
        self.button = tk.Button(text="Вычислить", command=self.calculate)

    def layout(self):
        self.frame.grid(row=0, column=0, rowspan=2, columnspan=2)
        self.n_input_label.grid(row=0, column=0, padx=self.PAD_X,
                                pady=self.PAD_Y)
        self.n_input.grid(row=0, column=1, padx=self.PAD_X, pady=self.PAD_Y)
        self.eps_input_label.grid(row=1, column=0, padx=self.PAD_X,
                                  pady=self.PAD_Y)
        self.eps_input.grid(row=1, column=1, padx=self.PAD_X, pady=self.PAD_Y)

        self.x_output_label.grid(row=2, column=0, padx=self.PAD_X,
                                 pady=self.PAD_Y, sticky=tk.E)
        self.x_output.grid(row=2, column=1, padx=self.PAD_X, pady=self.PAD_Y, sticky=tk.W)
        self.b_output_label.grid(row=2, column=2, padx=self.PAD_X,
                                 pady=self.PAD_Y, sticky=tk.E)
        self.b_output.grid(row=2, column=3, padx=self.PAD_X, pady=self.PAD_Y, sticky=tk.W)

        self.gauss_output_label.grid(row=3, column=0, padx=self.PAD_X,
                                     pady=self.PAD_Y, sticky=tk.E)
        self.gauss_output.grid(row=3, column=1, padx=self.PAD_X,
                               pady=self.PAD_Y, sticky=tk.W)
        self.gauss_check_output_label.grid(row=3, column=2, padx=self.PAD_X,
                                           pady=self.PAD_Y, sticky=tk.E)
        self.gauss_check_output.grid(row=3, column=3, padx=self.PAD_X,
                                     pady=self.PAD_Y, sticky=tk.W)

        self.iter_output_label.grid(row=4, column=0, padx=self.PAD_X,
                                    pady=self.PAD_Y, sticky=tk.E)
        self.iter_output.grid(row=4, column=1, padx=self.PAD_X,
                              pady=self.PAD_Y, sticky=tk.W)
        self.iter_check_output_label.grid(row=4, column=2, padx=self.PAD_X,
                                          pady=self.PAD_Y, sticky=tk.E)
        self.iter_check_output.grid(row=4, column=3, padx=self.PAD_X,
                                    pady=self.PAD_Y, sticky=tk.W)
        self.iter_count_output_label.grid(row=4, column=4, padx=self.PAD_X,
                                          pady=self.PAD_Y, sticky=tk.E)
        self.iter_count_output.grid(row=4, column=5, padx=self.PAD_X,
                                    pady=self.PAD_Y, sticky=tk.W)

        self.zeidel_output_label.grid(row=5, column=0, padx=self.PAD_X,
                                      pady=self.PAD_Y, sticky=tk.E)
        self.zeidel_output.grid(row=5, column=1, padx=self.PAD_X,
                                pady=self.PAD_Y, sticky=tk.W)
        self.zeidel_check_output_label.grid(row=5, column=2, padx=self.PAD_X,
                                            pady=self.PAD_Y, sticky=tk.E)
        self.zeidel_check_output.grid(row=5, column=3, padx=self.PAD_X,
                                      pady=self.PAD_Y, sticky=tk.W)
        self.zeidel_count_output_label.grid(row=5, column=4, padx=self.PAD_X,
                                            pady=self.PAD_Y, sticky=tk.E)
        self.zeidel_count_output.grid(row=5, column=5, padx=self.PAD_X,
                                      pady=self.PAD_Y, sticky=tk.W)

        self.reverse_output_label.grid(row=6, column=0, padx=self.PAD_X,
                                       pady=self.PAD_Y, sticky=tk.E)
        self.reverse_output.grid(row=6, column=1, padx=self.PAD_X,
                                 pady=self.PAD_Y)
        self.reverse_check_output_label.grid(row=6, column=2, padx=self.PAD_X,
                                             pady=self.PAD_Y, sticky=tk.E)
        self.reverse_check_output.grid(row=6, column=3, padx=self.PAD_X,
                                       pady=self.PAD_Y)

        self.system_output_label.grid(column=4, row=0, rowspan=4, sticky=tk.E)
        self.system_output.grid(column=5, row=0, rowspan=4)

        self.button.grid(row=7, column=0)

    def loop(self):
        self.root.mainloop()


    def calculate(self):
        n = self.n_var.get().strip()
        eps = self.eps_var.get().strip()
        if len(n) == 0:
            tk_mb.showwarning("Ошибка ввода", "Введите n!", parent=self.root)
            return
        try:
            n = int(n)
            if n <= 0:
                tk_mb.showwarning("Ошибка ввода", "Введите натуральное n!",
                                  parent=self.root)
                return
        except ValueError:
            tk_mb.showwarning("Ошибка ввода", "Введите корректное n!")
            return

        if len(eps) == 0:
            tk_mb.showwarning("Ошибка ввода", "Введите точность!",
                              parent=self.root)
            return
        try:
            eps = float(eps)
            if eps <= 0:
                tk_mb.showwarning("Ошибка ввода", "Введите точность больше нуля!",
                                  parent=self.root)
                return
        except ValueError:
            tk_mb.showwarning("Ошибка ввода", "Введите корректную точностью!")
            return

        a = SLAU.generate.get_matrix(n)
        x = SLAU.generate.get_x(n)
        b = SLAU.generate.get_b(n, a, x)
        self.x_var.set(self.list_to_str(x))
        self.b_var.set(self.list_to_str(b))
        gauss = SLAU.gauss.gauss(a, b, n)
        gauss_b = SLAU.matrix.check(a, gauss, n)
        self.gauss_var.set(self.list_to_str(gauss))
        self.gauss_check_var.set(self.list_to_str(gauss_b))
        iterat, iter_count = SLAU.iteration.iteration(a, b, n, eps)
        zeidel, zeidel_count = SLAU.iteration.zeigel(a, b, n, eps)
        iter_b = SLAU.matrix.check(a, iterat, n)
        zeidel_b = SLAU.matrix.check(a, zeidel, n)
        rev = SLAU.matrix.inverse_matrix(a, n)
        rev_check = SLAU.matrix.multi_matrix(a, rev, n)
        self.iter_var.set(self.list_to_str(iterat))
        self.iter_check_var.set(self.list_to_str(iter_b))
        self.iter_count_var.set(str(iter_count))
        self.zeidel_var.set(self.list_to_str(zeidel))
        self.zeidel_check_var.set(self.list_to_str(zeidel_b))
        self.zeidel_count_var.set(str(zeidel_count))
        self.show_system(a, b, n)
        self.show_matrix(rev, n, self.reverse_output)
        self.show_matrix(rev_check, n, self.reverse_check_output)

    def show_system(self, a, b, n):
        self.system_output.delete(1.0, tk.END)
        for i in range(n):
            for j in range(n):
                self.system_output.insert(tk.END, "{:<4.0f}".format(a[i][j]))
            self.system_output.insert(tk.END, "| {:<4.0f}".format(b[i]))
            if i != n-1:
                self.system_output.insert(tk.END, "\n")

    def show_matrix(self, matrix, n, widget):
        widget.delete(1.0, tk.END)
        for i in range(n):
            for j in range(n):
                widget.insert(tk.END, "{:<4.3f} ".format(matrix[i][j]))
            if i != n-1:
                widget.insert(tk.END, "\n")

    @staticmethod
    def list_to_str(list_):
        answer = ""
        for i in range(len(list_)):
            answer += str(list_[i])
            if i != len(list_) - 1:
                answer += " "
        return answer

if __name__ == "__main__":
    window = Window("YegorR's СЛАУ", "1020x300")
    window.start()