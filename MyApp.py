import tkinter as tk
from tkinter import messagebox, scrolledtext

class PCTroubleshooterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PC Repair Expert System")
        self.root.geometry("600x500")

        # Define rules as a dictionary of symptoms, actions, and references
        self.rules = {
            1: {
                "symptom": "PC won't turn on",
                "action": [
                    "Check if the power cable is connected properly.",
                    "Ensure the power outlet is working.",
                    "Replace the power supply unit (PSU).",
                    "Inspect the motherboard for damage."
                ],
                "references": [
                    "https://www.youtube.com/watch?v=example1",
                    "https://www.howtogeek.com/pc-wont-turn-on"
                ]
            },
            2: {
                "symptom": "Blue screen error",
                "action": [
                    "Restart your PC and check for Windows updates.",
                    "Run a memory diagnostic tool to check for RAM issues.",
                    "Reinstall the operating system.",
                    "Update or roll back device drivers."
                ],
                "references": [
                    "https://www.youtube.com/watch?v=example2",
                    "https://support.microsoft.com/blue-screen"
                ]
            },
            3: {
                "symptom": "Slow performance",
                "action": [
                    "Close unnecessary programs and background processes.",
                    "Run a disk cleanup and defragmentation.",
                    "Upgrade your RAM.",
                    "Switch to an SSD for faster storage."
                ],
                "references": [
                    "https://www.youtube.com/watch?v=example3",
                    "https://www.pcmag.com/speed-up-slow-pc"
                ]
            },
            4: {
                "symptom": "No internet connection",
                "action": [
                    "Check if the Wi-Fi or Ethernet cable is connected.",
                    "Restart your router or modem.",
                    "Update your network drivers.",
                    "Reset your network settings."
                ],
                "references": [
                    "https://www.youtube.com/watch?v=example4",
                    "https://www.lifewire.com/fix-no-internet-connection"
                ]
            },
            5: {
                "symptom": "Overheating",
                "action": [
                    "Clean the dust from the fans and vents.",
                    "Replace the thermal paste on the CPU.",
                    "Ensure proper airflow in the PC case.",
                    "Replace the cooling fan."
                ],
                "references": [
                    "https://www.youtube.com/watch?v=example5",
                    "https://www.tomshardware.com/pc-overheating-fix"
                ]
            },
        }

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange widgets in the GUI.
        """
        # Title Label
        title_label = tk.Label(self.root, text="PC Repair Expert System", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Symptom Selection
        symptom_frame = tk.LabelFrame(self.root, text="Select a Symptom", padx=10, pady=10)
        symptom_frame.pack(padx=20, pady=10, fill="x")

        self.symptom_var = tk.StringVar()
        self.symptom_var.set("")  # Default value

        for rule in self.rules.values():
            symptom_radio = tk.Radiobutton(
                symptom_frame,
                text=rule["symptom"],
                variable=self.symptom_var,
                value=rule["symptom"],
                font=("Arial", 12)
            )
            symptom_radio.pack(anchor="w")

        # Diagnose Button
        diagnose_button = tk.Button(self.root, text="Diagnose", command=self.diagnose, font=("Arial", 12))
        diagnose_button.pack(pady=10)

        # Results Display
        self.results_text = scrolledtext.ScrolledText(self.root, width=70, height=15, font=("Arial", 12))
        self.results_text.pack(padx=20, pady=10)

        # How to Use Button
        how_to_use_button = tk.Button(self.root, text="How to Use This Program", command=self.show_how_to_use, font=("Arial", 12))
        how_to_use_button.pack(pady=10)

    def diagnose(self):
        """
        Diagnose the selected symptom and display results.
        """
        symptom = self.symptom_var.get()
        if not symptom:
            messagebox.showwarning("No Symptom Selected", "Please select a symptom first!")
            return

        results, references = self.get_diagnosis(symptom)
        self.display_results(results, references)

    def get_diagnosis(self, symptom):
        """
        Get diagnosis and references for the selected symptom.
        """
        results = []
        references = []
        for rule in self.rules.values():
            if symptom.lower() == rule["symptom"].lower():
                results.extend(rule["action"])
                references.extend(rule.get("references", []))
        return results, references

    def display_results(self, results, references):
        """
        Display the diagnosis results and references in the text box.
        """
        self.results_text.delete(1.0, tk.END)  # Clear previous content

        if results:
            self.results_text.insert(tk.END, "Possible solutions:\n")
            for i, action in enumerate(results, 1):
                self.results_text.insert(tk.END, f"{i}. {action}\n")
            
            if references:
                self.results_text.insert(tk.END, "\nReferences for further help:\n")
                for i, ref in enumerate(references, 1):
                    self.results_text.insert(tk.END, f"{i}. {ref}\n")
        else:
            self.results_text.insert(tk.END, "No matching issues found. Please consult a professional technician.")

    def show_how_to_use(self):
        """
        Display instructions on how to use the program.
        """
        instructions = """
--- How to Use This Program ---
1. Select a symptom from the list.
2. Click the 'Diagnose' button to get possible solutions.
3. View the results and references in the text box below.
4. Click 'How to Use This Program' for instructions.
        """
        messagebox.showinfo("How to Use This Program", instructions)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = PCTroubleshooterGUI(root)
    root.mainloop()