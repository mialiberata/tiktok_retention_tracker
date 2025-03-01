# 🪼 Extração e visualização de métricas do TikTok in real time

Oi, Mia aqui! ≽^• ˕ • ྀི≼

Se tem uma coisa que me incomoda, é não saber **por que um vídeo viraliza e outro não**. Como o tempo de retenção afeta o desempenho no TikTok? Como visualizar isso de forma clara? Como automatizar tudo e evitar trabalho manual? Bom, resolvi criar este projeto para **coletar, processar e visualizar** esses dados com Python. E ficou melhor do que eu imaginava!

---

## **🧐 O que esse projeto faz?**

Este código ajuda criadores de conteúdo e analistas a **entender o desempenho de seus vídeos no TikTok**. Ele:

- 👉 Se conecta à API do TikTok (ou simula dados falsos, caso você não tenha API Key);
- 👉 Baixa e processa os dados de retenção dos vídeos;
- 👉 Filtra quem assistiu menos de 3 segundos;
- 👉 Cria **gráficos estilosos** para comparar vídeos que performaram bem vs. os que floparam;
- 👉 Exporta relatórios em CSV e PDF para uma análise mais detalhada.

---

## **🧩 Estrutura do Projeto**

```bash
📁 tiktok_metrics_pipeline/
├── 📄 config.json            # Onde você insere sua API Key do TikTok
├── 📄 main.py               # O código principal que faz tudo funcionar
├── 📄 generate_fake_data.py # Gera dados fictícios para testes
├── 📄 visualization.py      # Gera gráficos bonitos das métricas
├── 📄 export.py            # Exporta relatórios em CSV/PDF
├── 📄 README.md            # A explicação linda desse projeto
```

---

## **(っº - ºς) Como esse projeto foi pensado?**

Eu queria um jeito **fácil e visual** de entender os dados de retenção do TikTok. A ideia foi dividir o processo em **4 partes principais:**

### **1️⃣ Extração de Dados**

✅ Conectar com a API do TikTok para coletar os dados de visualização.
✅ Filtrar quem assistiu menos de 3 segundos.
✅ Pegar métricas como visualizações totais, retenção média, taxa de drop-off.

### **2️⃣ Processamento e Análise**

✅ Limpar os dados e calcular as métricas de retenção.
✅ Criar um DataFrame bonitinho com pandas para organizar os insights.

### **3️⃣ Visualização de Dados**

✅ Criar gráficos usando Matplotlib.
✅ Comparar vídeos que performaram bem vs. os que floparam.
✅ Gerar um relatório automatizado e exportar em PDF/CSV.

### **4️⃣ Automção & Deploy**

✅ Fazer o script rodar periodicamente (schedule, cron job, ou workflow do GitHub).
✅ Subir no GitHub com README e um exemplo de saída.

---

## **⋆⭒˚.⋆🪐 ⋆⭒˚.⋆ O que tem de especial nesse projeto?**

🎨 **Visualização Personalizada:**

- Usei **gradientes dinâmicos** com as cores do **TikTok** para criar um gráfico bonito e intuitivo.
- As linhas têm **curvas suaves** para melhorar a legibilidade dos dados.
- Adicionei uma **barra de cores** para indicar a taxa de retenção.

🚀 **Automatização Total:**

- O código pode rodar sozinho sem precisar de ajustes manuais.
- Se você não tiver API Key do TikTok, ele **gera dados falsos automaticamente** para testes.

---

## **🔧 Como rodar o projeto?**

1️⃣ **Instale as dependências:**

```bash
pip install -r requirements.txt
```

2️⃣ **Edite o ************************************************************`config.json`************************************************************ e adicione sua API Key** (se tiver acesso à API do TikTok).

3️⃣ **Execute o script:**

```bash
python main.py
```

4️⃣ **Veja os relatórios:**

- O gráfico será gerado automaticamente e exibido na tela.
- Um arquivo CSV (`relatorio_tiktok.csv`) e um PDF (`relatorio_tiktok.pdf`) serão salvos.

---

## **🐾 Próximos passos**

✅ Criar um dashboard interativo no **Streamlit**.
✅ Permitir que o usuário escolha diferentes paletas de cores.
✅ Adicionar mais insights sobre tempo médio de visualização.
✅ Criar um sistema de predição para prever quais vídeos podem bombar.

---

Dúvidas, feedbacks ou surtos? Deixe seu recado após o bocejo: /ᐠ - ˕ -マ ᶻ 𝗓 𐰁

