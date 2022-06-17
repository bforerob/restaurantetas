import tkinter
from estructuras import Pila
from estructuras import Queue

recetas = [['id', 'comida', 'precio'],
            ['1', 'hamburguesa', 5000],
            ['2', 'HotDog', 5000],
            ['3', 'Lasagna', 13000],
            ['4', 'Fritanga', 15000],
            ['5', 'ajiaco', 18000]]

pedidos = Queue()
ventas = Pila()
dinero = 0

def limpiarMenu():
    tituloMenu.pack_forget()
    tituloTomarPedido.pack_forget()
    tomarPedidoBot.pack_forget()
    administrarPedidosBot.pack_forget()
    administrarVentasBot.pack_forget()
    hamburguesaBot.pack_forget()
    menuPrincipalBot.pack_forget()
    perroCalienteBot.pack_forget()
    lasagnaBot.pack_forget()
    fritangaBot.pack_forget()
    ajiacoBot.pack_forget()
    felipeBot.pack_forget()
    listaPedidosTitulo.pack_forget()
    listaPedidos.pack_forget()
    entregarPedidoBot.pack_forget()
    pedidoEntregado.pack_forget()
    administrarVentas.pack_forget()
    borrarVentaBot.pack_forget()
    borrarVentasText.pack_forget()
    agregarPedidoText.pack_forget()
def tomarPedido():
    limpiarMenu()
    tituloTomarPedido.pack(padx=10, pady=10)
    hamburguesaBot.pack(padx=10, pady=5)
    perroCalienteBot.pack(padx=10, pady=5)
    lasagnaBot.pack(padx=10, pady=5)
    fritangaBot.pack(padx=10, pady=5)
    ajiacoBot.pack(padx=10, pady=5)
    felipeBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)

def agregarPedido(a):
    global dinero
    limpiarMenu()
    agregarPedidoText["text"] = "agregando " + '\n' + recetas[a][1] + " de " + str(recetas[a][2]) + "$ \n a la lista de pedidos"
    agregarPedidoText.pack(padx=10, pady=5)
    tomarPedidoBot.pack(padx=10, pady=5)
    administrarPedidosBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    pedidos.enqueue(recetas[a][1])
    ventas.apilar(recetas[a][2])
    ventas.apilar(recetas[a][1])
    dinero += recetas[a][2]
def administrarPedidos():
    limpiarMenu()
    if pedidos.length() == 0:
        listaPedidos["text"] = 'Aun no hay pedidos'
        listaPedidos.pack(padx=10, pady=10)
    else:
        listaPedidos["text"] = "Los pedidos pendientes son: "+ '\n' + pedidos.string()
        listaPedidos.pack(padx=10, pady=10)
        entregarPedidoBot.pack(padx=10, pady=10)
    menuPrincipalBot.pack(padx=10, pady=5)
def entregarPedido():
    limpiarMenu()
    pedidoEntregado["text"] = "entregando " + pedidos.head1()
    pedidoEntregado.pack(padx=10, pady=5)
    administrarPedidosBot.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    pedidos.dequeue()
def administrarVentas():
    global dinero
    limpiarMenu()
    if dinero == 0:
        administrarVentas["text"] = "aun no hay ventas el chuzo se cae a pedazos"
        administrarVentas.pack(padx=10, pady=5)
        menuPrincipalBot.pack(padx=10, pady=5)
    else:
        administrarVentas["text"] = "Las ventas son de " + str(dinero) +' $' + '\n'+ ventas.string()
        administrarVentas.pack(padx=10, pady=5)
        borrarVentaBot.pack(padx=10, pady=5)
        menuPrincipalBot.pack(padx=10, pady=5)

def borrarVentas():
    global dinero
    limpiarMenu()
    borrarVentasText["text"] = "Borrando la ultima venta: " + '\n' + str(ventas.tope()) + '\n'
    ventas.desapilar()
    borrarVentasText["text"] += str(ventas.tope())
    borrarVentasText.pack(padx=10, pady=5)
    administrarVentas.pack(padx=10, pady=5)
    menuPrincipalBot.pack(padx=10, pady=5)
    dinero -= ventas.tope()
    ventas.desapilar()


