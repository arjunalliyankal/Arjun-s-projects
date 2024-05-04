import tkinter as tk
import scrape_clean
class TextAreaFrame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Area Frame")

        self.text_area = tk.Text(self.window, height=2, width=50)
        self.text_area.pack(pady=10)

        self.button = tk.Button(self.window, text="Analyse", command=self.call_function)
        self.button.pack(pady=10)

        self.window.mainloop()

    def call_function(self):
      
        text = self.text_area.get(1.0, tk.END)
        scrape_clean.main(text)
        

if __name__ == "__main__":
    app = TextAreaFrame()