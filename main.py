
from estructuras import Pila
from estructuras import LinkedList
from estructuras import Queue
recetas = [['id', 'comida', 'precio'],
            ['1', 'hamburguesa', 5000],
            ['2', 'HotDog', 5000]]

pedidos = Queue()
ventas = Pila()
dinero = 0

def tomarPedido():
    global dinero

    for i in range (0,len(recetas)):
        print(recetas[i][0], recetas[i][1], recetas[i][2])

    a = int(input("seleccione su comida: "))
    if (a == 0 or a >= len(recetas)):
        print("por favor dijite una opcion valida")
        tomarPedido()
    else:
        print("agregando ", recetas[a][1], "a la lista de pedidos")
        pedidos.enqueue(recetas[a][1])
        ventas.apilar(recetas[a][2])
        ventas.apilar(recetas[a][1])
        dinero += recetas[a][2]
        menu()


def observarPedidos():
    if pedidos.length() == 0:
        print("no tienes pedidos inbesil")
    else:
        print(pedidos.length())
        print(pedidos.string())
    menu()


def despacharPedido():
    if pedidos.length() == 0:
        print("no tienes pedidos inbesil")
    else:
        print("entregando " + pedidos.head1())
    pedidos.dequeue()
    menu()


def observarVentas():
    global dinero
    if dinero == 0:
        print("aun no hay ventas el chuzo se cae a pedazos")
        menu()
    else:
        print("Las ventas son de ", dinero,'$')
        print(ventas.string())
        print("1. si")
        print("2. no")
        n = input("¿desea borrar la ultima venta?")
        if n == '1':
            ventas.desapilar()
            dinero -= ventas.tope()
            ventas.desapilar()
            menu()
        if n == '2':
            menu()
        else:
            print("por favor digite una opcion valida")
            observarVentas()

def carta():
    for i in range(0, len(recetas)):
        print(recetas[i][0], recetas[i][1], recetas[i][2])
    menu()


def menu():
    print("-_-_-_Bienvenido al restaurante jaja_-_-_-")
    print("1. tomar pedido")
    print("2. observar pedidos")
    print("3. despachar pedido")
    print("4. observar ventas")
    print("5. carta de recetas")
    n = input("seleccione una opcion ")
    if n == '1':
        tomarPedido()
    if n == '2':
        observarPedidos()
    if n == '3':
        despacharPedido()
    if n == '4':
        observarVentas()
    if n == '5':
        carta()
    else:
        print("dijite una opcion valida")
        menu()
menu()


