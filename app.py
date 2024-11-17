from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    imc = None
    mensagem = ""
    dicas = []
    nome = None  # Variável para armazenar o nome
    if request.method == "POST":
        try:
            # Obtemos os dados do formulário
            nome = request.form.get("nome", "Usuário")
            peso_input = request.form.get("peso", "0")
            altura_input = request.form.get("altura", "0")
            
            # Substituímos a vírgula por ponto para suportar ambos
            peso = float(peso_input.replace(",", "."))
            altura = float(altura_input.replace(",", "."))

            if peso > 0 and altura > 0:
                imc = round(peso / (altura ** 2), 2)

                if imc < 18.5:
                    mensagem = f"{nome}, você está abaixo do peso"
                    dicas = [
                        "Inclua mais alimentos ricos em proteínas e carboidratos saudáveis na sua dieta.",
                        "Consulte um nutricionista para criar um plano alimentar adequado.",
                        "Pratique exercícios para ganhar massa muscular de forma saudável."
                    ]
                elif 18.5 <= imc < 24.9:
                    mensagem = f"{nome}, seu peso está normal"
                    dicas = [
                        "Parabéns! Continue mantendo um estilo de vida equilibrado.",
                        "Pratique exercícios regularmente para manter a saúde em dia.",
                        "Consuma uma dieta variada com todos os grupos alimentares."
                    ]
                elif 25 <= imc < 29.9:
                    mensagem = f"{nome}, você está com sobrepeso"
                    dicas = [
                        "Tente reduzir o consumo de alimentos ultraprocessados.",
                        "Adicione mais frutas, legumes e alimentos ricos em fibras à sua dieta.",
                        "Aumente a frequência de atividades físicas em sua rotina."
                    ]
                else:
                    mensagem = f"{nome}, você está obeso"
                    dicas = [
                        "Adote uma dieta equilibrada com orientação profissional.",
                        "Evite açúcares, gorduras saturadas e alimentos ultraprocessados.",
                        "Inclua exercícios físicos regulares, como caminhadas ou natação.",
                        "Consulte um médico para acompanhamento de saúde."
                    ]
            else:
                mensagem = "Por favor, insira valores válidos para peso e altura."
        except ValueError:
            mensagem = "Por favor, insira valores válidos."

    return render_template("index.html", imc=imc, mensagem=mensagem, dicas=dicas, nome=nome)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
