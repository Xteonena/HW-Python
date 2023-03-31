import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("survey lung cancer.csv")

# Age histogram
sns.histplot(df['AGE'], kde=True, bins=10)
plt.title('Гистограмма возраста')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.show()

# Grouping data by age and diagnosis
age_grouped_data = df.groupby(['AGE', 'LUNG_CANCER']).size().reset_index(name='Count')
sns.lineplot(x='AGE', y='Count', hue='LUNG_CANCER', data=age_grouped_data)
plt.title('Распределение диагнозов рака легких по возрасту')
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.show()

# Grouping data by smoking habit and diagnosis
grouped_data = df.groupby(['SMOKING', 'LUNG_CANCER']).size().reset_index(name='Count')
sns.barplot(x='SMOKING', y='Count', hue='LUNG_CANCER', data=grouped_data)
plt.title('Результаты тестов на рак легких по курению')
plt.xlabel('Курит? Где 1-Нет, а 2-Да')
plt.ylabel('Количество')
plt.show()
