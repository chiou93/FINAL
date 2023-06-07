import matplotlib.pyplot as plt

# Создание диаграммы
plt.figure(figsize=(8, 6))

# Родительский класс
plt.text(0.5, 0.5, 'Родительский\nкласс', ha='center', va='center', fontsize=14, bbox=dict(facecolor='lightblue', edgecolor='black'))

# Домашние животные
plt.text(0.2, 0.25, 'Домашние\nживотные', ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightgreen', edgecolor='black'))

# Вьючные животные
plt.text(0.8, 0.25, 'Вьючные\nживотные', ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightgreen', edgecolor='black'))

# Связи между классами
plt.arrow(0.5, 0.45, 0, -0.1, head_width=0.03, head_length=0.03, fc='black', ec='black')
plt.arrow(0.5, 0.45, -0.3, -0.2, head_width=0.03, head_length=0.03, fc='black', ec='black')
plt.arrow(0.5, 0.45, 0.3, -0.2, head_width=0.03, head_length=0.03, fc='black', ec='black')

# Классы домашних животных
plt.text(0.1, 0.05, 'Собаки', ha='center', va='center', fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black'))
plt.text(0.3, 0.05, 'Кошки', ha='center', va='center', fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black'))
plt.text(0.5, 0.05, 'Хомяки', ha='center', va='center', fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black'))

# Классы вьючных животных
plt.text(0.7, 0.05, 'Лошади', ha='center', va='center', fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black'))
plt.text(0.9, 0.05, 'Верблюды', ha='center', va='center', fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black'))
plt.text(1.1, 0.05, 'Ослы', ha='center', va='center', fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black'))

# Настройка осей координат
plt.axis('off')

# Отображение диаграммы
plt.show()
