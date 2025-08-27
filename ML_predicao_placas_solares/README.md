<div align="center">
  <img src="../imags/solar_drive.png" alt="Banner do Projeto Solar Drive"/>
</div>

# Machine Learning de Predição de Placas Solares

---

Esta pasta contém uma das minhas partes da solução para o projeto <strong>Solar Drive</strong>, focada no desenvolvimento e na implementação de modelos de Machine Learning para análise de painéis solares flexíveis em veículos elétricos.

A solução consiste em uma API em Python que utiliza dois modelos principais para fornecer insights sobre o desempenho dos painéis solares com base em condições climáticas.

## Desenvolvimento do Projeto
<p>
  O arquivo <code>global.ipynb</code> é um <strong>Jupyter Notebook</strong> que documenta todo o processo de desenvolvimento e análise dos modelos de Machine Learning. Nele, você pode encontrar:
</p>
<ul>
  <li>A descrição detalhada do projeto e dos objetivos.</li>
  <li>As fontes de dados utilizadas.</li>
  <li>As etapas de organização e análise dos dados.</li>
  <li>O treinamento e a avaliação dos modelos de regressão e clusterização.</li>
  <li>A criação e a interpretação dos gráficos que visualizam a relação entre as variáveis.</li>
  <li>O salvamento dos modelos em formato <code>.pkl</code> para uso na API.</li>
</ul>

---

## Modelos Utilizados
<ul>
  <li>
    <strong>Modelo de Regressão Linear</strong> (<code>regression_model.pkl</code>)
    <ul>
      <li><strong>Função:</strong> Prever a eficiência de geração de energia dos painéis solares.</li>
      <li><strong>Treinamento:</strong> O modelo foi treinado com dados meteorológicos (temperatura, umidade, velocidade do vento, visibilidade e pressão) e dados simulados de produção de energia, incluindo "ruído" para se aproximar de condições reais.</li>
    </ul>
  </li>
  <li>
    <strong>Modelo de Clusterização</strong> (<code>cluster_model.pkl</code>)
    <ul>
      <li><strong>Função:</strong> Classificar as condições meteorológicas em clusters distintos.</li>
      <li><strong>Treinamento:</strong> O modelo K-Means foi utilizado para segmentar os dados em 3 clusters, que representam três cenários climáticos principais:
        <ol>
          <li><strong>Cluster 0:</strong> Condições quentes e secas.</li>
          <li><strong>Cluster 1:</strong> Condições intermediárias.</li>
          <li><strong>Cluster 2:</strong> Condições frias e úmidas.</li>
        </ol>
      </li>
    </ul>
  </li>
</ul>

---

## Estrutura do Repositório
<pre><code>ML_predicao_placas_solares/
|
|-- app/
|    `-- main.py       # API Flask para servir os modelos
|-- regression_model.pkl # Modelo de regressão (salvo com joblib)
|-- cluster_model.pkl    # Modelo de clusterização (salvo com joblib)
|-- index.html           # Arquivo interativo para testar a API
`-- global.ipynb         # Notebook Jupyter com o desenvolvimento e análise dos modelos
</code></pre>

---

## Como Executar a API

<p>Para rodar a API localmente, siga os passos abaixo.</p>

<ol>
  <li>
    <strong>Pré-requisitos:</strong> Certifique-se de que você tem o <code>Python</code> instalado. Em seguida, instale as bibliotecas necessárias:
    <pre><code>pip install Flask flask_cors scikit-learn joblib numpy</code></pre>
  </li>
  <li>
    <strong>Ajuste Necessário no Código da API:</strong>
    <p>O arquivo <code>app/main.py</code> está configurado com um caminho local para os modelos. Antes de rodar, <strong>você deve corrigir o caminho</strong>.</p>
    <p>Abra o arquivo <code>app/main.py</code> e altere as linhas de carregamento dos modelos para usar caminhos relativos, apontando para os arquivos na pasta principal:</p>
    <pre><code># Carregar os modelos salvos
regression_model = joblib.load("../regression_model.pkl")
cluster_model = joblib.load("../cluster_model.pkl")
</code></pre>
  </li>
  <li>
    <strong>Executar o Servidor Flask:</strong> Navegue até a pasta <code>app</code> e inicie o servidor:
    <pre><code>cd app
python main.py
</code></pre>
    <p>A API será iniciada e estará disponível em <code>http://127.0.0.1:5000</code>.</p>
  </li>
</ol>

---

## Como Testar a API com `index.html`

<p>O arquivo <code>index.html</code> oferece uma interface simples para interagir com a API sem a necessidade de ferramentas externas como o Postman.</p>

<ol>
  <li>
    <strong>Abrir o <code>index.html</code>:</strong> Simplesmente abra o arquivo <code>index.html</code> em seu navegador web.
  </li>
  <li>
    <strong>Prever Eficiência:</strong> Use o formulário <strong>"Prever Eficiência"</strong> para inserir os dados meteorológicos e ver a previsão de produção de energia.
  </li>
  <li>
    <strong>Identificar Cluster:</strong> Use o formulário <strong>"Identificar Cluster"</strong> com os mesmos dados para descobrir em qual categoria climática as condições se encaixam e qual a descrição correspondente.
  </li>
</ol>

<p>A seção <strong>"Sugestões"</strong> na página HTML fornece valores de exemplo para cada cluster, o que facilita o teste rápido dos modelos.</p>
