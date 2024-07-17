import tkinter as tk
from tkinter import messagebox

def calculate_WL(Vod, Ids, mu0, tox, epsilon0, epsilonox):
    Cox = epsilon0 * epsilonox / tox
    WL = (2 * Ids) / (mu0 * Cox * Vod**2)
    return WL

def calculate_and_display():
    try:
        Vod = float(entry_Vod.get())
        Ids = float(entry_IDS.get())
        mu0 = float(entry_mu0.get())
        tox = float(entry_tox.get())
        epsilon0 = float(entry_epsilon0.get())
        epsilonox = float(entry_epsilonox.get())

        WL = calculate_WL(Vod, Ids, mu0, tox, epsilon0, epsilonox)
        result_label.config(text=f"Calculated W/L parameter: {WL}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("W/L Parameter Calculator")

# Create labels and entry widgets for input
tk.Label(root, text="Vod (V):").grid(row=0, column=0)
entry_Vod = tk.Entry(root)
entry_Vod.grid(row=0, column=1)

tk.Label(root, text="Ids (A):").grid(row=1, column=0)
entry_IDS = tk.Entry(root)
entry_IDS.grid(row=1, column=1)

tk.Label(root, text="mu0 (m^2/Vs):").grid(row=2, column=0)
entry_mu0 = tk.Entry(root)
entry_mu0.grid(row=2, column=1)

tk.Label(root, text="tox (m):").grid(row=3, column=0)
entry_tox = tk.Entry(root)
entry_tox.grid(row=3, column=1)

tk.Label(root, text="epsilon0 (F/m):").grid(row=4, column=0)
entry_epsilon0 = tk.Entry(root)
entry_epsilon0.grid(row=4, column=1)

tk.Label(root, text="epsilonox (F/m):").grid(row=5, column=0)
entry_epsilonox = tk.Entry(root)
entry_epsilonox.grid(row=5, column=1)

# Create a button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=6, column=0, columnspan=2)

# Label to display the result
result_label = tk.Label(root, text="", anchor="w")
result_label.grid(row=7, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
