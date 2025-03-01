import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
from matplotlib.colors import LinearSegmentedColormap  # 🔹 Importação correta!

def generate_multicolor_line_chart(df):
    """
    Gera um gráfico de linha com gradiente de cores suaves usando a paleta do TikTok.
    """

    print("🔍 Verificando os dados antes de gerar o gráfico...")
    print(df.head())  # Exibe as 5 primeiras linhas do DataFrame

    if df.empty:
        print("⚠️ O DataFrame está vazio. Nenhum gráfico será gerado.")
        return

    x = np.linspace(0, len(df) - 1, len(df) * 10)  # 🔥 Mais pontos para suavizar as curvas
    y_original = df["retention_rate"].fillna(0)  # Substitui valores NaN por 0

    # **Interpolação para criar curvas suaves**
    spline = scipy.interpolate.CubicSpline(np.arange(len(df)), y_original)
    y = spline(x)  # Calcula os novos pontos suavizados

    # 🎨 **Criando um gradiente contínuo com as cores do TikTok**
    tiktok_colors = ["#69C9D0", "#EE1D52", "#FFFFFF"]  # Ciano, Vermelho Neon, Branco
    cmap = LinearSegmentedColormap.from_list("TikTok", tiktok_colors, N=256)  # 🔹 Correção aplicada!

    norm = plt.Normalize(vmin=min(y), vmax=max(y))
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    fig, ax = plt.subplots(figsize=(10, 5))

    # 🔥 **Desenha a linha suavizada com gradiente TikTok**
    for i in range(len(x) - 1):
        ax.plot(x[i:i+2], y[i:i+2], color=cmap(norm(y[i])), linewidth=2)

    # 📌 **Adicionar a barra de cores**
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label("Retenção (%)")  # Nome da escala de cores

    # 🎯 **Configuração dos eixos**
    ax.set_title("Taxa de Retenção do TikTok")
    ax.set_xlabel("Vídeos")
    ax.set_ylabel("Taxa de Retenção (%)")

    if "title" in df.columns:
        ax.set_xticks(np.linspace(0, len(df) - 1, len(df)))
        ax.set_xticklabels(df["title"], rotation=45, ha="right")

    plt.show(block=True)
    print("📊 Gráfico gerado com sucesso com paleta do TikTok e mais vídeos!")
