from tkinterdnd2 import TkinterDnD, DND_FILES
from PyPDF2 import PdfReader, PdfWriter
from tkinter import messagebox
import tkinter as tk


class PdfMergeApp:
    def __init__(self, root):
        self.root = root
        self.files_data = []  # Stores file names and page ranges

        # Setup the GUI
        self.setup_gui()

    def setup_gui(self):
        self.root.title("PDFmerge v1.0")
        self.root.geometry("600x400")

        # Label to instruct the user
        label = tk.Label(self.root, text="Drag PDFs here   (one file at a time, in order)", padx=10, pady=10)
        label.pack(pady=0)

        # Listbox to show dropped files
        self.listbox = tk.Listbox(self.root, width=50, height=10)
        self.listbox.pack(pady=5)

        # Frame to hold the text boxes for specifying page ranges
        self.page_frame = tk.Frame(self.root)
        self.page_frame.pack(pady=10)

        # Button to combine the PDFs
        combine_button = tk.Button(self.root, text="Combine PDFs", command=self.combine_pdfs)
        combine_button.pack(pady=10)

        # Enable drag-and-drop functionality on the window
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.on_drop)

    def on_drop(self, event):
        files = event.data.split('#')
        pdf_files = [file for file in files]

        if pdf_files:
            for file in pdf_files:
                label = file.split('/')[-1]
                self.files_data.append([file, "", ""])  # File name and empty page range
                self.listbox.insert(tk.END, label)
                self.add_page_input(self.files_data[-1])  # Add input fields for pages
        else:
            messagebox.showwarning("Invalid Files", "No PDF files dropped!")

    def add_page_input(self, file_data):
        # Create a row of textboxes for each PDF to specify the page range
        row = tk.Frame(self.page_frame)
        row.pack()

        # File name label
        # label = file_data[0].split('/')[-1][0:-1]
        label = file_data[0].split('/')[-1]
        filename_label = tk.Label(row, text=label, width=50)
        filename_label.grid(row=0, column=0)

        # Read the PDF
        file_path = file_data[0]
        # pdf_reader = PdfReader(file_path[1:-1])
        pdf_reader = PdfReader(file_path)
        total_pages = len(pdf_reader.pages)

        # Textboxes for specifying page range
        start_page_entry = tk.Entry(row, width=5)
        start_page_entry.grid(row=0, column=1)
        start_page_entry.insert(tk.END, 1)  # Insert existing page range

        end_page_entry = tk.Entry(row, width=5)
        end_page_entry.grid(row=0, column=2)
        end_page_entry.insert(tk.END, total_pages)  # Insert existing page range

        # Save the entries in the file_data
        file_data[1] = start_page_entry
        file_data[2] = end_page_entry

    def combine_pdfs(self):
        # Create a PDF writer to combine files
        pdf_writer = PdfWriter()

        for file_data in self.files_data:

            # Read the PDF to get the total page count
            file_path = file_data[0]
            # pdf_reader = PdfReader(file_path[1:-1])
            pdf_reader = PdfReader(file_path)
            total_pages = len(pdf_reader.pages)

            # Get the folder path
            last_slash_idx = [i for i, ltr in enumerate(file_path) if ltr == '/'][-1]
            folder_path = file_path[0:last_slash_idx] + '/'

            start_page = file_data[1].get()
            end_page = file_data[2].get()

            try:
                start_page = int(start_page) - 1 if start_page else None
                end_page = int(end_page) if end_page else None
            except ValueError:
                messagebox.showerror("Invalid Input", f"Invalid page range for {file_path}")
                return

            self.start_page = 1
            self.end_page = total_pages

            # Check for valid page ranges
            if start_page is not None and (start_page < 0 or start_page >= total_pages):
                messagebox.showerror("Invalid Page Range", f"Invalid start page for {file_path}")
                return

            if end_page is not None and (end_page > total_pages or (start_page is not None and end_page < start_page)):
                messagebox.showerror("Invalid Page Range", f"Invalid end page for {file_path}")
                return

            # Extract pages from the PDF
            for page_num in range(start_page or 0, end_page or total_pages):
                pdf_writer.add_page(pdf_reader.pages[page_num])

        # Save the combined PDF
        output_file = folder_path + "Combined.pdf"
        with open(output_file, "wb") as out_file:
            pdf_writer.write(out_file)

        messagebox.showinfo("Success", f"PDFs combined successfully into {output_file}")


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PdfMergeApp(root)
    root.mainloop()
