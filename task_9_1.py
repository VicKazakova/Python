from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print(f'{TrafficLight.__color[0]} is turned on')
        sleep(7)
        print(f'{TrafficLight.__color[1]} is turned on')
        sleep(2)
        print(f'{TrafficLight.__color[2]} is turned on')
        sleep(7)


traffic_light_Ordynka = TrafficLight()
traffic_light_Ordynka.running()
