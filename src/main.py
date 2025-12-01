import flet as ft
from typing import Callable, Any
import random
import pyperclip

class InputNombre(ft.TextField):
    def __init__(self):
        super().__init__()
        self.name = self.value
        self.expand = True
        self.hint_text = "Nombre de Contraseña"
        self.bgcolor = "#003246"

class CantidadCaracteres(ft.Slider):
    def __init__(self):
        super().__init__(
            label='{value} Caracteres',
            min=3,
            max=50,
            divisions=47,
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
        self.alignment=ft.alignment.center
        self.border=ft.border.all(1,ft.Colors.CYAN_ACCENT)
        self.bgcolor="#02005E"
        self.content = ft.Column([
            ft.Text(f"{nombre.capitalize()}",size=35,weight=ft.FontWeight.BOLD),
            ft.Text(f"{contra}",size=15,text_align=ft.TextAlign.CENTER),
            ft.IconButton(icon=ft.Icons.CONTENT_COPY,on_click=self.copiar()),
            ft.IconButton(icon=ft.Icons.DELETE,on_click=lambda e: eliminar(self))
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        
    
    def copiar(self):
        pyperclip.copy(self.contenido)
        


class ListaContraCard(ft.GridView):
    def __init__(self):
        super().__init__(expand=True, max_extent=500, child_aspect_ratio=1)
        self.controls=[]
    def eliminar(self,what):
        self.controls.remove(what)


class GenerarButton(ft.ElevatedButton):
    def __init__(self,func):
        super().__init__(on_click=func)
        self.text = "Crear Contraseña segura"
        self.scale=1.25
        

def main(page: ft.Page):
    page.bgcolor="#040020"
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

    for i in page.client_storage.get_keys(""):
        valor = page.client_storage.get(i)
        listaContraCard.controls.append(ContraCard(valor,i,eliminar))

    




    page.add(
        ft.Text("Generador de contraseñas seguras",size=35,weight=ft.FontWeight.BOLD,font_family="Consolas"),
        ft.Row([
            nameinput
            
        ]
        ),
        charcount,
        GenerarButton(generate),
        listaContraCard
    )

ft.app(main)
