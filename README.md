🌡️ Sistema Inteligente de Controle de Ar-Condicionado (IA Fuzzy)

Este projeto consiste em um MVP de um sistema inteligente baseado em Lógica Fuzzy capaz de calcular automaticamente a potência ideal de um ar-condicionado considerando:

🌡 Temperatura ambiente (°C)

💧 Umidade relativa do ar (%)

O sistema inclui:

🧠 Módulo de IA Fuzzy

🖥️ Interface Web completa (Streamlit)

📊 Dashboard com gráficos e histórico

🌐 Mini API integrada

📝 Registro automático de logs (CSV)

O objetivo é demonstrar o uso prático de Inteligência Artificial aplicada ao conforto térmico em um MVP simples, claro e totalmente funcional.

🧠 Como o Sistema Inteligente Funciona

A lógica fuzzy permite decisões aproximadas utilizando regras linguísticas — ideal para problemas contínuos como controle térmico.

Exemplos de regras fuzzy utilizadas:

SE temperatura é alta E umidade é alta → potência alta

SE temperatura é baixa E umidade é baixa → potência baixa

SE temperatura é média E umidade é alta → potência média/alta

O sistema realiza automaticamente:

Fuzzificação

Aplicação das regras fuzzy

Inferência

Defuzzificação

Resultado final (0% a 100%)

📌 Arquivo responsável pela IA:
fuzzy_controller.py

🛠️ Tecnologias Utilizadas
🔹 Linguagem & Bibliotecas (Python)

Python 3.10+

scikit-fuzzy — motor fuzzy principal

numpy

pandas

matplotlib

streamlit — interface web

🔹 Arquitetura do Projeto

IA encapsulada no módulo: fuzzy_controller.py

Interface + API em: app.py

Logs salvos em: logs.csv

Ambiente virtual isolado: .venv/

Tudo organizado de forma modular e didática.

📁 Estrutura do Projeto
fuzzy-ac-controller/
│── app.py                # Interface web + Dashboard + API
│── fuzzy_controller.py   # Lógica Fuzzy (IA)
│── logs.csv              # Histórico gerado automaticamente
│── requirements.txt      # Dependências instaláveis
│── .venv/                # Ambiente virtual (opcional)
│── README.md             # Documentação

⚙️ Como Rodar o Projeto (Passo a Passo Completo)
🔽 1. Clonar o repositório
git clone https://github.com/arthurkonzen/fuzzy-ac-controller
cd fuzzy-ac-controller

🧰 2. Criar um Ambiente Virtual
✔ Windows:
python -m venv .venv
.venv\Scripts\activate

✔ Linux / Mac:
python3 -m venv .venv
source .venv/bin/activate

📦 3. Instalar Dependências
Instalar usando requirements.txt
pip install -r requirements.txt

Ou instalar manualmente:
pip install scikit-fuzzy numpy streamlit pandas matplotlib

🚀 4. Executar o Sistema
streamlit run app.py


A aplicação abrirá automaticamente em:

👉 http://localhost:8501

🕹️ Como Usar o Sistema
✔ 1. Ajuste os sliders:

Temperatura (°C)

Umidade (%)

✔ 2. O sistema calcula automaticamente:

Potência (%) ideal do ar-condicionado

Recomendação textual (sucesso, alerta ou crítico)

✔ 3. Dashboard inclui:

📈 Gráfico da potência

📋 Tabela com todas as medições

📜 Logs armazenados em logs.csv

🔗 Demo da API integrada

🌐 API Integrada (via Streamlit)

Acessar diretamente via navegador:

http://localhost:8501/?temp=30&umid=70


Resposta JSON:

{
  "temperatura": 30,
  "umidade": 70,
  "potencia": 82.3
}


Perfeito para integração com sistemas externos ou sensores.

📊 Logs Automáticos (logs.csv)

Cada interação gera um registro contendo:

Timestamp

Temperatura inserida

Umidade inserida

Potência calculada

Exemplo de uso (para capítulos de resultados):

2025-12-09 17:40:21, 30, 70, 82.38
2025-12-09 17:41:10, 25, 50, 45.00

🧪 Testes Diretos no Python
from fuzzy_controller import compute_power

print(compute_power(30, 70))  # Exemplo de teste

🏁 Conclusão

Este MVP demonstra:

✔ Um sistema inteligente funcional

✔ IA fuzzy real aplicada ao controle térmico

✔ Interface web moderna e simples

✔ Dashboard para visualização e análise

✔ API embutida para integração

✔ Estrutura modular e profissional

Projeto ideal para fins acadêmicos e demonstração de conceitos de IA aplicada.

👥 Autores

Arthur Botelho Konzen
Ítalo Kaique Bueno
UTFPR – Sistemas Inteligentes Aplicados

🔗 Repositório

👉 https://github.com/arthurkonzen/fuzzy-ac-controller
