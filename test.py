import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Configuration des broches de l'écran LCD
lcd_columns = 16
lcd_rows = 2
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D5)
lcd_d7 = digitalio.DigitalInOut(board.D11)

# Initialisation de l'écran LCD
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Allumer l'écran LCD en rouge
lcd.clear()
lcd.color = (100, 0, 0)
lcd.message = "Hello, world!"
time.sleep(5)
