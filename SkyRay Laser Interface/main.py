import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage


"""SkyRay Laser Systems Control Interface"""

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Laser System Control Interface")
        self.geometry("1200x800")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        MainMenu(self).grid(row=0, column=0, sticky="nsew")

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Main Frame (Covers the entire application area)
        self.ana_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#0f0f1a")
        self.ana_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Configure the grid for the inner frames (Left and Right)
        self.ana_frame.grid_columnconfigure(0, weight=3) # Left Frame gets more space (e.g., 3 parts)
        self.ana_frame.grid_columnconfigure(1, weight=1) # Right Frame gets less space (e.g., 1 part)
        self.ana_frame.grid_rowconfigure(0, weight=1)

        # Right Frame (Info Display and Buttons)
        right_frame = ctk.CTkFrame(self.ana_frame,
                                     corner_radius=20,
                                     fg_color="#3a3a4a")
        # Placing the right frame using grid to define its relative width (weight=1)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 10), pady=10)

        # Left Frame (Image and Laser System Panels)
        left_frame = ctk.CTkFrame(self.ana_frame,
                                       corner_radius=20,
                                       fg_color="#1a1a2e")
        # Placing the left frame using grid to define its relative width (weight=3)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=10)


        # ------------------------------------------------------------------
        # --- RIGHT PANEL (CURRENT STATUS AND EVENT LOG) ---
        # ------------------------------------------------------------------
        
        # Logo Label
        # pil_image = Image.open("docs/logo.png")
        import os
        base_path = os.path.dirname(__file__)
        pil_image = Image.open(os.path.join(base_path, "docs", "logo.png"))

        resized_pil_image = pil_image.resize((500, 250))
        ctk_image = ctk.CTkImage(light_image=resized_pil_image, 
                         dark_image=resized_pil_image, # Use the same image for both modes
                         size=(378, 250))
        logo_label = ctk.CTkLabel(right_frame, image=ctk_image, text="")
        logo_label.place(relx=0.15, rely=0.02, relwidth=0.7, relheight=0.2)
        # Status Label
        ctk.CTkLabel(right_frame, text="SYSTEM STATUS", font=ctk.CTkFont(weight="bold", size=18)).place(relx=0.07, rely=0.23)
        
        current_status_text = ctk.CTkLabel(right_frame, text="""
Date/Time: 01.07.2025 12:00
Connection: SPW ACTIVE 
Mode: AUTONOMOUS FLIGHT
Target Lock: Object ID-42
Laser Status: READY POWER TRANSMİSSİON
""", justify=ctk.LEFT, text_color="#00ffff")
        current_status_text.place(relx=0.07, rely=0.26)

