import matplotlib.pyplot as plt


def get_arr(dic,key):
	l = []
	for obj in dic:
		l.append(obj[key])
	return l


print("Press Ctrl+C to exit")

normal_op = [
    {"voltage": 380, "current": 5.5, "power_input": 1040, "speed_rpm": 1475, "power_output": 636.35, "torque_Nm": 4.12, "efficiency": 61.188, "slip": 0.017, "power_factor": 0.287, "dc_voltage": 206, "dc_current": 2},
    {"voltage": 380, "current": 5.6, "power_input": 1240, "speed_rpm": 1467, "power_output": 837.6, "torque_Nm": 5.45, "efficiency": 67.548, "slip": 0.022, "power_factor": 0.336, "dc_voltage": 202, "dc_current": 3},
    {"voltage": 380, "current": 5.7, "power_input": 1580, "speed_rpm": 1453, "power_output": 1138.913, "torque_Nm": 7.49, "efficiency": 72.083, "slip": 0.031, "power_factor": 0.421, "dc_voltage": 198, "dc_current": 4.5},
    {"voltage": 380, "current": 5.8, "power_input": 1800, "speed_rpm": 1446, "power_output": 1334.913, "torque_Nm": 8.82, "efficiency": 74.162, "slip": 0.036, "power_factor": 0.472, "dc_voltage": 195, "dc_current": 5.5},
    {"voltage": 380, "current": 5.9, "power_input": 2040, "speed_rpm": 1440, "power_output": 1527.813, "torque_Nm": 10.13, "efficiency": 74.893, "slip": 0.04, "power_factor": 0.525, "dc_voltage": 192, "dc_current": 6.5},
    {"voltage": 380, "current": 6.0, "power_input": 2120, "speed_rpm": 1437, "power_output": 1619.6, "torque_Nm": 10.76, "efficiency": 76.396, "slip": 0.042, "power_factor": 0.537, "dc_voltage": 190, "dc_current": 7},
    {"voltage": 380, "current": 6.2, "power_input": 2500, "speed_rpm": 1416, "power_output": 1887.313, "torque_Nm": 12.73, "efficiency": 75.493, "slip": 0.056, "power_factor": 0.613, "dc_voltage": 184, "dc_current": 8.5},
]

unbalanced_op =  [
    {"voltage": 380, "current": 7.1, "power_input": 1200, "speed_rpm": 1472, "power_output": 624.35, "torque_Nm": 4.05, "efficiency": 52.029, "slip": 0.019, "power_factor": 0.257, "dc_voltage": 200, "dc_current": 2},
    {"voltage": 380, "current": 7.3, "power_input": 1420, "speed_rpm": 1462, "power_output": 822.6, "torque_Nm": 5.37, "efficiency": 57.93, "slip": 0.025, "power_factor": 0.296, "dc_voltage": 197, "dc_current": 3},
    {"voltage": 380, "current": 7.7, "power_input": 1780, "speed_rpm": 1447, "power_output": 1111.913, "torque_Nm": 7.34, "efficiency": 62.467, "slip": 0.035, "power_factor": 0.351, "dc_voltage": 192, "dc_current": 4.5},
    {"voltage": 380, "current": 8.1, "power_input": 2020, "speed_rpm": 1433, "power_output": 1296.413, "torque_Nm": 8.64, "efficiency": 64.179, "slip": 0.045, "power_factor": 0.379, "dc_voltage": 188, "dc_current": 5.5},
    {"voltage": 380, "current": 8.5, "power_input": 2300, "speed_rpm": 1419, "power_output": 1475.813, "torque_Nm": 9.93, "efficiency": 64.166, "slip": 0.054, "power_factor": 0.411, "dc_voltage": 184, "dc_current": 6.5},
    {"voltage": 380, "current": 8.8, "power_input": 2400, "speed_rpm": 1409, "power_output": 1563.6, "torque_Nm": 10.6, "efficiency": 65.15, "slip": 0.061, "power_factor": 0.414, "dc_voltage": 182, "dc_current": 7},
    {"voltage": 380, "current": 9.4, "power_input": 2725, "speed_rpm": 1397, "power_output": 1836.313, "torque_Nm": 12.55, "efficiency": 67.388, "slip": 0.069, "power_factor": 0.44, "dc_voltage": 178, "dc_current": 8.5},
]

