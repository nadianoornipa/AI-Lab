import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt

# Data for temperature variations
temps = [30, 32, 31, 29, 28, 27, 26]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

plt.figure(figsize=(8, 6))
plt.plot(days, temps, marker='o')
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")

plt.savefig("line_graph.png")
print("Plot saved as 'line_graph.png'")
