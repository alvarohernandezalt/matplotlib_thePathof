fig, ax = plt.subplots(facecolor="#F2F2F2")
ax.axis("off")
tColors = ["#252759", "#202140", "#BF452A", "#D93A2B"]
tLabels = ["Why", "so", "much", "colors?"]

center_x, center_y = 0.5, 0.5  # Center of the figure
delta = 0.05  # Small adjustment to prevent overlap

for i, (label, color) in enumerate(zip(tLabels, tColors)):
    ax.text(
        center_x,
        center_y - 4 * i * delta + 0.25,
        label,
        color=color,
        ha="center",
        fontsize=60,
        va="center",
    )

plt.show()
