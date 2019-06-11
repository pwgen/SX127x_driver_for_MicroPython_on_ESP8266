from time import sleep
import esp32


def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        data=esp32.hall_sensor()
        payload = 'Hal {0}'.format(data)
        print("Sending packet: \n{}\n".format(payload))
        lora.println(payload)
        lora.show_text("Send %i"%counter)
        counter += 1
        sleep(5)
