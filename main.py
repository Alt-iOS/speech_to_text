import whisper
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def transcribe_audio():
    """
    This function opens a file dialog to select an audio file, loads a pre-trained model, and calls the transcribe_audio_helper
    function to transcribe the selected audio file. It also displays a charging icon while the transcription is being processed.
    """
    filepath = filedialog.askopenfilename(title="Select audio file", filetypes=[("WAV files", "*.wav")])
    if filepath:
        model = whisper.load_model(name="base", download_root="models")
        progress_bar.pack(fill=tk.X, padx=10)
        root.after(1000, transcribe_audio_helper, model, filepath)

def transcribe_audio_helper(model, filepath):
    """
    This function takes a pre-trained model and a filepath as input, transcribes the audio file at the given filepath using
    the model, and displays the transcribed text in the text_output widget. If an error occurs during transcription, an error
    message is displayed in a messagebox. Finally, the charging icon is hidden.
    """
    try:
        result = model.transcribe(filepath)
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "".join(result["text"]))
        text_output.config(state=tk.DISABLED)
        text_output.pack(fill=tk.BOTH, expand=True)
        progress_bar.pack_forget()

    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        progress_bar.pack_forget()

root = tk.Tk()
root.title("Speech to Text")

button_select = tk.Button(root, text="Select audio file", command=transcribe_audio)
button_select.pack(pady=10)

text_output = tk.Text(root, height=10, state=tk.DISABLED)
text_output.pack(padx=10, pady=10)

progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.pack_forget()

root.mainloop()
