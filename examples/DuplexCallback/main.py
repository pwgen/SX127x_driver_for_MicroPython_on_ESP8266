# coding: utf-8
from machine import I2C,Pin
import time
import ssd1306
rst = Pin(16, Pin.OUT)
button=Pin(0,Pin.IN)
rst.value(1)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)

oled.fill(0)
oled.text('Press Boot', 45, 5)
oled.text('1 Sec to select', 20, 20)
oled.text('MenuA', 20, 40)
oled.show() 
time.sleep(1)
if button.value()==0:
	oled.fill(0)
	oled.text('ESP32', 45, 5)
	oled.text('MicroPython', 20, 20)
	oled.show() 
else:
	oled.fill(0)
	oled.text('ESP32', 45, 5)
	oled.text('Lora', 20, 20)
	oled.show() 


	import gc
	gc.collect()

	import sx127x
	gc.collect()

	import test
# import test_dual_channels as test
	gc.collect()
	test.main() 