def menuPrincipal():
    limpiarMenu()
    tituloMenu.pack(padx=10, pady=10)
    tomarPedidoBot.pack(padx=10, pady=10)
    administrarPedidosBot.pack(padx=10, pady=10)
    administrarVentasBot.pack(padx=10, pady=10)
fondoVentana = '#49A'
fondoBotones = "#FFA833"
ventana = tkinter.Tk()
ventana.geometry("500x600")
ventana.resizable(width=0, height=0)
ventana['bg'] = fondoVentana

tituloMenu = tkinter.Label(ventana, text ="Bienvenido", font ="Helvetica 20"
                           , bg = fondoBotones)
tituloTomarPedido = tkinter.Label(ventana, text ="TOMAR UN PEDIDO"
                                  , font = "Helvetica 20")
tomarPedidoBot = tkinter.Button(ventana, text ="Tomar pedido"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones
                                , command = tomarPedido)
administrarPedidosBot = tkinter.Button(ventana, text ="Administrar encargos"
                                       , font = "Helvetica 20"
                                       , width = 30, height = 1
                                       , bg = fondoBotones
                                       , command = administrarPedidos)

entregarPedidoBot = tkinter.Button(ventana, text ="Entregar pedido"
                                       , font = "Helvetica 20"
                                       , width = 30, height = 1
                                       , bg = fondoBotones
                                       , command = entregarPedido)

administrarVentasBot = tkinter.Button(ventana, text ="Administrar ventas"
                                      , font = "Helvetica 20"
                                      , width = 30, height = 1
                                      , bg = fondoBotones
                                      , command = administrarVentas)

menuPrincipalBot = tkinter.Button(ventana, text =" Menu Principal"
                                  , font = "Helvetica 20"
                                  , width = 30, height = 1
                                  , bg = fondoBotones
                                  , command = menuPrincipal)

hamburguesaBot = tkinter.Button(ventana, text ="1. Hamburguesa : 5.000$"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones,
                                command = lambda : agregarPedido(1))
perroCalienteBot = tkinter.Button(ventana, text ="2. Perro Caliente : 5.000$"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones,
                                command = lambda : agregarPedido(2))
lasagnaBot = tkinter.Button(ventana, text ="3. lasagna : 13.000$"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones,
                                command = lambda : agregarPedido(3))
fritangaBot = tkinter.Button(ventana, text ="4. Fritanga : 5.000$"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones,
                                command = lambda : agregarPedido(4))
ajiacoBot = tkinter.Button(ventana, text ="5. Ajiaco : 18.000$"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones,
                                command = lambda : agregarPedido(5))

felipeBot = tkinter.Button(ventana, text ="6. FelipeGod : invaluable"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones)
listaPedidosTitulo  = tkinter.Label(ventana, text ="ESTOS SON LOS PEDIDOS"
                                    , font = "Helvetica 20")
listaPedidos  = tkinter.Label(ventana
                                    , font = "Helvetica 20")
pedidoEntregado = tkinter.Label(ventana
                                    , font = "Helvetica 20")
administrarVentas = tkinter.Label(ventana
                                    , font = "Helvetica 20")
borrarVentaBot = tkinter.Button(ventana, text ="Borrar Venta"
                                , font = "Helvetica 20"
                                , width = 30, height = 1
                                , bg = fondoBotones
                                , command = borrarVentas)
borrarVentasText = tkinter.Label(ventana
                                    , font = "Helvetica 20")

agregarPedidoText = tkinter.Label(ventana
                                    , font = "Helvetica 20")

tituloMenu.pack(padx=10, pady=10)
tomarPedidoBot.pack(padx=10, pady=10)
administrarPedidosBot.pack(padx=10, pady=10)
administrarVentasBot.pack(padx=10, pady=10)


ventana.mainloop()