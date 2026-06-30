#  Sistema de Controle de Produção em Python

Este projeto é um sistema simples de **controle de produção** desenvolvido em Python.  
Ele permite registrar a quantidade de peças produzidas, calcular a taxa de defeito, classificar o desempenho e gerar relatórios em **CSV** e **gráficos**.

---

##  Funcionalidades
- Entrada de dados do operador e produção.
- Validação de informações (quantidade produzida e defeituosa).
- Cálculo de peças boas, taxa de defeito e desempenho.
- Geração de relatório no terminal.
- Salvamento automático em **CSV**.
- Criação de **gráfico de desempenho** com `matplotlib`.
- Página HTML para visualização via **GitHub Pages**.

---

##  Estrutura do Projeto

controle-producao/
│
├── main.py                # Código principal
├── relatorio_producao.csv # Histórico de produção
├── grafico_producao.png   # Gráfico gerado
├── index.html             # Página para GitHub Pages
└── README.md              # Documentação do projeto



---

##  Instalação e Uso

### 1. Clone o repositório
```bash
git clone  https://github.com/Ytilonascimento/controle-producao.git
cd controle-producao

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

matplotlib


python main.py

##  Demonstração Online
O gráfico gerado pelo sistema pode ser visualizado em:
[Acesse aqui]

(https://ytilonascimento.github.io/controle-producao/)

##  Como testar localmente
1. Baixe o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt


python main.py



