# temp_monitor.py
# Libreria de funciones para registrar lecturas de temperatura.
#
# Estructura del diccionario (monitor):
#   - 'max':      numero maximo de lecturas permitidas (int)
#   - 'readings': lista con las temperaturas de cada lectura (list)
#   - 'total':    suma total de todas las temperaturas (float)


def init(max_readings):
    return {"max": max_readings, "readings": [], "total": 0.0}
    


def add_reading(monitor, temp):
     if len(monitor["readings"]) < monitor["max"]:
        monitor["readings"].append(temp)
        monitor["total"] += temp
     return monitor



def count(monitor):
      return len(monitor["readings"])


def average_temp(monitor):
    if count(monitor) == 0:
        return 0.0
    return monitor["total"] / count(monitor)


def format_readings(monitor):
     return str(monitor["readings"])


def highest_temp(monitor):
     if count(monitor) == 0:
        return None
     return max(monitor["readings"])


import math

def coldest_window(monitor, k):
    readings = monitor["readings"]
    n = len(readings)
    # si k == 1, simplemente el mínimo
    if k == 1:
        return min(readings)
    # calcular promedio de cada ventana de tamaño k
    min_avg = math.inf
    for i in range(n - k + 1):
        window = readings[i:i+k]
        avg = sum(window) / k
        if avg < min_avg:
            min_avg = avg
    return min_avg


def longest_rising_streak(monitor):
    readings = monitor["readings"]
    if not readings:
        return 0
    max_streak = 1
    current_streak = 1
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:  # estrictamente mayor
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1
    return max_streak


def main():
    # crear un monitor para temperaturas de Bogota (12 horas, 6am-5pm)
    monitor = init(12)
    monitor = add_reading(monitor, 8.0)   # 6am
    monitor = add_reading(monitor, 9.5)   # 7am
    monitor = add_reading(monitor, 11.0)  # 8am
    monitor = add_reading(monitor, 13.5)  # 9am
    monitor = add_reading(monitor, 15.0)  # 10am
    monitor = add_reading(monitor, 17.5)  # 11am
    monitor = add_reading(monitor, 19.0)  # 12pm
    monitor = add_reading(monitor, 20.0)  # 1pm
    monitor = add_reading(monitor, 19.5)  # 2pm
    monitor = add_reading(monitor, 18.0)  # 3pm
    monitor = add_reading(monitor, 16.5)  # 4pm
    monitor = add_reading(monitor, 15.0)  # 5pm

    # imprimir estadisticas
    print("numero de lecturas =", count(monitor))               # 12
    print("temp promedio =", average_temp(monitor))             # 15.208...
    print("temp mas alta =", highest_temp(monitor))             # 20.0
    print("ventana mas fria (3) =", coldest_window(monitor, 3)) # 9.5
    print("racha creciente =", longest_rising_streak(monitor))  # 8

    # imprimir temperaturas
    print(format_readings(monitor))


if __name__ == "__main__":
    main()
