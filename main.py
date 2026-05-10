import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ==========================================================
# PARÂMETROS DO MODELO
# ==========================================================

RS = 1.0000
RM = 0.0050
RA = 0.0010
RC = 0.0398

CR = 4.4000
CS = 1.3300
CA = 0.0800

LS = 0.0005

V0 = 10.0

Emax = 2.5
Emin = 0.06

# ==========================================================
# FREQUÊNCIA CARDÍACA
# ==========================================================

def get_HR(t):
    """
    Frequência cardíaca variável no tempo.
    """

    if t < 2.5:
        return 75.0

    return 100.0


# ==========================================================
# FUNÇÃO DOUBLE HILL NORMALIZADA
# ==========================================================

def calc_En(tn):
    """
    Função de elastância normalizada.
    """

    term1 = (tn / 0.25) ** 2
    term1 /= (1 + (tn / 0.25) ** 2)

    term2 = 1 / (1 + (tn / 0.75) ** 10)

    return 1.55 * term1 * term2


# ==========================================================
# SISTEMA CARDIOVASCULAR
# ==========================================================

def cardio_system(t, y):

    Pve, Pae, Ps, Pao, Q, phi = y

    # Frequência cardíaca
    HR = get_HR(t)

    # Tempo normalizado
    tn = phi % 1.0

    # Elastância
    En = calc_En(tn)

    E = (Emax - Emin) * En + Emin

    C = 1.0 / E

    # Derivada da elastância
    dt_n = 1e-5

    dEn_dtn = (
        calc_En((tn + dt_n) % 1.0)
        - calc_En((tn - dt_n) % 1.0)
    ) / (2 * dt_n)

    dE_dt = (Emax - Emin) * dEn_dtn * (HR / 60.0)

    dC_dt = -dE_dt / (E ** 2)

    # ======================================================
    # VÁLVULAS
    # ======================================================

    def positive(value):
        return max(value, 0.0)

    mitral_flow = (1.0 / RM) * positive(Pae - Pve)

    aortic_flow = (1.0 / RA) * positive(Pve - Pao)

    # ======================================================
    # EQUAÇÕES DIFERENCIAIS
    # ======================================================

    dPve = (
        -(dC_dt / C) * Pve
        + (1.0 / C) * mitral_flow
        - (1.0 / C) * aortic_flow
    )

    dPae = (
        (Ps - Pae) / (RS * CR)
        - mitral_flow / CR
    )

    dPs = (
        (Pae - Ps) / (RS * CS)
        + Q / CS
    )

    dPao = (
        aortic_flow / CA
        - Q / CA
    )

    dQ = (
        (Pao - Ps) / LS
        - (RC / LS) * Q
    )

    dphi = HR / 60.0

    return [
        dPve,
        dPae,
        dPs,
        dPao,
        dQ,
        dphi
    ]


# ==========================================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ==========================================================

print("Iniciando simulação cardiovascular...")

t_start = 0
t_end = 5

t_span = (t_start, t_end)

t_eval = np.linspace(t_start, t_end, 5000)

# Condições iniciais
y0 = [
    10.0,  # Pve
    10.0,  # Pae
    90.0,  # Ps
    90.0,  # Pao
    0.0,   # Q
    0.0    # fase
]

# ==========================================================
# RESOLUÇÃO DAS EDOs
# ==========================================================

solution = solve_ivp(
    cardio_system,
    t_span,
    y0,
    t_eval=t_eval,
    method="RK45",
    max_step=1e-3
)

# ==========================================================
# EXTRAÇÃO DOS RESULTADOS
# ==========================================================

t = solution.t

Pve = solution.y[0]
Pae = solution.y[1]
Ps = solution.y[2]
Pao = solution.y[3]
Q = solution.y[4]
phi = solution.y[5]

# ==========================================================
# CÁLCULO DE E(t) E VOLUME VENTRICULAR
# ==========================================================

Et_array = np.zeros_like(t)

Vve = np.zeros_like(t)

for i in range(len(t)):

    tn = phi[i] % 1.0

    Et = (Emax - Emin) * calc_En(tn) + Emin

    Et_array[i] = Et

    Vve[i] = Pve[i] / Et + V0

# ==========================================================
# PLOTAGEM
# ==========================================================

fig, axs = plt.subplots(
    4,
    1,
    figsize=(12, 12),
    sharex=True
)

# ==========================================================
# E(t)
# ==========================================================

axs[0].plot(t, Et_array, linewidth=2)

axs[0].set_ylabel("E(t)\n(mmHg/ml)")

axs[0].set_title(
    "Simulação Cardiovascular — Simaan et al. (2009)"
)

axs[0].grid(True)

# ==========================================================
# PRESSÕES
# ==========================================================

axs[1].plot(
    t,
    Pve,
    linewidth=2,
    label="Pve"
)

axs[1].plot(
    t,
    Pao,
    "--",
    linewidth=2,
    label="Pao"
)

axs[1].plot(
    t,
    Ps,
    linewidth=1.5,
    label="Ps"
)

axs[1].plot(
    t,
    Pae,
    linewidth=2,
    label="Pae"
)

axs[1].set_ylabel("Pressões\n(mmHg)")

axs[1].legend()

axs[1].grid(True)

# ==========================================================
# FLUXO
# ==========================================================

axs[2].plot(
    t,
    Q,
    linewidth=2
)

axs[2].set_ylabel("Fluxo Q\n(ml/s)")

axs[2].grid(True)

# ==========================================================
# VOLUME
# ==========================================================

axs[3].plot(
    t,
    Vve,
    linewidth=2
)

axs[3].set_ylabel("Vve\n(ml)")

axs[3].set_xlabel("Tempo (s)")

axs[3].grid(True)

plt.tight_layout()

print("Simulação concluída.")

plt.show()