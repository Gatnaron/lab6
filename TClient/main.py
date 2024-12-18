import tkinter as tk
from tkinter import ttk, messagebox
import requests
from tkhtmlview import HTMLLabel

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите название города.")
        return

    try:
        url = f"http://localhost:3000?city={city}"
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text

            html_content = html_content.replace('<img', '<img width="120" height="120"')

            html_label.set_html(html_content)
        else:
            messagebox.showerror("Ошибка", "Не удалось получить данные о погоде.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка сети: {e}")

root = tk.Tk()
root.title("Прогноз погоды")  

root.geometry("450x550") 
root.resizable(False, False)  
root.eval('tk::PlaceWindow . center')  

header_frame = ttk.Frame(root)
header_frame.pack(pady=10)

city_label = ttk.Label(header_frame, text="Введите город:", font=("Arial", 12))
city_label.pack(side="left", padx=10)

city_entry = ttk.Entry(header_frame, width=20, font=("Arial", 12))
city_entry.pack(side="left")

get_weather_button = ttk.Button(root, text="Получить погоду", command=get_weather, width=20)
get_weather_button.pack(pady=20)

html_label = HTMLLabel(root, html="<p>Здесь будет прогноз погоды</p>", width=400, height=300)
html_label.pack(pady=10, fill="both", expand=True)

footer_label = ttk.Label(root, text="Выполнил студент группы бОИС-211 Оганян Иван", font=("Arial", 8), foreground="gray")
footer_label.pack(side="bottom", pady=5)

root.mainloop()
