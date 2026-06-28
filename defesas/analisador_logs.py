import time

# Simulação de um arquivo de LOG do servidor (histórico de tentativas de acesso)
# Cada linha registra o IP de origem e se o login foi um sucesso ou uma falha
historico_logs = [
    {"ip": "192.168.1.10", "status": "sucesso"},
    {"ip": "10.0.0.5", "status": "falha"},
    {"ip": "10.0.0.5", "status": "falha"},
    {"ip": "10.0.0.5", "status": "falha"}, # Terceira falha seguida!
    {"ip": "192.168.1.15", "status": "sucesso"},
    {"ip": "10.0.0.5", "status": "falha"}, # Quarta falha!
    {"ip": "200.50.10.2", "status": "sucesso"}
]

# Configuração de Segurança: Máximo de falhas permitidas antes de considerar um ataque
LIMITE_FALHAS = 3

print("--- INICIANDO MONITORAMENTO DE SEGURANÇA (BLUE TEAM) ---")
print("Analisando registros de tráfego em tempo real...\n")
time.sleep(1.0)

# Dicionário para contar quantas falhas cada IP cometeu
contador_falhas = {}

# O robô de defesa analisa linha por linha do histórico
for registro in historico_logs:
    ip_atual = registro["ip"]
    status_atual = registro["status"]
    
    if status_atual == "falha":
        # Adiciona 1 ao contador de falhas daquele IP específico
        contador_falhas[ip_atual] = contador_falhas.get(ip_atual, 0) + 1
        
        # Sistema de Alerta Crítico (SIEM/IDS)
        if contador_falhas[ip_atual] >= LIMITE_FALHAS:
            print(f"🚨 [ALERTA DE INCIDENTE] Possível ataque de força bruta detectado!")
            print(f"🛑 Ação Recomendada: Bloquear imediatamente o IP [{ip_atual}] no Firewall.")
            print(f"📊 Detalhes: Este IP acumulou {contador_falhas[ip_atual]} tentativas inválidas de acesso.\n")
    else:
        # Se o login foi um sucesso, o tráfego segue normal
        print(f"🔒 Tráfego Normal: Usuário autenticado com sucesso a partir do IP [{ip_atual}].")

print("--- ANÁLISE DE LOGS CONCLUÍDA COM SUCESSO ---")
