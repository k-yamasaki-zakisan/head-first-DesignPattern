from abc import ABCMeta, abstractmethod

class Menuitem(metaclass=ABCMeta):
    def __inin__(self, name:str, description:str, vegetarian:bool, price:float):
        self.__name = name
        self.__description = description
        self.__vegetarian = vegetarian
        self.__price = price
    
    @property
    def name(self) ->str:
        return self.__name
    
    @property
    def description(self) ->str:
        return self.__description
    
    @property
    def price(self) ->float:
        return self.__price
    
    @property
    def is_vegetarian(self) ->bool:
        return self.__vegetarian
    

    

    
    