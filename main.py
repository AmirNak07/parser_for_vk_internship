# 1. ID - id
# 1. Позиция (Backend-Разработчик) - title
# 2. Направление (AI VK) - direction
# 3. Город (Москва) - city
# 4. Формат Работы (Комбинированный) - workFormat
# 5. Занятость (Полная) - busyness
# 6. Предстоящие задачи - aboutTasksText
# 7. Необходимо иметь - aboutSkillsText
# 8. Ссылка (https://internship.vk.company/vacancy/960) - link
# 9. Раздел (Стажировка) - chapter


import requests
import json


def check_404(request):
    if not request["pageProps"]["page"] and request["pageProps"]["responseStatus"] == 404:
        return True
    return False


def good_request(id):
    req = requests.get(
        f"https://internship.vk.company/_next/data/1.5.20/vacancy/{id}.json?id={id}").text

    vk_response = json.loads(req)

    if not check_404(vk_response):
        good_response = {
            "page": {
                "id": vk_response["pageProps"]["page"]["vacancy"]["id"],
                "title": vk_response["pageProps"]["page"]["vacancy"]["title"],
                "direction": vk_response["pageProps"]["page"]["vacancy"]["direction"],
                "city": vk_response["pageProps"]["page"]["vacancy"]["city"],
                "workFormat": vk_response["pageProps"]["page"]["vacancy"]["format"],
                "busyness": vk_response["pageProps"]["page"]["vacancy"]["employment_verbose"],
                "aboutTasksText": vk_response["pageProps"]["page"]["vacancy"]["landing"]["aboutTasksText"]["items"],
                "aboutSkillsText": vk_response["pageProps"]["page"]["vacancy"]["landing"]["aboutSkillsText"]["items"],
                "link": f"https://internship.vk.company/_next/data/1.5.20/vacancy/{id}.json?id={id}",
                "chapter": "Стажировка"
            }
        }
        return good_response
    return vk_response


id = 1

with open("response3.json", "w", encoding="utf-8") as file:
    json.dump(good_request(id), file, ensure_ascii=False, indent=4)