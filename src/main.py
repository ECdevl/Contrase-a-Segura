import flet as ft
from typing import Callable, Any
import random


class InputNombre(ft.TextField):
    def __init__(self):
        super().__init__()
        self.name = self.value
        self.expand = True
        self.hint_text = "Nombre de Contraseña"
        self.bgcolor = "#FFFFFF"
        self.color = ft.Colors.BLACK

class CantidadCaracteres(ft.Slider):
    def __init__(self):
        super().__init__(
            label='{value} Caracteres',
            min=3,
            max=25,
            divisions=25,
            value=10
        )
        
        self.char = int(self.value)
    
        self.on_change = self._changed

    def _changed(self, e):
        self.char = int(e.control.value)

class ContraCard(ft.Container):
    def __init__(self,nombre,contra,eliminar:Any = None):
        super().__init__()
        self.name = nombre
        self.contenido = contra
        self.border=ft.border.all(1,ft.Colors.GREY_600)
        self.bgcolor="#606060"
        self.content = ft.Column([
            ft.Text(f"{nombre.capitalize()}",size=35,text_align=ft.TextAlign.LEFT,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),
            ft.SelectionArea(ft.Text(f"{contra}",size=15,text_align=ft.TextAlign.CENTER,color=ft.Colors.WHITE)),
            ft.IconButton(icon=ft.Icons.DELETE,on_click=lambda e: eliminar(self),alignment=ft.alignment.center_right)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

        
 


        


class ListaContraCard(ft.GridView):
    def __init__(self):
        super().__init__(expand=True,child_aspect_ratio=1,max_extent=200)
        self.controls=[]
    def eliminar(self,what):
        self.controls.remove(what)


class GenerarButton(ft.ElevatedButton):
    def __init__(self,func):
        super().__init__(on_click=func)
        self.text = "Crear Contraseña segura"
        self.scale=1.25
        
class ContraMaestraStack(ft.Container):
    def __init__(self,contra_maestra = None,page = ft.Page,load_func = None):
        super().__init__()
        texto = ft.Text(size=30,font_family="Consolas",color=ft.Colors.AMBER,weight=ft.FontWeight.BOLD)
        self.load_func = load_func
        self.wrong = ft.Text(color=ft.Colors.RED)
        self.page = page
        self.border = ft.border.all(6,ft.Colors.BLACK)
        confirmar = ft.ElevatedButton(bgcolor=ft.Colors.GREEN,width=150,height=50)
        cancelar = ft.ElevatedButton("Continuar sin clave",bgcolor=ft.Colors.RED, on_click=self.cancel,width=150,height=50)
        self.field = ft.TextField(bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK)
        self.bgcolor = ft.Colors.GREY
        self.alignment = ft.alignment.bottom_center
        self.width = self.page.width / 2
        self.height = self.page.height / 2
        if contra_maestra == None:
            texto.value = "No hay una clave para proteger sus contraseñas seguras, introduzca una clave abajo para mayor seguridad"
            confirmar.text = "Establecer clave"
            confirmar.on_click = self.new_pass
            self.content = ft.Column([
                texto,
                self.field,
                ft.Row([confirmar,
                cancelar])
                
            ])
        else:
            cancelar.text = "Cerrar"
            cancelar.on_click = self.cerrar
            texto.value = "Introduzca su clave maestra para acceder a sus contraseñas"
            confirmar.text = "Confirmar"
            confirmar.on_click = self.check_master_pass
            self.content = ft.Column([
                texto,
                self.field,
                ft.Row([confirmar,cancelar])

            ]
            )

    def cancel(self,e):
        self.page.overlay.remove(self)
        self.page.update()
    
    def cerrar(self,e):
        self.page.window.close()

    def new_pass(self,e):
        if self.field.value != "":
            self.page.client_storage.set("maestra",str(self.field.value))
            self.page.overlay.clear()
            self.load_func()
            self.page.update()

    def check_master_pass(self,e):
        correcta = self.page.client_storage.get("maestra")
        if self.field.value == correcta:
            self.page.overlay.clear()
            self.load_func()
            self.page.update()
            
        else:
            self.wrong.value = "Clave incorrecta"
        



def main(page: ft.Page):
    page.bgcolor="#2C2C2C"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Contraseña Maestra"
    nameinput = InputNombre()
    listaContraCard = ListaContraCard()
    charcount = CantidadCaracteres()

    def eliminar(what):
        listaContraCard.controls.remove(what)
        page.client_storage.remove(what.contenido)
        page.update()

    def generate(e):
        caracteres = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        caracteres += [str(i) for i in range(10)]
        caracteres += ["!",'#',"$","%","&","/","+","-","?","¡","¿","ñ"]
        lista = []
        for _ in range(charcount.char):
            if random.choice([True,False]):
                lista.append(random.choice(caracteres).upper())
            else:
                lista.append(random.choice(caracteres).lower())
        ContraCardenia_final = ''.join(lista)
        listaContraCard.controls.append(ContraCard(nameinput.value,ContraCardenia_final,eliminar))
        page.client_storage.set(str(ContraCardenia_final),nameinput.value)
        page.update()

    def cargar():
        for i in page.client_storage.get_keys(""):
            if i != "maestra":
                valor = page.client_storage.get(i)
                listaContraCard.controls.append(ContraCard(valor,i,eliminar))

    
    



    page.add(
        ft.Text("Generador de contraseñas seguras",size=35,weight=ft.FontWeight.BOLD,font_family="Consolas",color=ft.Colors.WHITE),
        ft.Row([
            nameinput
            
        ]
        ),
        charcount,
        GenerarButton(generate),
        listaContraCard
    )
    page.overlay.append(ft.Stack([ContraMaestraStack(page.client_storage.get("maestra"),page,cargar)],expand=True,alignment=ft.alignment.center))
    page.update()

ft.app(main)
