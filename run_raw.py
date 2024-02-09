from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

#iniciando um servido flask
app = Flask(__name__)

#Ao criar pastas criar um arquivo __init__.py, para import e export
"""
ele pega os métodos post que são requeridos para o servidor 
(como um post para uma api) e cria aqui uma tag bar da variavel product_code
"""

@app.route('/create_tag', methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get('product_code')

    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    return jsonify({ "tag path": path_from_tag})


#o host 0.0.0.0 indica que é localhost
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
