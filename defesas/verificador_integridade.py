import hashlib
import time

# Simulação do banco de dados de segurança com as "impressões digitais" (Hashes) originais dos arquivos do site
# O hash SHA-256 funciona como uma identidade digital imutável
hashes_originais_seguros = {
    "index.html": "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e",
    "config.php": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7",
    "login.py": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
}

# Simulação do estado atual dos arquivos (um hacker invadiu e alterou o arquivo de login para roubar senhas!)
# Note que o hash do 'login.py' mudou completamente por causa da alteração maliciosa
arquivos_atuais_no_servidor = {
    "index.html": "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e", # Intacto
    "config.php": "87428fc522803d31065e7bce3cf03fe475096631e5e07bbd7a0fde60c4cf25c7", # Intacto
    "login.py": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"   # FOI ALTERADO!
}

print("--- INICIANDO MONITORAMENTO DE INTEGRIDADE DE ARQUIVOS (BLUE TEAM) ---")
print("Analisando assinaturas digitais do sistema contra modificações não autorizadas...\n")
time.sleep(1.0)

# O robô de defesa compara cada arquivo atual com o histórico seguro
for nome_arquivo, hash_atual in arquivos_atuais_no_servidor.items():
    
    # Verifica se o arquivo é conhecido pelo sistema de segurança
    if nome_arquivo in hashes_originais_seguros:
        hash_original = hashes_originais_seguros[nome_arquivo]
        
        # Compara as impressões digitais
        if hash_atual == hash_original:
            print(f"🔒 Seguro: O arquivo [{nome_arquivo}] está íntegro e autêntico.")
        else:
            print(f"🚨 [ALERTA CRÍTICO] Violação de Integridade Detectada!")
            print(f"💥 O arquivo [{nome_arquivo}] foi modificado secretamente ou infectado por malware!")
            print(f"📊 Hash Original: {hash_original}")
            print(f"📊 Hash Modificado: {hash_atual}\n")
    else:
        print(f"⚠️ Atenção: Arquivo desconhecido ou suspeito encontrado no servidor: [{nome_arquivo}]")

print("\n--- AUDITORIA DE INTEGRIDADE CONCLUÍDA ---")
