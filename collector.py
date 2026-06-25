import json
from pathlib import Path

import requests

from config import BASE_URL, HEADERS


class Collector:

    def request(self, endpoint):

        url = f"{BASE_URL}/{endpoint}"

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def save_json(self, folder, filename, data):

        path = Path("data") / folder
        path.mkdir(parents=True, exist_ok=True)

        file = path / filename

        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"✔ Guardado: {file}")

    def download_world_cup_fixtures(self):

        data = self.request(
            "fixtures?league=1&season=2026"
        )

        self.save_json(
            "fixtures",
            "world_cup_2026.json",
            data
        )

        return data