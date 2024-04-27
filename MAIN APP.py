import tkinter as tk
from tkinter import messagebox, ttk
import time
from PIL import Image, ImageTk

print(Image.__version__)  # This will print the version of Pillow


class AnalysisProgressPanel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Analysis Progress")
        self.geometry("400x200")
        self.progress_var = tk.DoubleVar()

        self.progress_label = tk.Label(self, text="Analysis Progress", font=("Gotham", 14))
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate", variable=self.progress_var)
        self.progress_bar.pack(pady=10)

        self.progress_var.set(0)  # Initial progress value

        self.lit_progress_frame = tk.Frame(self, width=300, height=20, bg="white", relief=tk.SOLID, bd=1)
        self.lit_progress_frame.pack(pady=10)

        self.lit_progress_bar = tk.Label(self.lit_progress_frame, bg="blue", width=0, height=20)
        self.lit_progress_bar.pack(side=tk.LEFT)

    def update_literal_progress(self, progress):
        self.lit_progress_bar.config(width=int(progress * 3))

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Something Fishy")
        self.geometry("1920x1080")
        self.configure(bg="#FFFFFF")  # Set default background color

        self.style = ttk.Style()
        self.style.configure('Large.TButton', font=('Gotham', 16))  # Configure a larger font for buttons

        self.mode = tk.StringVar(value="Light")  # Default mode is Light
        self.language = tk.StringVar(value="English")  # Default language is English

        self.create_main_panel()

    def create_main_panel(self):
        # Title
        self.title_label = tk.Label(self, text="Something Fishy", font=("Gotham", 36, "bold"), bg="#FFFFFF")
        self.title_label.place(relx=0.05, rely=0.1, anchor=tk.W)  # Align to left side
        self.title_label.config(anchor=tk.W)  # Set anchor to left

        # Separator line
        separator_frame = tk.Frame(self, width=1920, height=2, bg="black")  # Adjust width to 1920 pixels
        separator_frame.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Create frame for buttons in the first row
        top_frame = tk.Frame(self)
        top_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-70)

        # Load camera clipart image
        camera_img = Image.open("C:/Users/Gaming Francisco/Downloads/lens.png")  # Replace "camera.png" with the path to your camera clipart image
        camera_img = camera_img.resize((100, 100))
        camera_icon = ImageTk.PhotoImage(camera_img)

        # Camera button with clipart image
        self.camera_btn = tk.Button(top_frame, image=camera_icon, command=self.open_camera, width=100, height=100, bg="#FFFFFF", bd=0)
        self.camera_btn.image = camera_icon  # Keep a reference to the image to avoid garbage collection
        self.camera_btn.pack(side=tk.LEFT, padx=20)

        # Space between Camera and Analyze buttons
        space1_frame = tk.Frame(top_frame, width=20, height=40, bg="#FFFFFF")
        space1_frame.pack(side=tk.LEFT)

        # Load analyze button image
        analyze_img = Image.open("C:/Users/Gaming Francisco/Downloads/Analysis.png")  # Replace "path_to_analyze_image.png" with the path to your analyze button image
        analyze_img = analyze_img.resize((100, 100))  # Resize the image if needed
        analyze_icon = ImageTk.PhotoImage(analyze_img)

        # Analyze button with image
        self.analyze_btn = tk.Button(top_frame, image=analyze_icon, command=self.run_analyze, bg="#FFFFFF", bd=0)
        self.analyze_btn.image = analyze_icon  # Keep a reference to the image to avoid garbage collection
        self.analyze_btn.pack(side=tk.LEFT, padx=20)

        # Space between Analyze and History buttons
        space2_frame = tk.Frame(top_frame, width=20, height=40, bg="#FFFFFF")
        space2_frame.pack(side=tk.LEFT)

        # History button
        self.history_btn = tk.Button(top_frame, text="History", command=self.open_history, font=("Gotham", 16), width=20, height=4, bg="#FFFFFF", fg="#000000")
        self.history_btn.pack(side=tk.LEFT, padx=20)

        # Spacer between rows
        spacer_frame = tk.Frame(self, height=40, bg="#FFFFFF")
        spacer_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=0)

        # Create frame for buttons in the second row
        bottom_frame = tk.Frame(self)
        bottom_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=70)

        # About button
        self.about_btn = tk.Button(bottom_frame, text="About", command=self.open_about, font=("Gotham", 16), width=20, height=4, bg="#FFFFFF", fg="#000000")
        self.about_btn.pack(side=tk.LEFT, padx=20)

        # Space between About and Settings buttons
        space3_frame = tk.Frame(bottom_frame, width=20, height=40, bg="#FFFFFF")
        space3_frame.pack(side=tk.LEFT)

        # Settings button
        self.settings_btn = tk.Button(bottom_frame, text="Settings", command=self.open_settings_panel, font=("Gotham", 16), width=20, height=4, bg="#FFFFFF", fg="#000000")
        self.settings_btn.pack(side=tk.LEFT, padx=20)

    def open_camera(self):
        # Placeholder for opening camera panel
        pass

    def run_analyze(self):
        progress_panel = AnalysisProgressPanel(self)

        for i in range(101):
            progress_panel.progress_var.set(i)  # Update progress bar
            progress_panel.update_literal_progress(i)  # Update literal progress bar
            progress_panel.update_idletasks()   # Update the GUI
            time.sleep(0.05)                    # Simulate analysis process time

        # Close the progress panel after analysis
        progress_panel.destroy()

        # Display analysis result on the main panel
        messagebox.showinfo("Analysis Result", "Fish is Fresh!")  # Placeholder message

    def open_history(self):
        # Placeholder for opening history panel
        pass

    def open_about(self):
        # Placeholder for opening about panel
        pass

    def open_settings_panel(self):
        settings_panel = tk.Toplevel(self)
        settings_panel.title("Settings Panel")
        settings_panel.geometry("400x200")

        # Mode Settings
        mode_frame = tk.Frame(settings_panel)
        mode_frame.pack(pady=10)
        mode_label = tk.Label(mode_frame, text="Mode Settings")
        mode_label.pack()

        light_mode_radio = tk.Radiobutton(mode_frame, text="Light Mode", variable=self.mode, value="Light")
        light_mode_radio.pack(side=tk.LEFT)
        dark_mode_radio = tk.Radiobutton(mode_frame, text="Dark Mode", variable=self.mode, value="Dark")
        dark_mode_radio.pack(side=tk.LEFT)

        # Language Settings
        language_frame = tk.Frame(settings_panel)
        language_frame.pack(pady=10)
        language_label = tk.Label(language_frame, text="Language Settings")
        language_label.pack()

        english_radio = tk.Radiobutton(language_frame, text="English", variable=self.language, value="English")
        english_radio.pack(side=tk.LEFT)
        english_radio.bind("<Button-1>", lambda event: self.translate_interface())

        filipino_radio = tk.Radiobutton(language_frame, text="Filipino", variable=self.language, value="Filipino")
        filipino_radio.pack(side=tk.LEFT)
        filipino_radio.bind("<Button-1>", lambda event: self.translate_interface())

        # Apply Button
        apply_btn = tk.Button(settings_panel, text="Apply", command=lambda: [self.translate_interface(), self.apply_settings(settings_panel)])
        apply_btn.pack(pady=10)

    def apply_settings(self, settings_panel):
        if self.mode.get() == "Dark":
            self.configure(bg="#212121")  # Change main background color to dark
            self.title_label.configure(bg="#212121", fg="#FFFFFF")  # Change title background and text color
            self.camera_btn.configure(bg="#2F2F2F", fg="#FFFFFF")  # Change camera button background and text color
            self.analyze_btn.configure(bg="#2F2F2F", fg="#FFFFFF")  # Change analyze button background and text color
            self.history_btn.configure(bg="#2F2F2F", fg="#FFFFFF")  # Change history button background and text color
            self.about_btn.configure(bg="#2F2F2F", fg="#FFFFFF")  # Change about button background and text color
            self.settings_btn.configure(bg="#2F2F2F", fg="#FFFFFF")  # Change settings button background and text color            self.separator_frame.configure(bg="#FFFFFF", fg="#000000")  # Change separator line color back to default

        else:
            self.configure(bg="#FFFFFF")  # Change main background color back to light
            self.title_label.configure(bg="#FFFFFF", fg="#000000")  # Change title background and text color
            self.camera_btn.configure(bg="#FFFFFF", fg="#000000")  # Change camera button background and text color
            self.analyze_btn.configure(bg="#FFFFFF", fg="#000000")  # Change analyze button background and text color
            self.history_btn.configure(bg="#FFFFFF", fg="#000000")  # Change history button background and text color
            self.about_btn.configure(bg="#FFFFFF", fg="#000000")  # Change about button background and text color
            self.settings_btn.configure(bg="#FFFFFF", fg="#000000")  # Change settings button background and text color

        settings_panel.destroy()  # Close settings panel after applying changes

    def translate_interface(self):
        language = self.language.get()
        if language == "Filipino":
            self.camera_btn["text"] = "Kamera"
            self.analyze_btn["text"] = "Mag-analyze"
            self.history_btn["text"] = "Kasaysayan"
            self.about_btn["text"] = "Tungkol"
            self.settings_btn["text"] = "Mga Setting"
        else:
            self.camera_btn["text"] = "Camera"
            self.analyze_btn["text"] = "Analyze"
            self.history_btn["text"] = "History"
            self.about_btn["text"] = "About"
            self.settings_btn["text"] = "Settings"

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
