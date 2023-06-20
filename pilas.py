from random import randint


class initialGraph:
    def __init__(self):
        self.__edges = {"AB": 0, "AC": 0, "BC": 0, "BD": 0, "CD": 0, "CE": 0, "DE": 0, "DF": 0, "EF": 0}
        self.__caminoSize = 0
        self.__ideal_Path = 0
        self.__total = 0
        self.__total_ideal = 0

    # crea un grafo al azar
    def update_edges(self):
        for i in self.__edges.keys():
            self.__edges[i] = randint(1, 5)
        return self.__edges

    # Hace la sumatoria del camino escogido por el usuario y la regresa(int)
    # La variable count siempre se pone en 0
    # la variable camino es la string que recibe del usuario
    def chosen_path(self, camino, count):
        listCamino = list(camino)
        self.__caminoSize = len(listCamino)
        for x in range(len(listCamino) - 1):
            #print(listCamino[count] + listCamino[count + 1])
            self.__total = self.__total + self.__edges[listCamino[count] + listCamino[count + 1]]
            count = count + 1
        return self.__total

    # encuentra el mejor camino y lo regresa en forma de lista[camino(string),resultado de sumatoria(int)]
    def ideal_path(self):
        b = ["ab", self.__edges["AB"]]
        c = ["ac", self.__edges["AC"]]
        if b[1] < c[1]:
            d = [b[0] + "d", b[1] + self.__edges["BD"]]
            if (self.__edges["BC"] + b[1]) < c[1]:
                c = [b[0] + "c", self.__edges["BC"] + b[1]]
            if d[1] < c[1]:
                e = [d[0] + "e", d[1] + self.__edges["DE"]]
                f = [d[0] + "f", d[1] + self.__edges["DF"]]
                if (self.__edges["CD"] + d[1]) < c[1]:
                    c = [d[0] + "c", self.__edges["CD"] + d[1]]
                if c[1] < e[1]:
                    if e[1] > (c[1] + self.__edges["CE"]):
                        e = ["abdce", c[1] + self.__edges["CE"]]
                    if e[1] < f[1]:
                        f = [e[0] + "f", e[1] + self.__edges["EF"]]
                else:
                    if e[1] < f[1]:
                        f = [e[0] + "f", e[1] + self.__edges["EF"]]

            else:
                e = [c[0] + "e", c[1] + self.__edges["CE"]]
                if (c[1] + self.__edges["CD"]) < d[1]:
                    d = [c[0] + "d", c[1] + self.__edges["CD"]]
                if d[1] < e[1]:
                    # nueva linea
                    f = [d[0] + "f", d[1] + self.__edges["DF"]]
                    e = [d[0] + "f", d[1] + self.__edges["DF"]]
                    if (d[1] + self.__edges["DE"]) < e[1]:
                        e = [d[0] + "e", d[1] + self.__edges["DE"]]
                    if (e[1] + self.__edges["EF"]) < f[1]:
                        f = [e[0] + "f", e[1] + self.__edges["EF"]]
                else:
                    f = [e[0] + "f", e[1] + self.__edges["EF"]]
                    if e[1] + self.__edges["DE"] < d[1]:
                        d = [e[0] + "d", e[1] + self.__edges["DE"]]
                    if (d[1] + self.__edges["DF"]) < f[1]:
                        f = [d[0] + "f", d[1] + self.__edges["DF"]]

        else:
            d = [c[0] + "d", c[1] + self.__edges["CD"]]
            e = [c[0] + "e", c[1] + self.__edges["CE"]]
            if (c[1] + self.__edges["BC"]) < b[1]:
                b = [c[0] + "b", c[1] + self.__edges["BC"]]
            if (b[1] + self.__edges["BD"]) < d[1]:
                d = [b[0] + "d", d[1] + self.__edges["BD"]]
            if d[1] < e[1]:
                f = [d[0] + "f", d[1] + self.__edges["DF"]]
                if (d[1] + self.__edges["DE"]) < e[1]:
                    e = [d[0] + "e", d[1] + self.__edges["DE"]]
                if (e[1] + self.__edges["EF"]) < f[1]:
                    f = [e[0] + "f", e[0] + self.__edges["EF"]]
            else:
                f = [e[0] + "f", e[1] + self.__edges["EF"]]
                if (e[1] + self.__edges["DE"]) < d[1]:
                    d = [e[0] + "d", e[1] + self.__edges["DE"]]
                if (d[1] + self.__edges["DF"]) < f[1]:
                    f = [d[0] + "f", d[1] + self.__edges["DF"]]
        return f

    def ideal_pathnumber(self):
        aux = 0
        aux2 = None
        for (i, j) in zip(self.__edges.keys(), self.__edges.values()):
            if aux2 is None:
                aux2 = i
                print(aux2)
            else:
                number = self.__edges[aux2]
                if number <= j:
                    aux += self.__edges[aux2]
                else:
                    aux += j
                aux2 = None
        self.__total_ideal = aux
        #return aux

    def compare_paths(self, chosen_path):
        self.ideal_pathnumber()
        shorter_way = False
        if self.chosen_path(chosen_path, 0) == self.__total_ideal:
            shorter_way = True
        return shorter_way


#if __name__ == '__main__':
    #c1 = initialGraph()
    #print(c1.update_edges())
    #print(c1.ideal_path())
    #print("El camino escogido da un total de: ", c1.chosen_path("ABCDEF", 0))
    #print("El camino mas optimo mide: ", c1.ideal_pathnumber())