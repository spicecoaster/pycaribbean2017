from umqtt.simple import MQTTClient
import network
import machine
import time

# Publish test messages using mosquitto_pub
# mosquitto_pub -t "led/1" -m on
# mosquitto_pub -t "led/1" -m off

MQTT_BROKER_IP="192.168.0.100"
STATION_NO=1

SSID='PYCARIB_IOT_WORKSHOP'
PASSWORD='WELCOMETOIOT'

red_led=machine.Pin(0, machine.Pin.OUT)

def setup_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def subscriber_callback(topic, msg):
    print((topic, msg))
    if msg == b"on":
        red_led.low()
        #time.sleep(0.5)
        #red_led.high()
    else:
        red_led.high()

def setup_mqtt_subscriber():
    global mqtt_subscriber

    mqtt_subscriber = MQTTClient("umqtt_client", MQTT_BROKER_IP)
    mqtt_subscriber.set_callback(subscriber_callback)
    mqtt_subscriber.connect()
    mqtt_subscriber.subscribe(b"led/1")
    while True:
        if True:
            mqtt_subscriber.wait_msg()
        else:
            mqtt_subscriber.check_msg()
            time.sleep(1)

def main():
    setup_wifi()
    setup_mqtt_subscriber()

if __name__ == "__main__":
    main()

