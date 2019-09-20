from hwr.app.model import ONNETpred, Model
from hwr.app.views import *
import tkinter as tk


# Overall layout
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        self.title('On-line hadnwriting recognition')
        self.geometry('{}x{}'.format(1024, 768))

        model = Model(ONNETpred)
        text_area = PredictedTextView(self, text="Text", width=50, height=40, padx=3, pady=3)
        pred_area = CorrectionsView(self, text="Correction", width=450, height=50, pady=3)
        draw_area = WritingPadView(self, text="Writing area", width=450, height=200, padx=3, pady=3)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        text_area.grid(row=0, sticky="nsew")
        pred_area.grid(row=1, sticky="ew")
        draw_area.grid(row=2, sticky="ew")

        text_area.grid_rowconfigure(0, weight=1)
        text_area.grid_columnconfigure(0, weight=1)
        pred_area.grid_rowconfigure(0, weight=1)
        draw_area.grid_columnconfigure(0, weight=1)
        draw_area.grid_rowconfigure(0, weight=1)

    def run(self):
        self.mainloop()


def main():
    App().run()


if __name__ == "__main__":
    main()
