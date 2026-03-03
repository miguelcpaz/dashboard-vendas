# 📊 Dashboard de Vendas em Python

Projeto de análise de vendas desenvolvido em Python utilizando Streamlit para visualização de dados de forma simples e interativa.

O sistema permite importar um arquivo CSV e gerar métricas e gráficos automaticamente com base nos dados enviados.

---

## 🚀 Funcionalidades

- Upload de arquivo CSV  
- Validação de colunas obrigatórias  
- Exibição dos dados brutos  
- Cálculo automático de:
  - Faturamento total  
  - Ticket médio  
  - Produto mais vendido  
- Gráfico de vendas por dia  
- Gráfico de vendas por produto  

---

## 🛠 Tecnologias Utilizadas

- 🐍 Python  
- 🌐 Streamlit  
- 📊 Pandas  
- 📈 Matplotlib  

---

## 📁 Formato do CSV Esperado

O arquivo deve conter no mínimo as seguintes colunas:


Data;Produto;Valor


Exemplo:


2026-01-01;Notebook;3500
2026-01-02;Mouse;120


> Observação: o separador utilizado deve ser `;`

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```
git clone https://github.com/seuusuario/dashboard-vendas-python.git
```

2. Acesse a pasta do projeto:

```
cd dashboard-vendas-python
```

3. Crie o ambiente virtual:

```
python -m venv venv
```

4. Ative o ambiente virtual:

Windows:
```
venv\Scripts\activate
```

5. Instale as dependências:

```
pip install -r requirements.txt
```

6. Execute a aplicação:

```
streamlit run app.py
```

---

## 📌 Objetivo do Projeto

Projeto desenvolvido com foco em prática de:

- Manipulação de dados  
- Visualização gráfica  
- Validação de entrada de dados  
- Estruturação de aplicação com Streamlit  

---

Desenvolvido para fins de estudo e portfólio.
