#using matplot lib to plot a line graph regression of autoimmune possible treatment with high possible success rate medicines
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Data for medicines for autoimmune diseases with effectiveness rates (%)
medicines = [
    {"name": "Methotrexate", "success_rate": 75, "category": "DMARDs"},
    {"name": "Hydroxychloroquine", "success_rate": 65, "category": "Antimalarials"},
    {"name": "Sulfasalazine", "success_rate": 60, "category": "DMARDs"},
    {"name": "Infliximab (TNF inhibitor)", "success_rate": 85, "category": "Biologics"},
    {"name": "Etanercept (TNF inhibitor)", "success_rate": 80, "category": "Biologics"},
    {"name": "Adalimumab (TNF inhibitor)", "success_rate": 82, "category": "Biologics"},
    {"name": "Rituximab (B-cell inhibitor)", "success_rate": 88, "category": "Biologics"},
    {"name": "Abatacept (T-cell modulator)", "success_rate": 78, "category": "Biologics"},
    {"name": "Tocilizumab (IL-6 inhibitor)", "success_rate": 86, "category": "Biologics"},
    {"name": "Anakinra (IL-1 inhibitor)", "success_rate": 72, "category": "Biologics"},
    {"name": "Baricitinib (JAK inhibitor)", "success_rate": 84, "category": "JAK Inhibitors"},
    {"name": "Tofacitinib (JAK inhibitor)", "success_rate": 83, "category": "JAK Inhibitors"},
    {"name": "Upadacitinib (JAK inhibitor)", "success_rate": 85, "category": "JAK Inhibitors"},
    {"name": "Prednisolone (Corticosteroid)", "success_rate": 70, "category": "Corticosteroids"},
    {"name": "Azathioprine", "success_rate": 58, "category": "Immunosuppressants"},
    {"name": "Mycophenolate Mofetil", "success_rate": 68, "category": "Immunosuppressants"},
    {"name": "Leflunomide", "success_rate": 72, "category": "DMARDs"},
    {"name": "Certolizumab Pegol", "success_rate": 81, "category": "Biologics"},
    {"name": "Golimumab", "success_rate": 79, "category": "Biologics"},
    {"name": "Belimumab (B-LyS inhibitor)", "success_rate": 76, "category": "Biologics"},
]

# Extract names and success rates
medicine_names = [med["name"] for med in medicines]
success_rates = [med["success_rate"] for med in medicines]

# Group by category
category_data = defaultdict(list)
for med in medicines:
    category_data[med["category"]].append(med["success_rate"])

# Create a figure with multiple subplots
fig = plt.figure(figsize=(16, 12))

# 1. Bar Chart - Success Rate by Medicine
ax1 = plt.subplot(2, 3, 1)
colors = plt.cm.Set3(np.linspace(0, 1, len(medicine_names)))
bars = ax1.barh(medicine_names, success_rates, color=colors)
ax1.set_xlabel("Success Rate (%)", fontsize=10, fontweight='bold')
ax1.set_title("Medicine Success Rates for Autoimmune Diseases", fontsize=12, fontweight='bold')
ax1.set_xlim(50, 95)
for i, bar in enumerate(bars):
    ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
             f'{success_rates[i]}%', va='center', fontsize=8)

# 2. Line Graph - Success Rate Trend
ax2 = plt.subplot(2, 3, 2)
sorted_medicines = sorted(medicines, key=lambda x: x["success_rate"])
sorted_names = [m["name"] for m in sorted_medicines]
sorted_rates = [m["success_rate"] for m in sorted_medicines]
ax2.plot(range(len(sorted_names)), sorted_rates, marker='o', linewidth=2, 
         markersize=6, color='#2E86AB', markerfacecolor='#A23B72')
ax2.fill_between(range(len(sorted_names)), sorted_rates, alpha=0.3, color='#2E86AB')
ax2.set_xticks(range(0, len(sorted_names), 2))
ax2.set_xticklabels([sorted_names[i] for i in range(0, len(sorted_names), 2)], rotation=45, ha='right', fontsize=8)
ax2.set_ylabel("Success Rate (%)", fontsize=10, fontweight='bold')
ax2.set_title("Success Rate Trend (Sorted)", fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)

# 3. Pie Chart - Category Distribution
ax3 = plt.subplot(2, 3, 3)
categories = list(category_data.keys())
category_counts = [len(category_data[cat]) for cat in categories]
colors_pie = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
wedges, texts, autotexts = ax3.pie(category_counts, labels=categories, autopct='%1.1f%%',
                                     colors=colors_pie, startangle=90)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(9)
ax3.set_title("Distribution of Medicines by Category", fontsize=12, fontweight='bold')

# 4. Box Plot - Success Rate Distribution by Category
ax4 = plt.subplot(2, 3, 4)
box_data = [category_data[cat] for cat in categories]
bp = ax4.boxplot(box_data, tick_labels=categories, patch_artist=True)
for patch, color in zip(bp['boxes'], colors_pie):
    patch.set_facecolor(color)
ax4.set_ylabel("Success Rate (%)", fontsize=10, fontweight='bold')
ax4.set_title("Success Rate Distribution by Category", fontsize=12, fontweight='bold')
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=9)
ax4.grid(True, alpha=0.3, axis='y')

# 5. Scatter Plot - Success Rate vs Medicine Index
ax5 = plt.subplot(2, 3, 5)
scatter_colors = ['#FF6B6B' if med["category"] == 'Biologics' else '#4ECDC4' if med["category"] == 'DMARDs' 
                  else '#45B7D1' for med in medicines]
ax5.scatter(range(len(medicines)), success_rates, s=200, alpha=0.6, c=scatter_colors, edgecolors='black')
ax5.set_xlabel("Medicine Index", fontsize=10, fontweight='bold')
ax5.set_ylabel("Success Rate (%)", fontsize=10, fontweight='bold')
ax5.set_title("Success Rate Distribution (Scatter Plot)", fontsize=12, fontweight='bold')
ax5.grid(True, alpha=0.3)

# 6. Bar Chart - Average Success Rate by Category
ax6 = plt.subplot(2, 3, 6)
avg_rates = [np.mean(category_data[cat]) for cat in categories]
bars6 = ax6.bar(categories, avg_rates, color=colors_pie, edgecolor='black', linewidth=1.5)
ax6.set_ylabel("Average Success Rate (%)", fontsize=10, fontweight='bold')
ax6.set_title("Average Success Rate by Category", fontsize=12, fontweight='bold')
plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=9)
ax6.set_ylim(55, 90)
for bar, rate in zip(bars6, avg_rates):
    ax6.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'{rate:.1f}%', ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()

plt.show()
