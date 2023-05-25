import mysql.connector
from car import Car

class DB:
    def __init__(self):
        self.__conn = mysql.connector.connect(host="localhost", user="root", password="", database="cardb")
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS car (
        id int(5) NOT NULL AUTO_INCREMENT,
        id_car varchar(50) DEFAULT NULL,
        model varchar(50) DEFAULT NULL,
        marque varchar(50) DEFAULT NULL,
        hp varchar(50) DEFAULT NULL,
        PRIMARY KEY(id)
        );
        """)
        self.close()

    def checkConnection(self):
        if not self.__conn.is_connected():
            self.__conn = mysql.connector.connect(host="localhost", user="root", password="", database="cardb")
            self.__cursor = self.__conn.cursor()

    def addCar(self, car: Car) -> bool:
        self.checkConnection()
        try:
            self.__cursor.execute(
                """INSERT INTO car (id_car, hp, marque, model) VALUES (%s, %s, %s, %s)""",
                car.info()
            )
            self.__conn.commit()
            return True
        except:
            return False
        finally:
            self.close()

    def getAllCars(self) -> bool | list:
        self.checkConnection()
        try:
            self.__cursor.execute("""SELECT * FROM car""")
            rows = self.__cursor.fetchall()
            return list(rows)
        except:
            return False
        finally:
            self.close()
    def getCarById(self, id: int) -> tuple | bool:
        self.checkConnection()
        try:
            self.__cursor.execute("""SELECT * FROM car WHERE id=%s""", (id,))
            row = self.__cursor.fetchone()
            return tuple(row)
        except:
            return False
        finally:
            self.close()

    def deleteCarById(self, id: int) -> bool:
        data=self.getCarById(id)
        self.checkConnection()
        try:
            self.__cursor.execute("""DELETE FROM car WHERE id=%s""", (id,))
            self.__conn.commit()
            self.__cursor.execute("SET @count = 0")
            self.__cursor.execute("UPDATE car SET id = @count:= @count + 1")
            self.__cursor.execute("ALTER TABLE car AUTO_INCREMENT = 1")
            self.__conn.commit()
            return data
        except:
            return False
        finally:
            self.close()

    def updateCar(self, id: int, car: Car) -> bool:
        self.checkConnection()
        try:
            self.__cursor.execute(
                """UPDATE car SET id_car=%s, hp=%s, marque=%s, model=%s WHERE id=%s""",
                (*car.info(), id)
            )
            self.__conn.commit()
            return self.getCarById(id)
        except:
            return False
        finally:
            self.close()
    def getLasElement(self)->bool|tuple|None:
        self.checkConnection()
        try:
            self.__cursor.execute("SELECT * FROM car ORDER BY id DESC LIMIT 1")
            row = self.__cursor.fetchone()
            if row:
                return tuple(row)
            else:
                return None
        except:
            return False
        finally:
            self.close()
    def close(self) -> bool:
        self.checkConnection()
        try:
            self.__cursor.close()
            self.__conn.close()
            return True
        except:
            return False

        

# a=(1,2,3)
# b=tuple(list(a)+[1])
# print(b)
# for i in b:
#     print(i)
