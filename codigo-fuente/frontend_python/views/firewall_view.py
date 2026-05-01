import customtkinter as ctk
import threading

class FirewallView(ctk.CTkFrame):
    def __init__(self, parent, bridge):
        super().__init__(parent)
        self.bridge = bridge

        ctk.CTkLabel(self, text="🌐 Firewall de Windows",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=30)

        # Estado del firewall
        self.status_label = ctk.CTkLabel(self, text="Estado: Desconocido",
                                         font=ctk.CTkFont(size=14))
        self.status_label.pack(pady=10)

        # Switch para activar/desactivar el firewall
        self.firewall_var = ctk.BooleanVar(value=True)
        self.firewall_switch = ctk.CTkSwitch(self, text="Activar Firewall",
                                             variable=self.firewall_var,
                                             command=self.toggle_firewall,
                                             font=ctk.CTkFont(size=14))
        self.firewall_switch.pack(pady=20)

        # Resultado de la última operación
        self.result_label = ctk.CTkLabel(self, text="",
                                         font=ctk.CTkFont(size=12),
                                         text_color="gray")
        self.result_label.pack(pady=5)

        # Perfiles de red
        profiles_frame = ctk.CTkFrame(self)
        profiles_frame.pack(pady=20, padx=40, fill="x")
        ctk.CTkLabel(profiles_frame, text="Perfiles de red:",
                     font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", padx=15, pady=(10, 5))
        self.profile_labels = {}
        for profile in ("Dominio", "Privado", "Público"):
            lbl = ctk.CTkLabel(profiles_frame, text="",
                               font=ctk.CTkFont(size=12))
            lbl.pack(anchor="w", padx=15, pady=2)
            self.profile_labels[profile] = lbl
        ctk.CTkLabel(profiles_frame, text="").pack(pady=5)

        self._update_status_label()

    def toggle_firewall(self):
        enabled = self.firewall_var.get()
        self.result_label.configure(text="Aplicando cambios...", text_color="gray")
        threading.Thread(target=self._apply_firewall, args=(enabled,), daemon=True).start()

    def _apply_firewall(self, enabled):
        action = "firewall_on" if enabled else "firewall_off"
        result = self.bridge.send_command({"action": action}, wait_for_response=True)
        self.after(0, self._on_result, enabled, result)

    def _on_result(self, enabled, result):
        if result.get("status") == "ok":
            self.firewall_var.set(enabled)
            msg = "Firewall activado correctamente." if enabled else "Firewall desactivado."
            self.result_label.configure(text=msg, text_color="#2ECC71" if enabled else "#E74C3C")
        else:
            msg = result.get("message", "Error al cambiar el estado del firewall.")
            self.result_label.configure(text=f"Error: {msg}", text_color="#E74C3C")
            # Revertir el switch si falló
            self.firewall_var.set(not enabled)
        self._update_status_label()

    def _update_status_label(self):
        active = self.firewall_var.get()
        if active:
            self.status_label.configure(text="Estado: ✅ Activo", text_color="#2ECC71")
            icon, color = "✔", "#2ECC71"
        else:
            self.status_label.configure(text="Estado: ❌ Inactivo", text_color="#E74C3C")
            icon, color = "✘", "#E74C3C"
        for profile, lbl in self.profile_labels.items():
            lbl.configure(text=f"  {icon}  {profile}", text_color=color)
