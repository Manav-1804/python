# Assessment
#Module 15) Python - Advance python programming
#Case Overview
#You are hired as a Junior Python Developer to build a small desktop-based application called
#MiniBlog. The app allows users to create, view, and save blog posts using a simple graphical interface.
#This app will help reinforce basic programming concepts such as file operations, exception handling, classes, and a Tkinter GUI. Core Features User Post Creation • User can enter their name, post title,
#and post content
#• Use GUI input fields (Entry, Text widgets) Save Post to File • Each post is saved to a text file using a naming format like username_title.txt
#• Use file handling to write post content
#View Saved Posts • User can select and view previously saved posts from a dropdown (or Listbox)
#• Read content from selected file and display in the GUI Basic Error Handling • Handle cases like empty fields or file not found
#• Show messages using messagebox Skills Tested
#• Tkinter GUI: Entry, Text, Label, Button, Listbox
#• File Handling: Open, write, read
#• Classes & Objects: Basic User and Post class
#• Exception Handling: Try-Except block.



import os
import tkinter as tk
from tkinter import messagebox

# -------------------- Classes --------------------

class User:
    def __init__(self, name):
        self.name = name


class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title
        self.content = content

    def filename(self):
        safe_title = self.title.replace(" ", "_")
        return f"{self.user.name}_{safe_title}.txt"


# -------------------- GUI Application --------------------

class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog Application")
        self.root.geometry("500x500")

        
        tk.Label(root, text="User Name:").pack()
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.pack()

        tk.Label(root, text="Post Title:").pack()
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack()

        tk.Label(root, text="Post Content:").pack()
        self.content_text = tk.Text(root, width=50, height=10)
        self.content_text.pack()

       
        tk.Button(root, text="Save Post", command=self.save_post).pack(pady=5)
        tk.Button(root, text="Load Posts", command=self.load_posts).pack(pady=5)

        
        tk.Label(root, text="Saved Posts:").pack()
        self.post_listbox = tk.Listbox(root, width=50)
        self.post_listbox.pack()
        self.post_listbox.bind("<<ListboxSelect>>", self.view_post)

    # -------------------- Functions --------------------

    def save_post(self):
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showerror("Error", "All fields are required!")
            return

        user = User(name)
        post = Post(user, title, content)

        try:
            with open(post.filename(), "w") as file:
                file.write(f"Author: {name}\n")
                file.write(f"Title: {title}\n\n")
                file.write(content)

            messagebox.showinfo("Success", "Post saved successfully!")
            self.clear_fields()
            self.load_posts()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_posts(self):
        self.post_listbox.delete(0, tk.END)
        try:
            files = [f for f in os.listdir() if f.endswith(".txt")]
            for file in files:
                self.post_listbox.insert(tk.END, file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No posts found.")

    def view_post(self, event):
        try:
            selected_file = self.post_listbox.get(self.post_listbox.curselection())
            with open(selected_file, "r") as file:
                content = file.read()

            self.content_text.delete("1.0", tk.END)
            self.content_text.insert(tk.END, content)

        except IndexError:
            pass
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)


# -------------------- Run App --------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()
