from gpiozero import PWMOutputDevice, DigitalOutputDevice
from gpiozero.pins.lgpio import LGPIOFactory

class MotorControl:
    def __init__(self, L_PWM=12, R_PWM=16, L_EN=27, R_EN=17, L2_PWM=21, R2_PWM=19, L2_EN=26, R2_EN=13):
        factory = LGPIOFactory()
        self.left_pwm = PWMOutputDevice(L_PWM, pin_factory=factory)
        self.right_pwm = PWMOutputDevice(R_PWM, pin_factory=factory)
        self.left2_pwm = PWMOutputDevice(L2_PWM, pin_factory=factory)
        self.right2_pwm = PWMOutputDevice(R2_PWM, pin_factory=factory)
        self.left_en = DigitalOutputDevice(L_EN, pin_factory=factory)
        self.right_en = DigitalOutputDevice(R_EN, pin_factory=factory)
        self.left2_en = DigitalOutputDevice(L2_EN, pin_factory=factory)
        self.right2_en = DigitalOutputDevice(R2_EN, pin_factory=factory)
        self.current_speed = 0.0
        self.target_speed = 0.0
        self.ramp_step = 0.02
        self.direction = "stop"
        self.left_en.on()
        self.right_en.on()
        self.left2_en.on()
        self.right2_en.on()

    def move_forward(self, speed): self._set("forward", speed)
    def turn_left(self, speed): self._set("left", speed)
    def turn_right(self, speed): self._set("right", speed)
    def stop_motor(self): self._set("stop", 0.0)

    def _set(self, direction, speed): self.direction, self.target_speed = direction, speed

    def ramp_to_target(self):
        if self.current_speed < self.target_speed:
            self.current_speed = min(self.target_speed, self.current_speed + self.ramp_step)
        elif self.current_speed > self.target_speed:
            self.current_speed = max(self.target_speed, self.current_speed - self.ramp_step)

        pwm = self.current_speed
        if self.direction == "forward":
            self.left_pwm.value = 0; self.right_pwm.value = pwm
            self.left2_pwm.value = 0; self.right2_pwm.value = pwm
        elif self.direction == "left":
            self.left_pwm.value = pwm; self.right_pwm.value = 0
            self.left2_pwm.value = 0; self.right2_pwm.value = pwm
        elif self.direction == "right":
            self.left_pwm.value = 0; self.right_pwm.value = pwm
            self.left2_pwm.value = pwm; self.right2_pwm.value = 0
        else:
            self.left_pwm.value = 0; self.right_pwm.value = 0
            self.left2_pwm.value = 0; self.right2_pwm.value = 0
