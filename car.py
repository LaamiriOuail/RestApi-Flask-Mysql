class Car:
    def __init__(self , id_car:str , model:str , hp:str , marque:str)->None:
        self.__model=model
        self.__hp = hp
        self.__marque=marque
        self.__id_car=id_car
    def info(self)->tuple:
        return (self.__id_car, self.__hp, self.__marque,self.__model)
        
        
        
    