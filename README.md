# Monitoramento-de-Primatas-2023
# Monitoramento de Primatas

O projeto **Monitoramento de Primatas** é uma iniciativa conjunta entre a **Universidade Unifeso** e pesquisadores do **Parque Nacional**, que visa rastrear e analisar o comportamento dos primatas na região. Através de tecnologias de **Geoprocessamento** e **Machine Learning**, o projeto monitora o deslocamento dos animais e prevê suas chances de sobrevivência, contribuindo para estudos de conservação ambiental.

### Funcionalidades:
- **Monitoramento Espacial**: geração de coordenadas geográficas e visualização do deslocamento dos primatas em mapas interativos.
- **Análise de Agrupamento**: aplicação do algoritmo **K-Means** para identificar padrões de movimentação e comportamento dos indivíduos.
- **Previsão de Sobrevivência**: uso do modelo **K-Nearest Neighbors (KNN)** para avaliar fatores como idade, peso, sexo e exposição a áreas urbanas.

### Tecnologias Utilizadas:
- Linguagem: **Python**
- Bibliotecas: `geopandas`, `pandas`, `numpy`, `folium`, `matplotlib`, `seaborn`, `sklearn`

### Como Executar:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-repositorio.git


Instale as dependências:
pip install -r requirements.txt

Execute o monitoramento dos primatas:
python monitoramento_primatas.py

Execute a previsão de sobrevivência:
python previsao_sobrevivencia.py
