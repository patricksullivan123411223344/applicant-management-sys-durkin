import customtkinter as ctk

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