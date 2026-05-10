# Simulação Cardiovascular — Modelo de Simaan et al. (2009)

Este projeto implementa uma simulação computacional do sistema cardiovascular baseada no modelo de parâmetros concentrados de quinta ordem descrito por Simaan et al. (2009).

O objetivo é reproduzir o comportamento hemodinâmico do ventrículo esquerdo, da circulação sistêmica e da aorta utilizando equações diferenciais ordinárias (EDOs).

---

# Funcionalidades

O modelo simula:

- Pressão ventricular esquerda (Pve)
- Pressão atrial esquerda (Pae)
- Pressão arterial sistêmica (Ps)
- Pressão aórtica (Pao)
- Fluxo sanguíneo total (Q)
- Volume ventricular esquerdo (Vve)
- Elastância ventricular variável E(t)
- Alterações dinâmicas da frequência cardíaca

O sistema também representa:

- Relaxamento isovolumétrico
- Enchimento ventricular
- Contração isovolumétrica
- Ejeção ventricular

---

# Tecnologias Utilizadas

- Python 3.10+
- NumPy
- SciPy
- Matplotlib

---

# Estrutura do Projeto

```bash
simulacao_cardio_simaan/
│
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

---

# Instalação do Projeto

## 1. Clonar ou baixar o projeto

Extraia ou copie a pasta do projeto para seu computador.

---

## 2. Abrir no VS Code

Abra o Visual Studio Code.

Depois vá em:

File > Open Folder

e selecione a pasta:

```bash
simulacao_cardio_simaan
```

---

# 3. Criar Ambiente Virtual

Abra o terminal do VS Code:

```bash
Ctrl + `
```

Execute:

## Windows

```powershell
python -m venv venv
```

Ative o ambiente virtual:

```powershell
.\venv\Scripts\Activate
```

Se aparecer erro de permissão:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois ative novamente:

```powershell
.\venv\Scripts\Activate
```

---

## Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 4. Instalar Dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

---

# 5. Executar o Projeto

Execute:

```bash
python main.py
```

ou clique no botão:

▶ Run Python File

no canto superior direito do VS Code.

---

# Saídas Geradas

A simulação irá gerar gráficos contendo:

1. Elastância ventricular E(t)
2. Pressões cardíacas e sistêmicas
3. Fluxo sanguíneo total
4. Volume ventricular esquerdo

---

# Modelo Matemático

O modelo utiliza:

- Circuito de parâmetros concentrados
- Equações diferenciais ordinárias
- Função de elastância "Double Hill"
- Comutação valvar baseada em diodos ideais

---

# Referência

Simaan, M. A., Ferreira, A., Chen, S., Antaki, J. F., & Galati, D. G. (2009).

"A Dynamical State Space Representation and Performance Analysis of a Feedback Controlled Rotary Left Ventricular Assist Device"

IEEE Transactions on Control Systems Technology.