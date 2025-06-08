import RPi.GPIO as GPIO
import time
import requests

# Define GPIO pins for motor control
IN1 = 17  # Left Motor Forward
IN2 = 18  # Left Motor Backward
IN3 = 22  # Right Motor Forward
IN4 = 23  # Right Motor Backward

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    stop()  # Ensure the car is stopped initially

def stop():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

def forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def backward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def left():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def right():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def get_command():
    try:
        response = requests.get("https://rc-api-self.vercel.app/state", timeout=3)
        return response.json().get("status", "stop")
    except:
        return "stop"

def main():
    setup()
    prev_command = "stop"

    while True:
        command = get_command().strip().lower()
        if command != prev_command:
            print(f"Received command: {command}")
            if command == "forward":
                forward()
            elif command == "backward":
                backward()
            elif command == "left":
                left()
            elif command == "right":
                right()
            else:
                stop()
            prev_command = command
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted! Stopping car.")
    finally:
        stop()
        GPIO.cleanup()