#         current_status_text2 = ctk.CTkLabel(right_frame, text="""
# Date/Time: 05.10.2025 (00:02:15)
# Section: ACTIVE (Laser Link / RF Backup)
# Mode: AUTONOMOUS / LINK
# Target Lock: Object ID: KH-04
# Coordinates: LAT: 41.0562 N, LON: 29.0068
# SIGNAL STATUS: LOCK ESTABLISHED / STEADY
# DATA RATE: 1.2 GBPS / NOMINAL
# """, justify=ctk.LEFT, text_color="#00ffff")
        # current_status_text2.place(relx=0.07, rely=0.26)


        # Event Log Header
        ctk.CTkLabel(right_frame, text="EVENT LOGS", font=ctk.CTkFont(weight="bold", size=18)).place(relx=0.07, rely=0.4)


        # Event Log Textbox
        info_textbox = ctk.CTkTextbox(right_frame,
                                          fg_color="#1a1a2e",
                                          text_color="white")
        info_textbox.place(relx=0.07,rely=0.45,relwidth=0.86,relheight=0.3)
                              
        log_text = """
[12:05:15] [DRS] Target Locked: Object ID-81
[12:05:20] [SPW] Power Receiver Ready
[12:05:55] [DRS] Laser Fired Successfully. Orbit Change Confirmed
[12:06:30] [SPW] Battery Fill Level: 95%
[12:07:00] [GPW] Energy Beam Terminated
[12:07:45] [DRS] Target Lost: Object ID-81
[12:08:10] [SYS] Temperature Nominal: 54°C
[12:08:30] [SYS] All systems operating within safe parameters
"""
        log_text2 = """
[00:01:05] [BMS] Target Lock: Object ID-KH-04 (41.0562 N, 29.0068 E) Confirmed.  
[00:01:20] [GPW] Laser Power Transmission Initiated (Manual). Beam Frequency Lock Achieved.  
[00:01:30] [BMS] Power Link Established with Ground Station GS-1. Transfer Efficiency: 85%.  
[00:01:50] [LSR] Beam Stability Nominal. Atmospheric Attenuation: 0.12 dB/km.  
[00:02:15] [SYS] System Health Check: All parameters within safe limits. Temperature: 45°C, Power Levels: Optimal.  

 """
        log_text3 = """
[00:00:05] [SYS] System Boot Initiated. All systems nominal.
[00:00:15] [BMS] Battery Status: 100% (Fully Charged)
[00:00:30] [NAV] GPS Lock Acquired. Coordinates: 41.0562 N, 29.0068 E
[00:00:45] [COM] Communication Link Established with Ground Station GS-1    
[00:01:00] [SPW] Target Lock: ENERGY IS BEING TRANSFERRED."""
        info_textbox.insert("0.0", log_text3)
        info_textbox.configure(state="disabled")

        # --- RIGHT PANEL CONTROL BUTTONS ---
        button_stop = ctk.CTkButton(right_frame, text="STOP ALL SYSTEMS", 
                                 hover_color="#751301", 
                                 fg_color="#9a1010", 
                                 text_color="white")
        button_stop.place(relx=0.07, rely=0.76, relheight=0.1, relwidth=0.86,)

        button_ignition = ctk.CTkButton(right_frame, text=" START İGNİTİON",
                                 fg_color="#0a7a2a", 
                                 hover_color="#0a9a10")
        button_ignition.place(relx=0.07, rely=0.87, relheight=0.1, relwidth = 0.86,)

        # ------------------------------------------------------------------
        # --- LEFT PANEL (IMAGE) ---
        # ------------------------------------------------------------------
        try:
            # Image loading
            base_path = os.path.dirname(__file__)
            pil_image = Image.open(os.path.join(base_path, "docs", "Energy_transfer.jpg"))
        #     pil_image = Image.open("docs/istanbul-satellite.png") # Update image path
            ctk_image = CTkImage(light_image=pil_image, size=(800, 700))
            image_label = ctk.CTkLabel(left_frame, image=ctk_image, text="")
            image_label.place(relx=0.15, rely=0.02, relwidth=0.7, relheight=0.5)
        except FileNotFoundError:
             # If image is not found, display a warning label
            image_label = ctk.CTkLabel(left_frame, text="SATELLITE CAMERA FEED (File Not Found)", fg_color="#3a3a4a")
            image_label.place(relx=0.15, rely=0.02, relwidth=0.7, relheight=0.5)


        # ------------------------------------------------------------------
        # --- 1. FRAME: DEBRIS REMOVAL SYSTEM (FUNCTIONAL BUTTONS) ---
        # ------------------------------------------------------------------
        debris_removal_frame = ctk.CTkFrame(left_frame,
                                             corner_radius=20,
                                             fg_color="#3a3a4a")
        debris_removal_frame.place(relx=0.02,rely=0.6,relwidth=0.3,relheight=0.3)
        debris_removal_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(debris_removal_frame, text="DEBRIS REMOVAL (DRS) CONTROL", font=ctk.CTkFont(weight="bold", size=10)).grid(row=0, column=0, pady=10, sticky="ew")
        
        # Buttons
        ctk.CTkButton(debris_removal_frame, text="Autonomous Target Lock", fg_color="#4f4f6e").grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(debris_removal_frame, text="Fire Laser (Manual)", fg_color="#2a7a4a").grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(debris_removal_frame, text="Stop Disposal Protocol", fg_color="#4f4f6e").grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        
        # ------------------------------------------------------------------
        # --- 2. FRAME: SATELLITE POWER SYSTEM (FUNCTIONAL BUTTONS) ---
        # ------------------------------------------------------------------
        satellite_power_frame = ctk.CTkFrame(left_frame,
                                             corner_radius=20,
                                             fg_color="#3a3a4a")
        satellite_power_frame.place(relx=0.35,rely=0.6,relwidth=0.3,relheight=0.3)
        satellite_power_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(satellite_power_frame, text=f"INTERSATELLİTE (SPW) POWER \nTRANSMİSSİON", font=ctk.CTkFont(weight="bold", size=10)).grid(row=0, column=0, pady=10, sticky="ew")

        # Buttons
        ctk.CTkButton(satellite_power_frame, text="Autonomous Pairing Mode", fg_color="#4f4f6e").grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(satellite_power_frame, text="Initiate Power Beam (Manuel)", fg_color="#e53935").grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(satellite_power_frame, text="Stop the power transmission", fg_color="#4f4f6e").grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        
        # ------------------------------------------------------------------
        # --- 3. FRAME: GROUND STATION POWER (FUNCTIONAL BUTTONS) ---
        # ------------------------------------------------------------------
        ground_station_power_frame = ctk.CTkFrame(left_frame,
                                             corner_radius=20,
                                             fg_color="#3a3a4a")
        ground_station_power_frame.place(relx=0.69,rely=0.6,relwidth=0.3,relheight=0.3)
        ground_station_power_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(ground_station_power_frame, text="GROUND STATION (GPW) \nPOWER TRANSMİSSİON",
                             font=ctk.CTkFont(weight="bold", size=10),
                             corner_radius=50).grid(row=0, column=0, pady=14, sticky="ew")

        # Buttons
        ctk.CTkButton(ground_station_power_frame, text="Initiate Target Lock", fg_color="#4f4f6e").grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(ground_station_power_frame, text="Initiate Power Beam (Manuel)", fg_color="#2a7a4a").grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        ctk.CTkButton(ground_station_power_frame, text="Stop the power transmission", fg_color="#4f4f6e").grid(row=3, column=0, padx=10, pady=5, sticky="ew")

    

# Application startup
if __name__ == "__main__":
    app = App()
    app.mainloop()