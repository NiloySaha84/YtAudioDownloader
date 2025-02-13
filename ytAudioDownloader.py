import yt_dlp
import tkinter as tk
from tkinter import messagebox


def download_audio():
    link = entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a YouTube link")
        return

    try:
        with yt_dlp.YoutubeDL({'extract_audio': True, 'format':'bestaudio', 'outtmpl':'/Users/niloysaha/Documents/Songs/%(title)s.%(ext)s'}) as video:
            info_dict = video.extract_info(link, download=True)
            info_title = info_dict['title']
            messagebox.showinfo("Success", f"Downloaded: {info_title}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download{e}")

root = tk.Tk()
root.title("Youtube Audio Downloader")
root.geometry("800x600")

label = tk.Label(root, text="Enter YouTube Link:", font=("Arial", 12))
label.pack(pady=(200,5))

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_audio, font=("Arial", 12))
download_button.pack(pady=5)

root.mainloop()
