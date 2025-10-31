import os
from dataclasses import dataclass
os.system("cls")

@dataclass

class autor:
    nome : str
    biografia : str

@dataclass

class livro:
    titulo : str
    ano : int

def exibir_detalhes(self):
    print(f"titulo:{self.titulo}")  
    print(f"Ano de publicacao:{self.ano}")  
    print(f"autor: {self.autor}")

autor1 = autor(nome ="Jorge Amado",biografia="um dos maiores autores brasileiros"  )
# cria uma instancia de livro e associando               
livro1 = livro (titulo ="capitaes de areia",ano =1937,autor=autor1 )
livro1.exibir_detalhes()

        
  
    