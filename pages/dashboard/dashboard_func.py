from flask import Flask, render_template
import requests
from config import config
from loader import app
from pathlib import Path

@app.route("/dashboard")
def dashboard():
    res = get_data_list()
    items_list, data_list = res[0], res[1]
    return render_template('dashboard/dashboard.html', title='Dashboard', data_list=data_list, items_list=items_list)


def get_data_list():
    with open(f"pages/dashboard/temp/{config.get('dashboard').get('file')}", "wb") as temp: # Любое название конечного файла
        temp.write(requests.get(config.get('dashboard').get('url_link')).content)
        temp.close()
    
    data_list = list()
    # В функцие ниже происходит обработка файла, получение списка списков
    with open(f"pages/dashboard/temp/{config.get('dashboard').get('file')}", "r", encoding='utf-8') as temp:
        for line in temp.readlines(): # Обрабатываем построчно
            temp_line = line.split(",") # Получаем массив строки
            for _ in range(len(temp_line)):
                t = temp_line[_].strip() # Убираем лишние пробелы у каждого элемента массива строки
                t = t.replace("\n", "") # Убираем знак переноса строки
                temp_line[_] = t
            data_list.append(temp_line) # Добавляем очищенную строку в общий массив
        temp.close()

    return (data_list.pop(0), data_list) 
            # Возвращаем первую строку с названиями стлобцов (мы её удаляем из массива, но метод возвращает её занчения)
                              # И весь массив с данными и с удалённой первой строкой
