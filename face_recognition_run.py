import tkinter as tk
from tkinter import messagebox
import cv2
import threading
import random

class FaceRecognitionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Face Recognition App")
        self.video_running = False
        self.cap = None

        # UI elements
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        control_frame = tk.Frame(window)
        control_frame.pack(pady=10)

        self.start_btn = tk.Button(control_frame, text="Start", command=self.start_detection)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(control_frame, text="Stop", command=self.stop_detection, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=10)

        self.status_label = tk.Label(window, text="Status: Waiting to start...")
        self.status_label.pack()

        self.known_count = tk.Label(window, text="Known: 0")
        self.known_count.pack()

        self.unknown_count = tk.Label(window, text="Unknown: 0")
        self.unknown_count.pack()

    def start_detection(self):
        self.video_running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Detecting faces...")
        self.cap = cv2.VideoCapture(0)
        self.process_video()

    def stop_detection(self):
        self.video_running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped")
        self.known_count.config(text="Known: 0")
        self.unknown_count.config(text="Unknown: 0")
        self.canvas.delete("all")
        if self.cap:
            self.cap.release()

    def process_video(self):
        if not self.video_running:
            return

        ret, frame = self.cap.read()
        if ret:
            # Simulated detection
            face_count = random.randint(1, 3)
            known = sum(1 for _ in range(face_count) if random.random() > 0.5)
            unknown = face_count - known

            self.known_count.config(text=f"Known: {known}")
            self.unknown_count.config(text=f"Unknown: {unknown}")
            self.status_label.config(
                text="✓ Known face detected" if known else "✗ Unknown face detected",
                fg="green" if known else "red"
            )

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 480))
            img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = cv2.resize(img, (640, 480))
            self.photo = tk.PhotoImage(data=cv2.imencode('.ppm', img)[1].tobytes())
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(1000, self.process_video)  # Detect once per second

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()