from ble_uart import BLE_UART#匯入藍芽模組
from machine import Pin#匯入腳位模組
import time#匯入時間模組

ble = BLE_UART("ESP32_bluetooth")#藍芽名稱

led = Pin(5, Pin.OUT)#LED位置是連接在第五腳位，狀態設置為輸出

while True:
    i = ble.get()
    if i == "1":
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(1)
        print(i)
    if i == "2":
        for j in range(2):
            led.value(1)
            time.sleep(1)
            led.value(0)
            time.sleep(1)
        print(i)
