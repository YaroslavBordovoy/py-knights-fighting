from typing import List

from app.knights.knights import Knight


class Armour:

    @staticmethod
    def get_armour(knights: List[Knight], armour: list) -> None:
        for i in armour:
            knights.protection += i["protection"]
