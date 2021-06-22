import inspect
from typing import List

from abc_class import Computer
from exc_for_comp import AddElemCompException, CompTurnOnException


class GamingComputer(Computer):

    def __init__(self,
                 processor: str,
                 block_power: int,
                 hdd: List[dict],
                 memory: int,
                 graphics_card: List[str],
                 cooling: bool,
                 rgb: str,
                 ssd: bool,
                 work_cooling: bool = False,
                 switch_on: bool = False):
        super().__init__(processor=processor,
                         block_power=block_power,
                         hdd=hdd,
                         memory=memory,
                         switch_on=switch_on)
        self._graphics_card = graphics_card
        self.cooling = cooling
        self.work_cooling = work_cooling
        self.rgb = rgb
        self.ssd = ssd

    def swap_rgb(self, hex_format):
        self.rgb = hex_format

    def turn_on(self):
        super().turn_on()
        self.work_cooling = True

    def turn_off(self):
        self.work_cooling = False
        super().turn_off()

    def swap_graphics_card(self, old_card, new_card):
        if not self._switch_on:
            index_swap = self._graphics_card.index(old_card)
            self._graphics_card[index_swap] = new_card
        else:
            raise CompTurnOnException("Computer is already turn on")

    def __str__(self):
        base = super().__str__()
        base += ". I have {count_graphic_card} video card's. ".format(
            count_graphic_card=len(self._graphics_card))
        if self.ssd:
            base += "I have ssd"
        return base

    def add_memory(self, addit: int):
        if not self._switch_on and self.__divmod__(addit):
            self.__add__(value=addit)
        else:
            raise CompTurnOnException("Computer is already turn on")

    def __divmod__(self, other):
        if divmod(other, 4)[1] == 0:
            return True

    def add_graphic_card(self, other: str):
        if not self._switch_on:
            if self.__lt__(other):
                self.__add__(card=other)
            else:
                raise AddElemCompException("Cannot add video card")
        else:
            raise CompTurnOnException("Computer is already turn on")

    def __lt__(self, other: str):
        if len(self._graphics_card) < 2:
            return True
        return False

    def __add__(self, *args, **kwargs):
        """Определяет откуда вызов функции"""
        if inspect.getouterframes(inspect.currentframe())[1].function == self.add_hdd.__name__:
            value = self.hdd_value_common + self.hdd[-1]['value']
            self.hdd_value_common = value
        elif inspect.getouterframes(inspect.currentframe())[1].function == self.add_memory.__name__:
            self.memory += kwargs['value']
        elif inspect.getouterframes(inspect.currentframe())[1].function == self.add_graphic_card.__name__:
            self._graphics_card.append(kwargs['card'])
        else:
            raise AddElemCompException("Element to add is not defined")


if __name__ == '__main__':
    # собираем компьютер
    gaming_comp_1 = GamingComputer(
        processor='intel',
        block_power=700,
        hdd=[{
            "name": "toshiba",
            "value": 1000
        },
            {
                "name": "samsung",
                "value": 1000,
            }],
        memory=32,
        graphics_card=['GTX 1060', 'GTX 1080'],
        cooling=True,
        rgb='#ffffff',
        ssd=True
    )
    print(gaming_comp_1)
    # Собираем компьютер во включенном состоянии
    try:
        gaming_comp_2 = GamingComputer(
            processor='intel',
            block_power=700,
            hdd=[{
                "name": "toshiba",
                "value": 1000
            },
                {
                    "name": "samsung",
                    "value": 1000,
                }],
            memory=32,
            graphics_card=['GTX 1060', 'GTX 1080'],
            cooling=True,
            rgb='#ffffff',
            ssd=True,
            switch_on=True
        )
        print(gaming_comp_2)
    except CompTurnOnException as exc:
        print(exc.text_exc)

    try:
        gaming_comp_1.add_graphic_card('GTX 1080')
    except AddElemCompException as exc:
        print(exc.text_exc)
        gaming_comp_1.swap_graphics_card(old_card='GTX 1060', new_card='GTX 1080')

    print(gaming_comp_1._graphics_card)
