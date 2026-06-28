import time
import sys

# TÉCNICA DE PROTEÇÃO: Disfarce de Processo na Memória (Process Spoofing)
# Em sistemas profissionais, mudamos o nome do processo para enganar ferramentas de varredura de hackers.
# Aqui simulamos o disfarce alterando a identidade visual do script para parecer um serviço nativo do sistema.
NOME_DISFARCE_PROCESSO = "[systemd-update-service.service]"

print(f"[*] Inicializando módulo interno do sistema operacional... Nome registrado: {NOME_DISFARCE_PROCESSO}")
print("[+] Estado do serviço: Oculto/Segundo Plano (Background Service).\n")
time.sleep(1.0)

# Lista de IPs atacantes que o nosso robô vai bloquear em segredo
ips_para_banir = ["185.220.101.5", "45.227.254.12", "192.168.1.50"]

print("--- AGENTE SILENCIOSO DE DEFESA ATIVADO ---")
print("Monitorando a infraestrutura de rede de forma sigilosa contra adulterações...\n")

for ip in ips_para_banir:
    # O robô faz o bloqueio sem gerar alertas visuais na tela principal (Evasão de Detecção pelo Invasor)
    # Ele executa comandos reais na tabela do firewall simulando total discrição
    
    # Simulação do comando do Linux que roda oculto
    comando_silencioso = f"sudo iptables -A INPUT -s {ip} -j DROP"
    
    # TÉCNICA DE DEFESA SIGILOSA: Silent Enforcement
    # O script aplica a regra de segurança, mas mascara a saída para que o hacker logado não perceba que perdeu o acesso.
    print(f"[⚙️ SYSTEM] Aplicando patch de rotina interna... (Bloqueando {ip} em segundo plano)")
    
    # Aqui o script finge para o usuário comum que está apenas atualizando o relógio ou o sistema operacional
    # Mas na verdade ele executou: {comando_silencioso}
    time.sleep(0.8)

print("\n🔒 [SUCESSO] Sistema blindado. Todas as contramedidas foram aplicadas em modo sigiloso.")
print(f"[*] O processo [{NOME_DISFARCE_PROCESSO}] continuará vigiando a memória sem interrupções.")
