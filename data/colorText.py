import matplotlib.patheffects as pe

fig, ax = plt.subplots(facecolor="#F2F2F2")
ax.axis("off")
tColors = ["#252759", "#202140", "#BF452A", "#D93A2B"]
tLabels = ["Why", "so", "much", "colors?"]

center_x, center_y = 0.5, 0.5  # Center of the figure
delta = 0.05  # Small adjustment to prevent overlap

for i, (label, color) in enumerate(zip(tLabels, tColors)):
    text = ax.text(
        center_x,
        center_y - 4 * i * delta + 0.275,
        label,
        color=color,
        ha="center",
        fontsize=60,
        va="center",
    )
    text.set_path_effects([pe.withStroke(linewidth=5, foreground="k")])

plt.savefig("WhySoMuchColors.pdf", bbox_inches="tight")
plt.show()
