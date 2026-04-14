# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor
  
def main():
    filename = input("Nombre del archivo: ")

    with open(filename, "r") as f:
        n = int(f.readline().strip())

        monitor = temp_monitor.init(n)
        for _ in range(n):
            temp = float(f.readline().strip())
            monitor = temp_monitor.add_reading(monitor, temp)


    print(temp_monitor.longest_rising_streak(monitor))


if __name__ == "__main__":
    main()
