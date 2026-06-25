import customtkinter as ctk
from job_controller import JobsFrame
from status_controller import StatusFrame

# Set global design properties
ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Options: "blue", "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Durkin Application Management System")
        self.geometry("600x350")

        # Overview panel from OverviewFrame() class
        self.overview_panel = StatusFrame(master=self, corner_radius=15, border_width=2)
        self.overview_panel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Jobs overview panel from JobsFrame()
        self.jobs_panel = JobsFrame(master=self, corner_radius=15, border_width=2)
        self.jobs_panel.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()