from src.main.server.server import app

if __name__ == "__main__":
    #debug para que qualquer alteração salva já seja
    #colocada quando o servidor já estiver inicializado
    app.run(host='0.0.0.0', port=3000, debug=True)
