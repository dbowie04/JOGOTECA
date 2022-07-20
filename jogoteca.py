from flask import Flask, render_template

app = Flask(__name__)

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = jogo('The Sims', 'Simulação de vida', ' PC')
jogo2 = jogo('Minecraft','Sobrevivência', 'PC' )
jogo3 = jogo('Pou','Bicho Virtual', 'Celular' )
jogo4 = jogo('Detroit: Become Human','Ação e Aventura', 'PlayStation 4' )

lista = [jogo1, jogo2, jogo3, jogo4]

@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo= 'Meus jogos', jogos= lista)
    
@app.route('/novo')
def novo():
    return render_template('novo.html',titulo= 'titulo')
app.run()

