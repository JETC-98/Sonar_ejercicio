import os


class ui:
    def __init__(self):
        self.__hi = "Hey, tenemos un problema, tenemos un grafo, queremos llegar del nodo A, al nodo F\n" \
                    "La idea es que encontremos la forma más rápida de llegar! \n " \
                    "La longitud de cada arista que conectan con un nodo son las siguientes:\n"
        self.__input = "Por favor, introduce el camino que tú creas el más corto: \n"
        self.__positive = "Asombroso, tu respuesta es correcta!"
        self.__negative = "La respuesta es incorrecta, éste es el camino más corto:"
        self.__continue = "¿Desea realizar otro ejercicio? \n"

    def main_menu(self):
        print(self.__hi)
        path = input(self.__input)
        path = path.upper()
        return path

    def feedback(self, flag):
        if flag:
            print(self.__positive)
        else:
            print(self.__negative)
        return flag

    def must_continue(self):
        Flag = False
        print(self.__continue)
        answer = input()
        answer = answer.upper()
        if answer != "N":
            Flag = True
        return Flag

    @staticmethod
    def cls():
        if os.name == "posix":
            os.system("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system("cls")

