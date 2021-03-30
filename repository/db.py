from domain.types import *


class DB:

    objetsInventary = [
        AgedBrie("Aged Brie", 2, 0),
        NormalItem("Elixir of the Mongoose", 5, 7),
        NormalItem("+5 Dexterity Vest", 10, 20),
        Sulfuras("Hand of Ragnaros", 0, 80),
        Sulfuras("Hand of Ragnaros", -1, 80),
        BackstagePasses("TAFKAL80ETC concert", 15, 20),
        BackstagePasses("TAFKAL80ETC concert", 10, 49),
        BackstagePasses("TAFKAL80ETC concert", 5, 49),
        NormalItem("Conjured Mana Cake", 3, 6),
    ]

    @classmethod
    def get_objeto(cls, name):
        items = cls.objetsInventary
        return [item for item in items if item.name == name][0]
