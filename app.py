#criando servidor

#pelo request da pra saber o method que foi usado
from flask import Flask, render_template, request


app = Flask(__name__, template_folder="./src/views") 

#se o usuario clicar na pagina principal retorna a mensagem ola mundo
#render_template = para renderizar uma página
#o render template, por padrao procura a pasta templates. abrir uma pasta com esse nome e criar index.html
#caso queira deixar o index.html em outro lugar, passar o parametro template_folder="caminho"
#por padrao a sinxtate é get, não precisaria passar
#O GET por ser um array pode receber mais verbos
@app.route("/", methods=["GET", "POST", "DELETE", "UPDATE"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"]!="" or request.form["num2"]!=""):
            if(request.form["opc"] == "soma"):
                soma = int(request.form["num1"]) + int(request.form["num2"])
                return {
                    "Resultado": str(soma) #retornar em json
                }
            elif (request.form["opc"] == "subt"):
                subt = int(request.form["num1"]) - int(request.form["num2"])
                return {
                    "Resultado":str(subt)
                }
            elif (request.form["opc"] == "mult"):
                mult = int(request.form["num1"]) * int(request.form["num2"])
                return {
                    "Resultado":str(mult)
                }
            elif (request.form["opc"] == "div"):
                div = int(request.form["num1"]) / int(request.form["num2"])
                return {
                    "Resultado":str(div) 
                }
        else:
            return "Informe um valor válido"

#@app.route("/", methods=["POST"])
#def sobre():
#    return "POST"

#É possivel usar o error para definir rotas
#()parametro do erro. exemplo 404
#é possivel renderizar uma página para o erro ex: error.html
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

#caso tente usar um verbo que não foi passado no parametro a cima
@app.errorhandler(405)
def not_found2(error):
    return "Verbo não existe"

@app.route("/<int:id>")
def home_id(id):
    return str(int(id) +1)
#parametro passado pela url. Ele não aceita numero. é necessário transformar em string se necessário
#str(int(id) +1) = str(string) transformado a soma de inteiros em string

# app.run() = define a porta padrao que vai ser exibida(5000)
#caso queira passar outra porta, app.run(port=8080)
#para fazer a mudanca de porta, para a aplicação com ctr c e reiniciar a aplicação
#debug = parametro para atualizar terminal e exibir na nova porta

app.run(port=8080, debug=True)




#paycache armazena o cache, se apar funciona do mesmo jeito

