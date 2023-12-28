from scipy.special import airy, ai_zeros

nmax = 16

# Find the first nmax zeros of Ai(x)
a, _, _, _ = ai_zeros(nmax)
# The actual boundary condition is Ai(-qE) = 0 at q=0, so:
qE = -a


def prob_qm(n, dq):
    """
    Return the quantum mechanical probability density for a particle moving
    in a uniform gravitational field.

    """
    # The quantum mechanical wavefunction is proportional to Ai(q-qE) where
    # the qE corresponding to quantum number n is indexed at n-1
    psi, _, _, _ = airy(q - qE[n - 1])
    # Return the probability density, after rough-and-ready normalization
    P = psi**2
    return P / (sum(P) * dq)


def prob_cl(n):
    """
    Return the classical probability density for a particle bouncing
    elastically in a uniform gravitational field.

    """
    # The classical probability density is already normalized
    condition = qE[n - 1] * (qE[n - 1] - q) < 0
    return np.where(condition, np.nan, 0.5 / np.sqrt(qE[n - 1] * (qE[n - 1] - q)))


# The ground state, n=1
# q, dq = np.linspace(0, 4, 1000, retstep=True)

# An excited state, n=16
q, dq = np.linspace(0, 20, 1000, retstep=True)

fig, ax = plt.figure(figsize=(6, 6), facecolor="#9F9F9F"), plt.axes(facecolor="#9F9F9F")

# Change the params of both ticks and ticklegend
ax.tick_params(axis="x", colors="#C6C8CB")
ax.tick_params(axis="y", colors="#C6C8CB")
ax.set_ylim(0, 0.8)

# Change the color of spines
for spine in "bottom", "left", "top", "right":
    ax.spines[spine].set_color("#C6C8CB")


# Label using artist object (set_label() method)
(classical,) = ax.plot(q, prob_cl(1), color="#EBA62A")
classical.set_label("Classical")

(quantum,) = ax.plot(q, prob_qm(1, dq), color="#EB892A")
quantum.set_label("Quantum")

ax.set_xlabel("P(q)", color="#C6C8CB")
ax.set_ylabel("q", color="#C6C8CB", rotation=0)
ax.set_title("A quantum particle in a gravitational field", color="#C6C8CB")
ax.text(2.25, 0.78, s="Classical", va="center", color="#EBA62A", size=10)
ax.text(
    q[-1] - 0.5,
    prob_qm(1, dq)[-1] + 0.04,
    s="Quantum",
    va="center",
    color="#EB892A",
    size=10,
)

# Save the vector SVG
plt.savefig("quantumGravitational.svg")

# An excited state, n=16
q, dq = np.linspace(0, 20, 1000, retstep=True)

fig, ax = plt.figure(figsize=(6, 6), facecolor="#9F9F9F"), plt.axes(facecolor="#9F9F9F")

# Change the params of both ticks and ticklegend
ax.tick_params(axis="x", colors="#C6C8CB")
ax.tick_params(axis="y", colors="#C6C8CB")
ax.set_xlim(0, 23)
ax.set_ylim(0, 0.3)

# Change the color of spines
for spine in "bottom", "left", "top", "right":
    ax.spines[spine].set_color("#C6C8CB")


# Label using artist object (set_label() method)
(classical,) = ax.plot(q, prob_cl(16), color="#EBA62A")
classical.set_label("Classical")

(quantum,) = ax.plot(q, prob_qm(16, dq), color="#EB892A")
quantum.set_label("Quantum")

ax.set_xlabel("P(q)", color="#C6C8CB", labelpad=10)
ax.set_ylabel("q", color="#C6C8CB", rotation=0, labelpad=10)
ax.set_title(
    "A quantum particle in a gravitational field",
    color="#C6C8CB",
    ha="center",
    fontsize=12,
    y=1.03,
)
ax.text(
    0.5,
    1.00,
    s="The Excited State n=16",
    ha="center",
    transform=ax.transAxes,
    color="#C6C8CB",
    fontsize=10,
)
ax.annotate("Classical", xy=(18, 0.29), va="center", color="#EBA62A", size=10)
ax.annotate(
    "Quantum",
    xy=(q[-1] - 0.5, prob_qm(1, dq)[-1] + 0.01),
    va="center",
    color="#EB892A",
    size=10,
)

# Save the vector SVG
plt.savefig("quantumExcitedGravitational.svg")
