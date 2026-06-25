import customtkinter as ctk

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
