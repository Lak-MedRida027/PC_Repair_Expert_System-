class PCTroubleshooter:
    def __init__(self):
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

    def diagnose(self, symptom):
        """
        Diagnose the PC issue based on the provided symptom.
        """
        results = []
        references = []
        for rule in self.rules.values():
            if symptom.lower() == rule["symptom"].lower():
                results.extend(rule["action"])
                references.extend(rule.get("references", []))
        return results, references

    def get_user_input(self):
        """
        Get symptoms from the user.
        """
        print("\nHere is the list of all possible symptoms:")
        for rule in self.rules.values():
            print(f"- {rule['symptom']}")
        
        symptom = input("\nEnter the symptom of your PC issue: ").strip()
        return symptom

    def show_diagnosis(self, diagnosis, references):
        """
        Display the diagnosis results and references.
        """
        if diagnosis:
            print("\nPossible solutions:")
            for i, action in enumerate(diagnosis, 1):
                print(f"{i}. {action}")
            
            if references:
                print("\nReferences for further help:")
                for i, ref in enumerate(references, 1):
                    print(f"{i}. {ref}")
        else:
            print("\nNo matching issues found. Please consult a professional technician.")

    def show_how_to_use(self):
        """
        Display instructions on how to use the program.
        """
        print("\n--- How to Use This Program ---")
        print("1. View all symptoms: Displays a list of all possible symptoms.")
        print("2. Diagnose PC issue: Enter your PC's symptoms to get a diagnosis.")
        print("3. How to use this program: Display these instructions.")
        print("4. Exit: Close the program.")
        print("\nSteps to diagnose a PC issue:")
        print("- Select option 2 from the menu.")
        print("- Enter the symptom you're experiencing from the list.")
        print("- The program will provide possible solutions and references for further help.")

    def show_menu(self):
        """
        Display an interactive menu for the user.
        """
        while True:
            print("\n--- PC Troubleshooter Menu ---")
            print("1. View all symptoms")
            print("2. Diagnose PC issue")
            print("3. How to use this program")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\nHere is the list of all possible symptoms:")
                for rule in self.rules.values():
                    print(f"- {rule['symptom']}")
            elif choice == "2":
                symptom = self.get_user_input()
                diagnosis, references = self.diagnose(symptom)
                self.show_diagnosis(diagnosis, references)
            elif choice == "3":
                self.show_how_to_use()
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


# Main program
if __name__ == "__main__":
    troubleshooter = PCTroubleshooter()
    troubleshooter.show_menu()