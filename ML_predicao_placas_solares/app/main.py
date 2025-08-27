from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS
import joblib
import numpy as np

# Carregar os modelos salvos
regression_model = joblib.load(r"..\regression_model.pkl")
cluster_model = joblib.load(r"..\cluster_model.pkl")

# Mapeamento dos clusters para as condições que eles representam
cluster_descriptions = {
    0: "Condições quentes e secas, favoráveis para eficiência solar.",
    1: "Condições intermediárias, com eficiência moderada.",
    2: "Condições frias e úmidas, menos favoráveis para eficiência solar."
}

# Inicializar o aplicativo Flask
app = Flask(__name__)
CORS(app)  # Ativar suporte a CORS

# Endpoint para prever eficiência (regressão)
@app.route("/prever-eficiencia", methods=["POST"])
def prever_eficiencia():
    try:
        # Receber dados do JSON enviado pelo cliente
        dados = request.get_json()
        caracteristicas = np.array([
            [
                dados["temperatura_media"],
                dados["umidade_media"],
                dados["velocidade_vento_media"],
                dados["visibilidade_media"],
                dados["pressao_media"]
            ]
        ])

        # Fazer a previsão com o modelo de regressão
        previsao = regression_model.predict(caracteristicas)[0]

        return jsonify({
            "sucesso": True,
            "previsao_eficiencia": f"{previsao:.2f} watts em 15 minutos"
        })
    except Exception as e:
        return jsonify({
            "sucesso": False,
            "erro": str(e)
        })

# Endpoint para identificar o cluster (K-means)
@app.route("/identificar-cluster", methods=["POST"])
def identificar_cluster():
    try:
        # Receber dados do JSON enviado pelo cliente
        dados = request.get_json()
        caracteristicas = np.array([
            [
                dados["temperatura_media"],
                dados["umidade_media"],
                dados["velocidade_vento_media"],
                dados["visibilidade_media"],
                dados["pressao_media"]
            ]
        ])

        # Fazer a previsão do cluster com o modelo K-means
        cluster = cluster_model.predict(caracteristicas)[0]
        descricao = cluster_descriptions.get(cluster, "Descrição não disponível.")

        return jsonify({
            "sucesso": True,
            "cluster": int(cluster),
            "descricao": descricao
        })
    except Exception as e:
        return jsonify({
            "sucesso": False,
            "erro": str(e)
        })

# Rodar o aplicativo Flask
if __name__ == "__main__":
    app.run(debug=True)

