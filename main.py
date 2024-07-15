# 1. Позиция (Backend-Разработчик) - position
# 2. Направление (AI VK) - direction
# 3. Город (Москва) - city
# 4. Формат Работы (Комбинированный) - work_format
# 5. Занятость (Полная) - busyness
# 6. Предстоящие задачи - tasks
# 7. Необходимо иметь - necessary_to_have
# 8. Ссылка (https://internship.vk.company/vacancy/960) - link
# 9. Раздел (Стажировка) - chapter


import requests
import json


id = 750

req = requests.get(f"https://internship.vk.company/_next/data/1.5.20/vacancy/{
    id}.json?id={id}").text

with open("response.json", "w", encoding="utf-8") as file:
    json.dump(json.loads(req), file, ensure_ascii=False, indent=4)


# for i in range(1000):
#     req_link = f"https://internship.vk.company/_next/data/1.5.20/vacancy/{
#     i}.json?id={i}"

#     req = requests.get(req_link).text
    
#     json.loads(req)