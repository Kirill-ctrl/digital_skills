import inspect
from typing import List

from exc_for_comp import AddElemCompException, CompTurnOnException


class Computer:

    def __init__(self,
                 processor: str,
                 block_power: int,
                 hdd: List[dict],
                 memory: int,
                 switch_on: bool = False):
        """
        Method-constructor
        """
        self._processor = processor
        self._block_power = block_power
        self.hdd = hdd
        self.memory = memory
        if not switch_on:
            self._switch_on = switch_on
        else:
            raise CompTurnOnException("Computer need turn of (switch_on=False)")
        self.__hdd_value_common = sum([self.add_hdd(*item.values(), init=True) for item in self.hdd])

    def __call__(self, state: bool = True):
        """
        When the function is called, the computer turns on
        """
        self._switch_on = state

    def __str__(self):
        """Print base text by collected object"""
        return "I am Computer with processor: {proc}, memory: {memory} GB and {hdd} GB for hdd".format(
            proc=self._processor,
            memory=self.memory,
            hdd=self.__hdd_value_common
        )

    def __add__(self, *args, **kwargs):
        """
        Adds the passed parameter to a specific object.
        Must be redefined in daughter classes if expanded functional to add
        """
        # Определяет откуда вызов функции
        if inspect.getouterframes(inspect.currentframe())[1].function == self.add_hdd.__name__:
            self.__hdd_value_common += self.hdd[-1]['value']
        else:
            raise AddElemCompException("Element to add is not defined")

    def __gt__(self, other: int):
        """Check by power"""
        if self._block_power > other:
            print('I will not change')
            return False
        else:
            self.__lt__(other)

    def __lt__(self, other: int):
        """Check by power"""
        if self._block_power < other:
            print('I agree, new is better')
            return True

    @property
    def hdd_value_common(self):
        """For using in daughter classes"""
        return self.__hdd_value_common

    @hdd_value_common.setter
    def hdd_value_common(self, value: int):
        """For using in daughter classes"""
        self.__hdd_value_common = value

    def turn_on(self):
        """Turn on computer"""
        self._switch_on = True

    def turn_off(self):
        """Turn off computer"""
        self._switch_on = False

    def swap_processor(self, new_processor: str):
        """
        Change the processor if the specified conditions are met
        """
        if not self._switch_on:
            if isinstance(new_processor, str):
                self._processor = new_processor
            else:
                raise TypeError
        else:
            raise CompTurnOnException("Computer is already turn on")

    def add_hdd(self, hdd_name: str, hdd_value: int, init: bool = False):
        """
        Adds dict in list[dict] for object Computer.hdd
        """
        if init:  # If called from __init__
            return hdd_value
        if not self._switch_on:
            self.hdd.append(
                {
                    "name": hdd_name,
                    "value": hdd_value
                }
            )
            self.__add__()
        else:
            raise CompTurnOnException("Computer is already turn on")

    def swap_block_power(self, block_power_value: int):
        """
        Change the block_power if the specified conditions are met
        """
        if not self._switch_on:
            if self.__gt__(block_power_value):
                self._block_power = block_power_value
        else:
            raise CompTurnOnException("Computer is already turn on")


if __name__ == '__main__':
    # собираем компьютер правильно
    comp_1 = Computer(
        processor='amd',
        block_power=650,
        hdd=[
            {
                "name": 'toshiba',
                "value": 1000
            }
        ],
        memory=16
    )
    print(comp_1)

    # собираем компьютер неправильно и обрабатываем ошибку
    try:
        comp_2 = Computer(
            processor='amd',
            block_power=650,
            hdd=[
                {
                    "name": 'toshiba',
                    "value": 1000
                }
            ],
            memory=16
        )
        print(comp_2)
    except CompTurnOnException as exc:
        print(exc.text_exc)

    comp_1.turn_on()
    try:
        comp_1.swap_processor(new_processor='intel')
    except CompTurnOnException as exc:
        print(exc.text_exc)
    comp_1.turn_off()
    comp_1.swap_processor(new_processor='intel')
    print(comp_1)
    comp_1.add_hdd('samsung', 1000)
    comp_1.add_hdd('samsung', 120)
    print(comp_1)
    print(comp_1.hdd_value_common)
    comp_1()
    try:
        comp_1.swap_block_power(700)
        comp_1.swap_block_power(500)
    except CompTurnOnException as exc:
        print(exc.text_exc)
    comp_1.turn_off()
    try:
        comp_1.swap_processor(12341)
    except TypeError:
        print('Processor not be int')
    print(comp_1._processor)
