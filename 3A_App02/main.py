import flet as ft
from pip._vendor.rich import align
from flet_core.alignment import Alignment


def main(page: ft.Page):
    page.title="¿Me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.bgcolor="pink"
    
    lbl1=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40,weight="bold"))
    
    Img1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50)
    
    btnNo=ft.ElevatedButton("no",
                            color="red",
                            width=100,
                            height=50)
    
    def no(e):
        btnSi.width+=30
        btnNo.height+=10
        pagex.update()
        
    def si(e):
        Img1.src="feliz.png"
        pagex.update()
        
    btnSi.on_click=si
    btnNo.on_click=no


    page.add(
        ft.Column(
            [
                lbl1,
                Img1,
                ft.Row([btnSi,btnNo],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20 
        ) 
        
    )
    
    
    
    
ft.app(main)
