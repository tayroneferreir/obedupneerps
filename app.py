from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64


app = Flask(__name__)





@app.route('/')
def Login():
    return render_template('login.html')
    

@app.route('/home')
def Home():
    return render_template('index.html')


@app.route('/dados')
def Dados():
    data = {
        'Ano': [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1],
        'Ingressos': [30, 27, 31, 28, 30, 34, 33, 39, 34, 33, 26]
    }
    df = pd.DataFrame(data)

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.plot(df['Ano'], df['Ingressos'], marker='o')  # Plota o gráfico de linha
    plt.title('Ingressos no curso Noturno')  # Define o título do gráfico
    plt.xlabel('Ano')  # Define o rótulo do eixo x
    plt.ylabel('Ingressos')  # Define o rótulo do eixo y
    plt.grid(True)  # Adiciona uma grade ao gráfico


    # Salva o gráfico em um objeto BytesIO
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_b64 = base64.b64encode(img.getvalue()).decode()

    categorias = ['Casado', 'Solteiro', 'Divorciado', 'Não declarado']
    valores = [2, 24, 7, 19]

    # Criando o gráfico de barras
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.bar(categorias, valores)  # Cria o gráfico de barras
    plt.title('Estado Civil em 2022')  # Define o título do gráfico
    plt.xlabel('Categorias')  # Define o rótulo do eixo x
    plt.ylabel('Valores')  # Define o rótulo do eixo y

    # Salva o gráfico em um objeto BytesIO
    img_bar = io.BytesIO()
    plt.savefig(img_bar, format='png')
    img_bar.seek(0)
    img_bar_b64 = base64.b64encode(img_bar.getvalue()).decode()

    # Renderiza o template HTML
    return render_template('dados.html', img_data=img_b64, img_bar=img_bar_b64)


@app.route('/contatos')
def Contatos():

    
    return render_template('contatos.html')

if __name__ == "__main__":
    app.run(debug=True)