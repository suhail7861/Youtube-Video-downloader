import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_youtube_video(video_url, output_path='.'):
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()

        if video:
            messagebox.showinfo('Info', f'Downloading: {yt.title}...')
            video.download(output_path)
            messagebox.showinfo('Info', 'Download complete!')
        else:
            messagebox.showerror('Error', 'No available video format to download.')
    except Exception as e:
        messagebox.showerror('Error', f'Error: {e}')

def on_download_button_click():
    video_url = url_entry.get()
    download_youtube_video(video_url)

# Create main application window
app = tk.Tk()
app.title('YouTube Video Downloader')

# URL Entry
url_label = tk.Label(app, text='Enter YouTube video URL:')
url_label.pack(pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

# Download Button
download_button = tk.Button(app, text='Download', command=on_download_button_click)
download_button.pack(pady=10)

# Start the application main loop
app.mainloop()
