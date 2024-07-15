import requests
import json


class Page:
    def __init__(self, id) -> None:
        self.id = id

    @staticmethod
    def check_404(request):
        try:
            if not request["pageProps"]["page"] and request["pageProps"]["responseStatus"] == 404:
                return True
            return False
        except KeyError:
            print("Invalid json")

    def good_request(self, id):
        req = requests.get(
            f"https://internship.vk.company/_next/data/1.5.20/vacancy/{id}.json?id={id}").text
        vk_response = json.loads(req)

        if not self.check_404(vk_response):
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
                    "chapter": "Стажировка" if "стажировка" in str(vk_response) else "Вакансия"
                }
            }
            return good_response
        return vk_response

    def write_to_json(self, file_source):
        with open(file_source, "w", encoding="utf-8") as file:
            json.dump(self.good_request(self.id), file,
                      ensure_ascii=False, indent=4)


id = 960
page = Page(id)

page.write_to_json("good_response.json")
