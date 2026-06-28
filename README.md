# 🛡️ Gaveta 2: Meu Kit de Defesa (Proteção de Sistemas)

Este repositório é o meu "guarda-roupa" de ferramentas de **Cibersegurança (Blue Team)**. Aqui eu guardo e organizo robôs digitais que criei em **Python** para vigiar, proteger e blindar computadores e sites contra invasores.

---

## 📂 Estrutura do Repositório

O projeto está estruturado de forma profissional em subpastas para facilitar a navegação:

* 📁 **`defesas/`**: A gaveta principal onde ficam guardados os programas de proteção.
* 📁 **`laboratorio/`**: Contém as instruções completas para montar um ambiente virtual e vulnerável seguro para testes locais.
* 📑 **`README.md`**: Este manual de instruções explicativo (este arquivo).

---

## 🔍 O que meus Robôs de Defesa fazem? (Explicado de Forma Simples)

Como essas ferramentas rodam dentro do nosso próprio servidor, elas não precisam de camuflagem de rede. Elas usam **disfarces invisíveis** na memória para que, caso um hacker invada o sistema, ele não consiga descobrir e desligar as nossas ferramentas de proteção.

### 1. O Vigilante de Registros (`analisador_logs.py`)
Monitora os livros de visitas do servidor. Se um mesmo número de IP errar a senha muitas vezes seguidas, ele liga o alarme contra ataques de força bruta.
* **Disfarce:** Finge ser um gerenciador de registros padrão do sistema (`[rsyslogd.service]`).

### 2. O Fiscal de Arquivos (`verificador_integridade.py`)
Tira uma "impressão digital" de cada arquivo importante do site. Se um vírus alterar uma única letra do código, o robô pega a mudança e avisa o administrador.
* **Disfarce:** Mascara-se como um fiscal de peças do computador (`[kernel-hardware-monitor]`) e possui regras de auto-defesa.

### 3. O Trincador de Portas Automatizado (`bloqueador_firewall.py`)
Recebe a lista de IPs perigosos e vai direto na muralha de rede (Firewall) para trancar a porta na cara do hacker automaticamente.
* **Disfarce:** Executa os bloqueios em segundo plano fingindo ser uma atualização de rotina (`[systemd-update-service.service]`).

---

## 🚀 Como Executar e Testar

Para testar os robôs de forma totalmente segura sem afetar sistemas reais, acesse o guia passo a passo dentro do diretório:
📂 `laboratorio/instrucoes_laboratorio.txt`

Para rodar os scripts localmente via terminal:
```bash
cd defesas
python analisador_logs.py
python verificador_integridade.py
python bloqueador_firewall.py
```

---
*编Projetos educativos focados em Defesa Cibernética, Proteção Invisível de Processos e Automação.*
