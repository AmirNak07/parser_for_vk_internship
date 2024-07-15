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

    def good_request(self):
        req = requests.get(
            f"https://internship.vk.company/_next/data/1.5.20/vacancy/{self.id}.json?id={self.id}").text
        vk_response = json.loads(req)

        if not self.check_404(vk_response):
            good_response = {
                vk_response["pageProps"]["page"]["vacancy"]["id"]: {
                    "page": {
                        "id": vk_response["pageProps"]["page"]["vacancy"]["id"],
                        "title": vk_response["pageProps"]["page"]["vacancy"]["title"],
                        "direction": vk_response["pageProps"]["page"]["vacancy"]["direction"],
                        "city": vk_response["pageProps"]["page"]["vacancy"]["city"],
                        "workFormat": vk_response["pageProps"]["page"]["vacancy"]["format"],
                        "busyness": vk_response["pageProps"]["page"]["vacancy"]["employment_verbose"],
                        "aboutTasksText": vk_response["pageProps"]["page"]["vacancy"]["landing"]["aboutTasksText"]["items"],
                        "aboutSkillsText": vk_response["pageProps"]["page"]["vacancy"]["landing"]["aboutSkillsText"]["items"],
                        "link": f"https://internship.vk.company/_next/data/1.5.20/vacancy/{self.id}.json?id={self.id}",
                        "chapter": "Стажировка" if "стажировка" in str(vk_response) else "Вакансия"
                    }
                }
            }
            return good_response
        return {"statuscode": 404}

    def write_to_json(self, file_source):
        with open(file_source, "w", encoding="utf-8") as file:
            json.dump(self.good_request(), file, ensure_ascii=False, indent=4)


class PagesOfVacancies:
    def __init__(self) -> None:
        self.pages_json = {
            "pages": {}
        }

    def add_all_pages(self, start=500, stop=1200):
        for i in range(start, stop):
            page = Page(i)
            result = page.good_request()
            if result == {"statuscode": 404}:
                print(f"{i} -> Error: 404")
                continue
            self.pages_json["pages"][i] = result[i]
            print(f"{i} -> Successful")

    def write_all_to_json(self, file_source):
        with open(file_source, "w", encoding="utf-8") as file:
            json.dump(self.pages_json, file, ensure_ascii=False, indent=4)


pages = PagesOfVacancies()

pages.add_all_pages()
pages.write_all_to_json("good_response.json")
