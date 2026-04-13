from time import sleep
from rich import print

class Televisao:
    def __init__(self):
        self.canal=1
        self.volume=50
        self.volume_min=0
        self.volume_max=100
        self.canal_min=1
        self.canal_max=20
        self.ligada=False
    
    
            
    def ligar(self):
        print('[yellow]Ligando Tv...[/]')
        sleep(1)
        print('[bold white]Tv ligada com sucesso.')
        self.ligada=True

    def desligar(self):
        print('[red]Desligando Tv...[/]')
        sleep(1)
        print('[bold white]Tv desligada com sucesso.')
        self.ligada=False
    

    def estar_ligada(func):
        def wrapper(self, *args, **kwargs):
            if not self.ligada:
                print('A Tv não está ligada')
                return 
            return func(self, *args,**kwargs)
        return wrapper
    
    @estar_ligada
    def mudar_canalcima(self):

        if self.canal < self.canal_max:
            self.canal+=1
        
        elif self.canal==self.canal_max:
            self.canal=0
        
             
    @estar_ligada
    def mudar_canalbaixo(self):
        
        if self.canal > self.canal_min:
            self.canal-=1
        elif self.canal ==self.canal_min:
            self.canal=20
    
    @estar_ligada
    def aumentar_volume(self):
        if self.volume==self.volume_max:
            print('[bold purple]Volume máx[/]')
            return
        elif self.volume < self.volume_max:
            self.volume+=10
            
    
    @estar_ligada
    def diminuir_volume(self):
        
        if self.volume==self.volume_min:
            print("[bold blue]Volume mín[/]")
            return
        elif self.volume > self.volume_min:
            self.volume-=10
        
            
    
    def __str__(self):
        return f"Televisao - Ligada {self.ligada} \n- Canal: {self.canal} \n- Volume: {self.volume}"


tv=Televisao()

tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
tv.mudar_canalcima()
tv.mudar_canalcima()
print(tv)
sleep(3)


    

