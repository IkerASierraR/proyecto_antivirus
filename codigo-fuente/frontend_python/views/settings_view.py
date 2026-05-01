import customtkinter as ctk
import psutil
import threading

class SettingsView(ctk.CTkFrame):
    def __init__(self, parent, bridge):
        super().__init__(parent)
        self.bridge = bridge

        ctk.CTkLabel(self, text="Información del Sistema",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        hw_frame = ctk.CTkFrame(self)
        hw_frame.pack(pady=10, padx=20, fill="x")
        cpu = psutil.cpu_percent(interval=0.1)
        ctk.CTkLabel(hw_frame, text=f"CPU: {cpu}%").pack(anchor="w", padx=15, pady=5)
        mem = psutil.virtual_memory()
        ctk.CTkLabel(hw_frame, text=f"RAM: {mem.used//(1024**2)} MB / {mem.total//(1024**2)} MB ({mem.percent}%)").pack(anchor="w", padx=15, pady=5)

        try:
            disk = psutil.disk_usage('C:\\')
            disk_text = f"Disco C: {disk.free//(1024**3)} GB libre de {disk.total//(1024**3)} GB"
        except (OSError, PermissionError):
            disk_text = "Disco: Información no disponible"

        ctk.CTkLabel(hw_frame, text=disk_text).pack(anchor="w", padx=15, pady=5)