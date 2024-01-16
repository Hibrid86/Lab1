import csv
from statistics import mean
with open('DATA475_lab_rectangles_data.csv') as f:
    next(f)
    reader = csv.reader(f)
    areas = []
    for row in reader:
        areas.append(float(row[1]) * float(row[2]))

summary = {
    'Total Count': len(areas),
    'Maximum': max(areas),
    'Minimum': min(areas),
    'Summation': sum(areas),
    'Average': mean(areas),
}
for key, value in summary.items():
    print(f"{key}: {value}")

with open('summary.csv', "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(summary.keys())
    writer.writerow(summary.values())
# f.close()