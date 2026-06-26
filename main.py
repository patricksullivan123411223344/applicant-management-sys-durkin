import customtkinter as ctk

def open_window(parent: "App"):
    if parent is None:
        return

    parent.withdraw()

    child = ctk.CTkToplevel(parent)
    child.title("Process Application")
    child.geometry("600x400")

    def on_close():
        child.destroy()
        parent.deiconify()

    child.protocol("WM_DELETE_WINDOW", on_close)
    parent.wait_window(child)

# Set global design properties
ctk.set_appearance_mode("Dark")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Options: "blue", "green", "dark-blue"

class StatusFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Title section 
        self.grid_columnconfigure(0, weight=1)
        self.title_label = ctk.CTkLabel(self, text="Applications Status", font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # Total number of completed applications on the system
        self.total_processed_applications = ctk.CTkLabel(self, text="Total Processed Application #:", font=("Arial", 14))
        self.total_processed_applications.grid(row=1, column=0, padx=10, pady=10)

        # List of all applications that need to be processed on our end
        self.unprocessed_applications = ctk.CTkLabel(self, text="Applications Awaiting Processing:", font=("Arial", 14))
        self.unprocessed_applications.grid(row=2, column=0, padx=10, pady=10)

        # List of all applications that incomplete from the applicants end
        self.incomplete_applications = ctk.CTkLabel(self, text="Incomplete Applications:", font=("Arial", 14))
        self.incomplete_applications.grid(row=3, column=0, padx=10, pady=10)

        # Process application button to dashboard
        self.process_application_btn = ctk.CTkButton(
            self,
            text="Process Application",
            font=("Arial", 14),
            command=lambda: open_window(self.winfo_toplevel()),
        )
        self.process_application_btn.grid(row=4, column=0, padx=10, pady=10)

class JobsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Title section
        self.grid_columnconfigure(0, weight=1)
        self.title_label = ctk.CTkLabel(self, text="Jobs Status", font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)

        # Current jobs mid-execution
        self.current_jobs = ctk.CTkLabel(self, text="Current Jobs:", font=("Arial", 14))
        self.current_jobs.grid(row=1, column=0, padx=10, pady=10)

        # Immediate next job
        self.up_next = ctk.CTkLabel(self, text="Up next:", font=("Arial", 14))
        self.up_next.grid(row=2, column=0, padx=10, pady=10)

        # Current Job Queue
        self.queued_jobs = ctk.CTkLabel(self, text="Queued Job List:", font=("Arial", 14))
        self.queued_jobs.grid(row=3, column=0, padx=10, pady=10)

        # Button to jump to the jobs dashboard
        self.to_dash_btn = ctk.CTkButton(self, text="Manage jobs", command=None)
        self.to_dash_btn.grid(row=4, column=0, padx=10, pady=5)

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