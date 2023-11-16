import tkinter as tk
from urllib.request import urlopen
from urllib.error import URLError

def open_url():
    url = entry.get()
    try:
        response = urlopen(url)
        html_content = response.read().decode('utf-8')
        text.insert(tk.END, html_content)
    except URLError as e:
        text.insert(tk.END, f"Failed to open URL: {e.reason}\n")

root = tk.Tk()
root.title("Simple Browser")

# Entry field for URL input
entry = tk.Entry(root)
entry.pack(fill=tk.X)

# Button to open the URL
button = tk.Button(root, text="Open", command=open_url)
button.pack()

# Text area to display the web page content
text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
