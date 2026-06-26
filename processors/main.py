from process_student import ParseStudent
from excel_controller import dynamic_write
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path

root = TkinterDnD.Tk()
# don't instantiate DocParser without data; use factory methods when needed
state = {
    "selected_excel_path": None
}

def on_click() -> None:
    file_path_str = filedialog.askopenfilename(
        title="Select a file from your desktop",
        initialdir=Path.home() / "Desktop",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    if file_path_str:
        file_path = Path(file_path_str)
        state["selected_excel_path"] = file_path
        select_path_button.config(text=f"Filepath chosen: {file_path.name}", bg="lightgreen")
    else:
        select_path_button.config(text="Error selecting filepath", bg="salmon")

def handle_reset(event):
    event.widget.config(bg="lightgray", text="Drop your .docx file here")

def handle_drop(event):
    paths = root.tk.splitlist(event.data)
    if not paths:
        return
    dropped_path = Path(paths[0])

    destination_path = state["selected_excel_path"]
    if not destination_path:
        event.widget.config(bg="salmon", text="Drop failed. No save path selected!")
        return

    if dropped_path.suffix.lower() == ".docx":
        cleaned = ParseStudent.from_docx(dropped_path)
        dynamic_write(destination_path, cleaned)
        event.widget.config(bg="lightgreen", text="Drop successful!")
    else:
        event.widget.config(bg="salmon", text="Error occured during drop. Process failed.")

root.title("Docx Parser Drop Zone")
root.geometry("400x300")

select_path_button = tk.Button(root, text="Click to select path", bg="lightgray", command=on_click)
select_path_button.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

drop_label = tk.Label(root, text="Drop your .docx file here", bg="lightgray", width=40, height=10)
drop_label.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)  
drop_label.drop_target_register(DND_FILES)
drop_label.dnd_bind("<<Drop>>", handle_drop)
drop_label.dnd_bind("<Leave>", handle_reset)

if __name__ == "__main__":
    try:
        root.mainloop()
    except KeyboardInterrupt:
        root.destroy()