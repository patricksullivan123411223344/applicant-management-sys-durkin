import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

class ProcessingMenu(ctk.CTkToplevel):
    def __init__(self, master, root_window):
        super().__init__(master)
        self.root_window = root_window
        self.geometry("400x200")
        self.title("Application Processing Menu")
        self.state = {
            "selected_excel_path": None
        }

        # Title section
        self.title_label = ctk.CTkLabel(self, text="Application Processing Menu", font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # Select path button section
        self.select_path_button = ctk.CTkButton(self, 
                                                text="Please select where you want to save your data", 
                                                font=("Arial", 14),
                                                command=on_click)
        
        self.select_path_button.grid(row=1, column=0, padx=10, pady=10)
        
        # Drop box section
        self.drop_label = ctk.CtkLabel(self, 
                                       text="Drop your docx here:", 
                                       font=("Arial", 14), 
                                       fg_color="lightgray",
                                       width=40,
                                       height=10)
        
        self.drop_label.grid(row=2, column=0, padx=10, pady=10)
        
        # Utility functions
        def on_click(self):
            file_path_str = filedialog.askopenfilename(
                title="Select a file",
                initialdir=Path.home() / "Desktop",
                filetypes=[("Excel Files", "*.xlsx")]
            )

            if file_path_str:
                file_path = Path(file_path_str)
                self.state["selected_excel_path"] = file_path
                self.select_path_button.configure(text=f"Filepath chosen: {file_path.name}", fg_color="lightgreen")
            else:
                self.select_path_button.configure(text="Error selecting filepath", fg_color="salmon")


        