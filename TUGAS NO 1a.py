# Menghitung jarak fokus lensa

n = 1.50  # Indeks bias
R1 = 22.0  # Jari-jari kelengkungan permukaan lensa R1 dalam cm
R2 = 17.5  # Jari-jari kelengkungan permukaan lensa R2 dalam cm

# Rumus untuk menghitung jarak fokus lensa
f = 1 / ((n - 1) * (1/R1 + 1/R2))

print("Jarak fokus lensa (f) adalah:",f,"cm")
