import time
import itertools

class Trafficlight:
    __color = [["red", [7,31]], ["yellow", [2,33]], ["green",[7,32]],["yellow",[2,33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])

traffic_light_1 = Trafficlight()
traffic_light_1.running()




