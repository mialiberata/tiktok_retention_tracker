import random

def generate_fake_data():
    """Gera dados fictícios para simular a API do TikTok"""
    
    videos = []
    
    for i in range(10):  # 🔥 Agora temos 10 vídeos!
        if i < 3:
            # 🎯 3 vídeos com baixa retenção
            views = random.randint(5000, 15000)
            views_below_3s = int(views * random.uniform(0.6, 0.8))  # 60% a 80% das views abaixo de 3s
        else:
            # 🎯 7 vídeos com retenção alta
            views = random.randint(10000, 30000)
            views_below_3s = int(views * random.uniform(0.1, 0.3))  # Apenas 10% a 30% abaixo de 3s

        videos.append({
            "id": f"v{i+1}",
            "title": f"Vídeo {i+1}",
            "views": views,
            "views_below_3s": views_below_3s
        })

    return {"videos": videos}
