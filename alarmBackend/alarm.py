from gpiozero import Button, LED
import time
import requests

class Alarm:
    def _init_(self):
        self.alarm_on = False
        self.alarm_enabled = False
        self.current_digit = "off"
        self.led_alarm = LED(11)
        self.led_a = LED(24)
        self.led_b = LED(25)
        self.led_c = LED(8)
        self.led_d = LED(7)
        self.led_e = LED(12)
        self.led_f = LED(16)
        self.led_g = LED(20)
        self.buttons = [
            Button(14),
            Button(15),
            Button(18),
            Button(23)
        ]
        self.buttons[0].when_pressed = self.set_digit_1
        self.buttons[1].when_pressed = self.set_digit_2
        self.buttons[2].when_pressed = self.set_digit_3
        self.buttons[3].when_pressed = self.show_sequence_and_toggle_alarm

    def toggle_alarm(self):
        self.alarm_on = not self.alarm_on
        self.led_alarm.toggle()

    def set_digit(self, digit):
        self.current_digit = digit
        self.show_digit(self.current_digit)

    def set_digit_1(self):
        self.set_digit(1)
        if self.alarm_on==True:
            self.send_data()
        else:
            self.current_digit = "off"

    def set_digit_2(self):
        self.set_digit(2)
        if self.alarm_on==True:
            self.send_data()
        else:
            self.current_digit = "off"

    def set_digit_3(self):
        self.set_digit(3)
        if self.alarm_on==True:
            self.send_data()
        else:
            self.current_digit = "off"

    def show_sequence_and_toggle_alarm(self):
        if self.alarm_on==False:
            for i in range(1, 10):
                self.set_digit(i)
                time.sleep(0.5)
            self.set_digit("A")  # Show the letter A at the end if the alarm is on
            time.sleep(0.5)
        else:
            for i in range(1, 10):
                self.set_digit(i)
                time.sleep(0.5)
            self.set_digit("off")  # Clear the display at the end if the alarm is off
            time.sleep(0.5)
        self.toggle_alarm()
        self.alarm_enabled = True
        self.send_data()


    def send_data(self):
        data = {
            'current_digit': self.current_digit,
            'alarm_state': 'on' if self.alarm_on else 'off'
        }
        response = requests.post('http://10.1.10.208:3000/api/data', json=data)
        print(response.text)
    
    # ... rest of the Alarm class code

def handle_button_command(self, button):
    if button == "button1":
        self.set_digit_1()
    elif button == "button2":
        self.set_digit_2()
    elif button == "button3":
        self.set_digit_3()
    elif button == "button4":
        self.show_sequence_and_toggle_alarm()

# ... rest of the Alarm class code



    def show_digit(self, digit):
        led_a = self.led_a
        led_b = self.led_b
        led_c = self.led_c
        led_d = self.led_d
        led_e = self.led_e
        led_f = self.led_f
        led_g = self.led_g

        if digit == 0:
            led_a.off()
            led_b.off()
            led_c.off()
            led_d.off()
            led_e.off()
            ed_f.off()
            led_g.on()
        elif digit == 1:
            led_a.on()
            led_b.off()
            led_c.off()
            led_d.on()
            led_e.on()
            led_f.on()
            led_g.on()
        elif digit == 2:
            led_a.off()
            led_b.off()
            led_c.on()
            led_d.off()
            led_e.off()
            led_f.on()
            led_g.off()
        elif digit == 3:
            led_a.off()
            led_b.off()
            led_c.off()
            led_d.off()
            led_e.on()
            led_f.on()
            led_g.off()
        elif digit == 4:
            led_a.on()
            led_b.off()
            led_c.off()
            led_d.on()
            led_e.on()
            led_f.off()
            led_g.off()
        elif digit == 5:
            led_a.off()
            led_b.on()
            led_c.off()
            led_d.off()
            led_e.on()
            led_f.off()
            led_g.off()
        elif digit == 6:
            led_a.off()
            led_b.on()
            led_c.off()
            led_d.off()
            led_e.off()
            led_f.off()
            led_g.off()
        elif digit == 7:
            led_a.off()
            led_b.off()
            led_c.off()
            led_d.on()
            led_e.on()
            led_f.on()
            led_g.on()
        elif digit == 8:
            led_a.off()
            led_b.off()
            led_c.off()
            led_d.off()
            led_e.off()
            led_f.off()
            led_g.off()
        elif digit == 9:
            led_a.off()
            led_b.off()
            led_c.off()
            led_d.off()
            led_e.on()
            led_f.off()
            led_g.off()
        elif digit == "A":
            led_a.off()
            led_b.off()
            led_c.off()
            led_d.on()
            led_e.off()
            led_f.off()
            led_g.off()
        elif digit == "off":
            led_a.on()
            led_b.on()
            led_c.on()
            led_d.on()
            led_e.on()
            led_f.on()
            led_g.on()

def main_loop(self):
    previous_digit = None
    previous_alarm_state = None

    while True:
        try:
            response = requests.get('http://10.1.10.208:3000/api/command')
            button_command = response.json()['button']
            self.handle_button_command(button_command)
        except Exception as e:
            print("Error fetching button command:", e)

        self.show_digit(self.current_digit)

        if self.alarm_on:
            self.led_alarm.on()
        else:
            self.led_alarm.off()

        if self.current_digit != previous_digit or self.alarm_on != previous_alarm_state:
            previous_digit = self.current_digit
            previous_alarm_state = self.alarm_on
            self.send_data()

        time.sleep(0.1)

    self.send_data()



alarm = Alarm()
alarm.main_loop()
