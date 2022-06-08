class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    # write method computeDefference
     # https://www.youtube.com/watch?v=RFGXxnEAejo
    def computeDifference(self):
        # toma el array 
        # array = a
        # buscar todaas las diferencias
        f,c = 0, 0
        listado_diferencias = []

        # a = [1,2,5]
        for i in a:
            # if resultado < (a[1+c] - a[0+f]):
                listado_diferencias.append(a[1+c] - a[0+f])
                c+=1
                if c == (len(a)-1):
                    f+=1
                    c-=1
            # else:
              #   return resultado
        print(f"listado es: {listado_diferencias}")
        # return listado_diferencias

        # ir guardando los resultados
        # devolver el mas alto
    def add_maximumDifference(self, maximumDifference):
        b = self.computeDifference().sort()
        print(f"maximo: {maximumDifference}")
        # self.maximumDifference = b[len(b)-1]
        # return b[len(b)-1] 
    


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)