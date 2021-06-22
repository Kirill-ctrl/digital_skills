import inspect
from typing import List

from abc_class import Computer


class OfficeComputer(Computer):
    def __init__(self,
                 processor: str,
                 block_power: int,
                 hdd: List[dict],
                 memory: int,
                 switch_on: bool = False):
        super().__init__(processor=processor,
                         block_power=block_power,
                         hdd=hdd,
                         memory=memory,
                         switch_on=switch_on)

    def __str__(self):
        return "I am simple office computer!"

    def __divmod__(self, other):
        if divmod(other, 2)[1] == 0:
            return True
        return False

    def __add__(self, *args, **kwargs):
        """Определяет откуда вызов функции"""
        if inspect.getouterframes(inspect.currentframe())[1].function == self.add_hdd.__name__:
            value = self.hdd_value_common + self.hdd[-1]['value']
            self.hdd_value_common = value
        elif inspect.getouterframes(inspect.currentframe())[1].function == self.add_memory.__name__:
            self.memory += kwargs['value']
        else:
            print("Element to add is not defined")

    @staticmethod
    def show_rgb():
        print('No, i will broken')

    def add_memory(self, addit: int):
        if not self._switch_on:
            if self.__divmod__(addit):
                self.__add__(value=addit)
            else:
                print("You cannot add memory whose number does not correspond to a power of two")
        else:
            print("Computer is already turn on")


if __name__ == '__main__':
    # собираем компьютер правильно
    office_comp_1 = OfficeComputer(
        processor='intel',
        block_power=650,
        hdd=[
            {
                "name": "toshiba",
                "value": 1000
            }
        ],
        memory=16
    )
    print(office_comp_1)

    office_comp_1.show_rgb()
    print(office_comp_1.memory)
    office_comp_1.add_memory(15)

    print(office_comp_1.memory)
