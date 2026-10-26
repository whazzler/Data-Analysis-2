import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

print('Menampilkan 5 data pertama')
print(df.head())

print('Menampilkan 5 data terakhir')
print(df.tail())

print('Menampilkan semua informasi')
print(df.info())

print(df.describe())


# df['spaghetti count'].plot(kind='hist', bins=7, color='cyan', edgecolor='black')

# plt.title('spaghetti count')
# plt.xlabel('number of noodles')
# plt.ylabel('height')
# plt.grid(axis='y', linestyle='--', alpha=0.2)

# plt.tight_layout()
# plt.savefig('dasjdjkdmkewew.jpg')
# plt.show()
# plt.close()

race_counts = df['race/ethnicity'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8, 5))
race_counts.plot(kind='pie', color='skyblue', ax=ax)

ax.set_title('Number of Students by Race/Ethnicity Group', fontsize=14, fontweight='bold')
ax.set_xlabel('Race/Ethnicity Group', fontsize=12)
ax.set_ylabel('Student Count', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('student_counts_by_race.png')
plt.close()

plt.figure(figsize=(8, 5))

