Descrição do Projeto

Este projeto consiste em um MVP de um sistema inteligente baseado em Lógica Fuzzy para calcular automaticamente a potência recomendada de um ar-condicionado, considerando:

Temperatura ambiente (°C)

Umidade relativa (%)

Ele inclui:

✔ Módulo Inteligente (IA Fuzzy)
✔ Interface Web (Streamlit)
✔ Dashboard com gráficos e logs
✔ Mini API integrada
✔ Sistema de armazenamento de dados (CSV)

O objetivo é demonstrar o uso de Inteligência Artificial aplicada ao controle de conforto térmico de forma simples, acessível e funcional.

🧠 Como o Sistema Inteligente Funciona

A lógica fuzzy faz a inferência de forma aproximada, usando regras do tipo:

SE temperatura é alta E umidade é alta → potência é alta

SE temperatura é baixa E umidade é baixa → potência é baixa

O módulo de IA recebe valores contínuos de temperatura e umidade, aplica:

Fuzzificação

Aplicação das regras fuzzy

Inferência

Defuzzificação

E retorna uma potência entre 0% e 100%.

Arquivo responsável:
📌 fuzzy_controller.py

🖥️ Tecnologias Utilizadas
🔹 Linguagens e Bibliotecas

Python 3.10+

scikit-fuzzy — motor fuzzy principal

NumPy

Streamlit — interface web e dashboard

Pandas — manipulação de logs

CSV — armazenamento de histórico

🔹 Arquitetura

IA encapsulada em um módulo Python (fuzzy_controller.py)

Interface + API integradas em app.py

Logs armazenados em logs.csv

Arquitetura limpa e modular

📁 Estrutura do Projeto
fuzzy-ac-controller/
│── app.py                 # Interface web + Dashboard + API
│── fuzzy_controller.py    # Motor Fuzzy (IA)
│── logs.csv               # Logs gerados automaticamente
│── .venv/                 # Ambiente virtual isolado
│── README.md              # ESTE documento

⚙️ Como Rodar o Projeto
1️⃣ Clonar o repositório (se estiver usando GitHub)
git clone https://github.com/seu_usuario/fuzzy-ac-controller
cd fuzzy-ac-controller

2️⃣ Criar o ambiente virtual

No Windows:

python -m venv .venv


Ativar:

.venv\Scripts\activate

3️⃣ Instalar dependências
pip install -r requirements.txt


Se não tiver o requirements.txt, instale manualmente:

pip install scikit-fuzzy numpy streamlit pandas

4️⃣ Rodar o sistema
streamlit run app.py


Abrirá automaticamente em:

http://localhost:8501

🕹️ Como Usar o Sistema
✔ Ajuste a temperatura pelo slider
✔ Ajuste a umidade pelo slider
✔ O sistema calcula automaticamente a potência ideal
✔ Dashboard atualiza em tempo real:

Gráfico da potência

Tabela com logs

Métricas atuais

✔ API integrada

Você pode chamar a IA pela URL:

http://localhost:8501/?temp=30&umid=70


Retorno:

{
  "temperatura": 30,
  "umidade": 70,
  "potencia": 82.3
}

📊 Geração de Logs

Cada interação do usuário é salva automaticamente em:

logs.csv


O arquivo contém:

timestamp

temperatura

umidade

potência calculada

Ideal para o capítulo de Estudo Experimental e Resultados.

🧪 Testes

Para testar com valores fixos:

from fuzzy_controller import compute_power
print(compute_power(30, 70))

🏁 Conclusão

Este projeto demonstra:

Um sistema inteligente funcional

IA real utilizando lógica fuzzy

Interface moderna e fácil de usar

API integrável

Dashboard com histórico

Estrutura perfeita para um MVP acadêmico

📎 Autor

Arthur Konzen
UTFPR — Sistemas Inteligentes Aplicados
