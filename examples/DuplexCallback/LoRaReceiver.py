from time import sleep

def receive(lora):
    print("LoRa Receiver")

    while True:
        if lora.receivedPacket():
            lora.blink_led()

            try:
                payload = lora.read_payload()
                print("*** Received message ***\n{}".format(payload.decode()))
            except Exception as e:
                print(e)
            print("with RSSI: {}\n".format(lora.packetRssi()))
            lora.show_text('%i:'%lora.packetRssi(),0,0,clear_first = True, show_now = False)
            #sleep(1)
            lora.show_text("{}".format(payload.decode()),0,16,clear_first = False, show_now = True)