balanced_op_simulation = [
    { "voltage": 400, "current": 4.187, "power_input": 581.8, "speed_rpm": 1493, "dc_voltage": 205.5, "dc_current": 2.055, "power_output": 433.2, "power_factor": 0.347, "efficiency": 74.46, "torque_Nm": 2.771, "slip": 0.00478 },
    { "voltage": 400, "current": 4.242, "power_input": 763, "speed_rpm": 1490, "dc_voltage": 203, "dc_current": 2.9, "power_output": 610.1, "power_factor": 0.45, "efficiency": 79.96, "torque_Nm": 3.91, "slip": 0.0065 },
    { "voltage": 400, "current": 4.384, "power_input": 1087, "speed_rpm": 1486, "dc_voltage": 198.4, "dc_current": 4.4, "power_output": 925, "power_factor": 0.62, "efficiency": 85.21, "torque_Nm": 5.946, "slip": 0.0096 },
    { "voltage": 400, "current": 4.528, "power_input": 1338, "speed_rpm": 1482, "dc_voltage": 194.9, "dc_current": 5.57, "power_output": 1165, "power_factor": 0.74, "efficiency": 86.8, "torque_Nm": 7.51, "slip": 0.012 },
    { "voltage": 400, "current": 4.666, "power_input": 1544, "speed_rpm": 1479, "dc_voltage": 192.1, "dc_current": 6.511, "power_output": 1360, "power_factor": 0.82, "efficiency": 88.2, "torque_Nm": 8.78, "slip": 0.014 },
    { "voltage": 400, "current": 4.754, "power_input": 1662, "speed_rpm": 1477, "dc_voltage": 190.4, "dc_current": 7.05, "power_output": 1471, "power_factor": 0.873, "efficiency": 88.65, "torque_Nm": 9.51, "slip": 0.015 },
    { "voltage": 400, "current": 5.03, "power_input": 1995, "speed_rpm": 1473, "dc_voltage": 185.8, "dc_current": 8.58, "power_output": 1785, "power_factor": 0.99, "efficiency": 89.5, "torque_Nm": 11.58, "slip": 0.0183 }
]

unbalanced_op_simulation = [
    { "voltage": 400, "current": 7, "power_input": 1198, "speed_rpm": 1475, "dc_voltage": 206.2, "dc_current": 2.06, "power_output": 620, "power_factor": 0.26, "efficiency": 52, "torque_Nm": 4, "slip": 0.017 },
    { "voltage": 400, "current": 7.2, "power_input": 1410, "speed_rpm": 1466, "dc_voltage": 203, "dc_current": 2.9, "power_output": 825, "power_factor": 0.3, "efficiency": 58, "torque_Nm": 5.5, "slip": 0.026 },
    { "voltage": 400, "current": 7.68, "power_input": 1790, "speed_rpm": 1448, "dc_voltage": 198.4, "dc_current": 4.4, "power_output": 1120, "power_factor": 0.37, "efficiency": 63, "torque_Nm": 7.5, "slip": 0.037 },
    { "voltage": 400, "current": 8.089, "power_input": 2006, "speed_rpm": 1436, "dc_voltage": 195, "dc_current": 5.57, "power_output": 1300, "power_factor": 0.39, "efficiency": 64.2, "torque_Nm": 8.7, "slip": 0.04 },
    { "voltage": 400, "current": 8.37, "power_input": 2297, "speed_rpm": 1420, "dc_voltage": 192.1, "dc_current": 6.51, "power_output": 1480, "power_factor": 0.42, "efficiency": 64.5, "torque_Nm": 10, "slip": 0.055 },
    { "voltage": 400, "current": 8.75, "power_input": 2395, "speed_rpm": 1410, "dc_voltage": 190.4, "dc_current": 7.05, "power_output": 1565, "power_factor": 0.44, "efficiency": 66.4, "torque_Nm": 11.2, "slip": 0.062 },
    { "voltage": 400, "current": 9.3, "power_input": 2730, "speed_rpm": 1395, "dc_voltage": 185.8, "dc_current": 8.58, "power_output": 1840, "power_factor": 0.47, "efficiency": 68, "torque_Nm": 13, "slip": 0.07 }
]



def plot_graphs(normal_op, unbalanced_op):
	
	def plot(x, y, title, xlabel, ylabel):
		plt.figure(title)
		plt.plot(get_arr(normal_op, x), get_arr(normal_op, y), 'o-', label='Normal Operation')
		plt.plot(get_arr(unbalanced_op, x), get_arr(unbalanced_op, y), 'x-', label='Unbalanced Operation')
		plt.title(title)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.legend()
		plt.grid(True)
		plt.show(block=False)
	
	plot('slip', 'efficiency', 'Slip vs Efficiency', 'Slip', 'Efficiency')
	plot('torque_Nm', 'speed_rpm', 'Torque vs Speed', 'Torque (Nm)', 'Speed (RPM)')
	plot('torque_Nm', 'current', 'Torque vs Motor Input Current', 'Torque (Nm)', 'Current (A)')
	plot('torque_Nm', 'efficiency', 'Torque vs Efficiency', 'Torque (Nm)', 'Efficiency')
	plot('torque_Nm', 'power_factor', 'Torque vs Input Power Factor', 'Torque (Nm)', 'Power Factor')
	plot('torque_Nm', 'slip', 'Torque vs Slip', 'Torque (Nm)', 'Slip')
	plot('current', 'efficiency', 'Motor Current vs Efficiency', 'Current (A)', 'Efficiency')
	plot('current', 'power_input', 'Motor Current vs Input Power', 'Current (A)', 'Input Power (W)')
	plot('current', 'power_factor', 'Motor Current vs Input Power Factor', 'Current (A)', 'Power Factor')
	plot('power_input', 'power_factor', 'Power Input vs Input Power Factor', 'Input Power (W)', 'Power Factor')
	plot('power_input', 'efficiency', 'Power Input vs Efficiency', 'Input Power (W)', 'Efficiency')
	plot('power_output', 'power_factor', 'Output Power vs Input Power Factor', 'Output Power (W)', 'Power Factor')
	plot('power_output', 'efficiency', 'Output Power vs Efficiency', 'Output Power (W)', 'Efficiency')

# plot_graphs(normal_op, unbalanced_op)
plot_graphs(balanced_op_simulation, unbalanced_op_simulation)

input()