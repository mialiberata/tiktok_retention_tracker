import json
import requests
import pandas as pd
from generate_fake_data import generate_fake_data  # Importa módulo de dados fictícios
from visualization import generate_multicolor_line_chart  # Importa o gráfico corrigido
from export import export_csv, export_pdf  # Importa módulo de exportação

# 📌 **Carregar Configuração**
CONFIG_FILE = "config.json"

def load_config():
    """Carrega configurações do arquivo JSON"""
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("⚠️ Arquivo de configuração não encontrado. Prosseguindo com valores padrão...")
        return {}

config = load_config()
API_KEY = config.get("api_key", "")

# 📌 **Função para buscar dados da API do TikTok**
def get_tiktok_data():
    """Obtém os dados da API do TikTok ou gera dados fictícios caso não haja API Key."""
    if not API_KEY:
        print("⚠️ Nenhuma API Key fornecida. Gerando dados fictícios...")
        return generate_fake_data()
    
    url = "https://api.tiktok.com/metrics/videos"  # Exemplo fictício
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"time_frame": "last_7_days"}  
    
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"⚠️ Erro ao acessar API do TikTok (código {response.status_code}). Gerando dados fictícios...")
            return generate_fake_data()
    except requests.RequestException as e:
        print(f"❌ Erro ao conectar à API: {e}")
        return generate_fake_data()

# 📌 **Processamento dos Dados**
def process_data(data):
    """Converte os dados para DataFrame e calcula a taxa de retenção."""
    if "videos" not in data or not data["videos"]:
        print("⚠️ Nenhum vídeo encontrado nos dados.")
        return pd.DataFrame()  # Retorna DataFrame vazio

    df = pd.DataFrame(data["videos"])

    if "views" in df.columns and "views_below_3s" in df.columns:
        df["retention_rate"] = (1 - (df["views_below_3s"] / df["views"])) * 100  # Converte para porcentagem
        print("✅ Dados processados com sucesso! Exemplo:")
        print(df[["views", "views_below_3s", "retention_rate"]].head())  # Exibe as 5 primeiras linhas
    else:
        print("⚠️ Dados incompletos recebidos. Certifique-se de que a API está retornando corretamente.")
        df["retention_rate"] = 0  # Evita erro caso os dados estejam faltando

    return df

# 📌 **Geração da Visualização**
def generate_visualization(df):
    """Gera um gráfico multicolorido se houver dados disponíveis."""
    if df.empty:
        print("⚠️ Nenhum dado disponível para visualização.")
        return
    
    print("📊 Gerando visualização...")
    generate_multicolor_line_chart(df)  # 🔹 Agora estamos passando `df` corretamente!

# 🚀 **Executando o Pipeline**
def run_pipeline():
    print("🔄 Buscando dados...")
    data = get_tiktok_data()
    df = process_data(data)

    generate_visualization(df)  # 🔹 Garante que `df` é passado corretamente!

    print("📄 Exportando relatórios...")
    export_csv(df)  # Exporta para CSV
    export_pdf(df)  # Exporta para PDF

    print("✅ Pipeline finalizado com sucesso!")

# 📌 **Execução Principal**
if __name__ == "__main__":
    run_pipeline()
