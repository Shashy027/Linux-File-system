import os
import stat
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class FileGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File System")
        self.create_widgets()

    def create_widgets(self):
        self.create_btn = tk.Button(self, text="Create File", command=self.create_file)
        self.list_btn = tk.Button(self, text="List Files", command=self.list_files)
        self.delete_btn = tk.Button(self, text="Delete File", command=self.delete_file)
        self.read_btn = tk.Button(self, text="Read File", command=self.read_file)
        self.write_btn = tk.Button(self, text="Write to File", command=self.write_file)
        self.set_perm_btn = tk.Button(self, text="Set Permission", command=self.set_permission)
        self.exit_btn = tk.Button(self, text="Exit", command=self.quit)

        self.create_btn.pack(fill=tk.BOTH, padx=10, pady=5)
        self.list_btn.pack(fill=tk.BOTH, padx=10, pady=5)
        self.delete_btn.pack(fill=tk.BOTH, padx=10, pady=5)
        self.read_btn.pack(fill=tk.BOTH, padx=10, pady=5)
        self.write_btn.pack(fill=tk.BOTH, padx=10, pady=5)
        self.set_perm_btn.pack(fill=tk.BOTH, padx=10, pady=5)
        self.exit_btn.pack(fill=tk.BOTH, padx=10, pady=5)

        # Add context menu to the buttons
        self.add_context_menu(self.create_btn, ["Create File"])
        self.add_context_menu(self.list_btn, ["List Files"])
        self.add_context_menu(self.delete_btn, ["Delete File"])
        self.add_context_menu(self.read_btn, ["Read File"])
        self.add_context_menu(self.write_btn, ["Write to File"])
        self.add_context_menu(self.set_perm_btn, ["Set Permission"])
        self.add_context_menu(self.exit_btn, ["Exit"])

    def add_context_menu(self, widget, options):
        context_menu = tk.Menu(self, tearoff=0)
        for option in options:
            context_menu.add_command(label=option)
        widget.bind("<Button-3>", lambda e: context_menu.tk_popup(e.x_root, e.y_root))

    def create_file(self):
        filename = filedialog.asksaveasfilename(title="Create File", filetypes=(("All Files", "*.*"),))
        if filename:
            try:
                open(filename, 'w').close()
                messagebox.showinfo("Success", f"File '{filename}' created successfully.")
            except:
                messagebox.showerror("Error", f"Failed to create file '{filename}'.")

    def list_files(self):
        dirname = filedialog.askdirectory(title="Select Directory")
        if dirname:
            try:
                files = os.listdir(dirname)
                file_list = "\n".join(files)
                messagebox.showinfo("Listing Files", f"Listing files in directory '{dirname}':\n\n{file_list}")
            except:
                messagebox.showerror("Error", f"Failed to open directory '{dirname}'.")

    def delete_file(self):
        filename = filedialog.askopenfilename(title="Delete File", filetypes=(("All Files", "*.*"),))
        if filename:
            try:
                os.remove(filename)
                messagebox.showinfo("Success", f"File '{filename}' deleted successfully.")
            except:
                messagebox.showerror("Error", f"Failed to delete file '{filename}'.")

    def read_file(self):
        filename = filedialog.askopenfilename(title="Read File", filetypes=(("All Files", "*.*"),))
        if filename:
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                messagebox.showinfo("File Content", f"Content of file '{filename}':\n\n{content}")
            except:
                messagebox.showerror("Error", f"Failed to open file '{filename}'.")

    def write_file(self):
        filename = filedialog.asksaveasfilename(title="Write to File", filetypes=(("All Files", "*.*"),))
        if filename:
            try:
                content = simpledialog.askstring("Write to File", "Enter the content to write:")
                if content is not None:
                    with open(filename, 'w') as file:
                        file.write(content)
                    messagebox.showinfo("Success", f"Content written to file '{filename}' successfully.")
                else:
                    messagebox.showerror("Error", "No content provided.")
            except:
                messagebox.showerror("Error", f"Failed to write to file '{filename}'.")

    def set_permission(self):
        filename = filedialog.askopenfilename(title="Set Permission", filetypes=(("All Files", "*.*"),))
        if filename:
            try:
                permission = simpledialog.askstring("Set Permission", "Enter the permission (e.g., 0644):")
                if permission is not None:
                    octal_permission = int(permission, 8)
                    os.chmod(filename, octal_permission)
                    messagebox.showinfo("Success", f"Permission set successfully for '{filename}'.")
                else:
                    messagebox.showerror("Error", "No permission provided.")
            except:
                messagebox.showerror("Error", f"Failed to set permission for '{filename}'.")

def main():
    file_gui = FileGUI()
    file_gui.mainloop()

if __name__ == "__main__":
    main()
