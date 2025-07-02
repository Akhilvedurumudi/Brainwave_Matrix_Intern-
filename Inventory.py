import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = 'inventory_data.json'
USERS_FILE = 'users.json'
LOW_STOCK_THRESHOLD = 5

# ------------------ Data Handling ------------------

def load_data(file, default):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump(default, f)
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

products = load_data(DATA_FILE, {})
users = load_data(USERS_FILE, {"admin": "admin123"})

# ------------------ Core Functionalities ------------------

def add_product(name, quantity, price):
    if name in products:
        messagebox.showerror("Error", "Product already exists.")
        return
    products[name] = {"quantity": int(quantity), "price": float(price)}
    save_data(DATA_FILE, products)
    messagebox.showinfo("Success", f"{name} added.")

def update_product(name, quantity, price):
    if name not in products:
        messagebox.showerror("Error", "Product not found.")
        return
    products[name] = {"quantity": int(quantity), "price": float(price)}
    save_data(DATA_FILE, products)
    messagebox.showinfo("Updated", f"{name} updated.")

def delete_product(name):
    if name in products:
        del products[name]
        save_data(DATA_FILE, products)
        messagebox.showinfo("Deleted", f"{name} deleted.")
    else:
        messagebox.showerror("Error", "Product not found.")

def get_sales_summary():
    total_value = sum(p["quantity"] * p["price"] for p in products.values())
    return f"Total Inventory Value: ₹{total_value:.2f}"

def get_low_stock_alerts():
    return [name for name, p in products.items() if p["quantity"] < LOW_STOCK_THRESHOLD]

# ------------------ GUI Section ------------------

def login_screen():
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username:").pack()
    username = tk.Entry(login_window)
    username.pack()

    tk.Label(login_window, text="Password:").pack()
    password = tk.Entry(login_window, show='*')
    password.pack()

    def login():
        user, pwd = username.get(), password.get()
        if user in users and users[user] == pwd:
            login_window.destroy()
            main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    tk.Button(login_window, text="Login", command=login).pack()
    login_window.mainloop()

def main_screen():
    window = tk.Tk()
    window.title("Inventory Management")

    # Product form
    tk.Label(window, text="Product Name").grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)

    tk.Label(window, text="Quantity").grid(row=1, column=0)
    qty_entry = tk.Entry(window)
    qty_entry.grid(row=1, column=1)

    tk.Label(window, text="Price").grid(row=2, column=0)
    price_entry = tk.Entry(window)
    price_entry.grid(row=2, column=1)

    def add():
        add_product(name_entry.get(), qty_entry.get(), price_entry.get())

    def update():
        update_product(name_entry.get(), qty_entry.get(), price_entry.get())

    def delete():
        delete_product(name_entry.get())

    def view_alerts():
        alerts = get_low_stock_alerts()
        messagebox.showinfo("Low Stock Products", ", ".join(alerts) if alerts else "All stocks are sufficient.")

    def view_sales():
        messagebox.showinfo("Sales Summary", get_sales_summary())

    tk.Button(window, text="Add Product", command=add).grid(row=3, column=0)
    tk.Button(window, text="Update Product", command=update).grid(row=3, column=1)
    tk.Button(window, text="Delete Product", command=delete).grid(row=3, column=2)
    tk.Button(window, text="Low Stock Alerts", command=view_alerts).grid(row=4, column=0)
    tk.Button(window, text="Sales Summary", command=view_sales).grid(row=4, column=1)

    window.mainloop()

# ------------------ Run App ------------------
if __name__ == "__main__":
    login_screen()
