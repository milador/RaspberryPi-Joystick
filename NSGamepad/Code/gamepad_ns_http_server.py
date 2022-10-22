from typing import Optional
import time
from fastapi import FastAPI,Path
from fastapi.middleware.cors import CORSMiddleware
from NSGamepad import *

gamepad = NSGamepad()
gamepad.begin('/dev/hidg0')

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
tags_metadata = [
    {
        "name": "dpad",
        "description": "",
    },
    {
        "name": "buttons",
        "description": "",
    },
    {
        "name": "meta",
        "description": "",
    },
    {
        "name": "stick",
        "description": "",
    }
]

@app.post('/dpad_up', tags=["dpad"])
def dpad_up():
    gamepad.dPad(DPad.UP)
    time.sleep(0.1)
    gamepad.dPad(DPad.CENTERED)
    return "Ok"

@app.post('/dpad_down', tags=["dpad"])
def dpad_down():
    gamepad.dPad(DPad.DOWN)
    time.sleep(0.1)
    gamepad.dPad(DPad.CENTERED)
    return "Ok"

@app.post('/dpad_left', tags=["dpad"])
def dpad_down():
    gamepad.dPad(DPad.LEFT)
    time.sleep(0.1)
    gamepad.dPad(DPad.CENTERED)
    return "Ok"

@app.post('/dpad_right', tags=["dpad"])
def dpad_down():
    gamepad.dPad(DPad.LEFT)
    time.sleep(0.1)
    gamepad.dPad(DPad.CENTERED)
    return "Ok"

@app.post('/stick_l', tags=["sticks"])
def lstick(
        x: int = Path(default=128,ge=0, le=255),
        y: int = Path(default=128,ge=0, le=255)
    ):
    gamepad.leftXAxis(x)
    gamepad.leftYAxis(y)
    return "Ok"

@app.post('/stick_r', tags=["sticks"])
def rstick(
        x: int = Path(default=128,ge=0, le=255),
        y: int = Path(default=128,ge=0, le=255)
    ):
    gamepad.rightXAxis(x)
    gamepad.rightYAxis(y)
    return "Ok"

@app.post("/button_Y", tags=["button"])
def press_button_Y():
    gamepad.press(NSButton.Y)
    time.sleep(0.5)
    gamepad.release(NSButton.Y)
    return "Ok"


@app.post("/button_B", tags=["button"])
def press_button_B():
    gamepad.press(NSButton.B)
    time.sleep(0.5)
    gamepad.release(NSButton.B)
    return "Ok"


@app.post("/button_A", tags=["button"])
def press_button_A():
    gamepad.press(NSButton.A)
    time.sleep(0.5)
    gamepad.release(NSButton.A)
    return "Ok"

@app.post("/button_X", tags=["button"])
def press_button_X():
    gamepad.press(NSButton.X)
    time.sleep(0.5)
    gamepad.release(NSButton.X)
    return "Ok"

@app.post("/button_LEFT_TRIGGER", tags=["button"])
def press_button_LEFT_TRIGGER():
    gamepad.press(NSButton.LEFT_TRIGGER)
    time.sleep(0.5)
    gamepad.release(NSButton.LEFT_TRIGGERX)
    return "Ok"
 
@app.post("/button_RIGHT_TRIGGER", tags=["button"])
def press_button_RIGHT_TRIGGER():
    gamepad.press(NSButton.RIGHT_TRIGGER)
    time.sleep(0.5)
    gamepad.release(NSButton.RIGHT_TRIGGER)
    return "Ok"
 
@app.post("/button_LEFT_THROTTLE", tags=["button"])
def press_button_LEFT_THROTTLE():
    gamepad.press(NSButton.LEFT_THROTTLE)
    time.sleep(0.5)
    gamepad.release(NSButton.LEFT_THROTTLE)
    return "Ok"
 
@app.post("/button_RIGHT_THROTTLE", tags=["button"])
def press_button_X():
    gamepad.press(NSButton.RIGHT_THROTTLE)
    time.sleep(0.5)
    gamepad.release(NSButton.RIGHT_THROTTLE)
    return "Ok"
 
@app.post("/button_MINUS", tags=["button"])
def press_button_X():
    gamepad.press(NSButton.MINUS)
    time.sleep(0.5)
    gamepad.release(NSButton.MINUS)
    return "Ok"
  
@app.post("/button_PLUS", tags=["button"])
def press_button_PLUS():
    gamepad.press(NSButton.PLUS)
    time.sleep(0.5)
    gamepad.release(NSButton.PLUS)
    return "Ok"

@app.post("/button_LEFT_STICK", tags=["button"])
def press_button_LEFT_STICK():
    gamepad.press(NSButton.LEFT_STICK)
    time.sleep(0.5)
    gamepad.release(NSButton.LEFT_STICK)
    return "Ok"

@app.post("/button_RIGHT_STICK", tags=["button"])
def press_button_RIGHT_STICK():
    gamepad.press(NSButton.RIGHT_STICK)
    time.sleep(0.5)
    gamepad.release(NSButton.RIGHT_STICK)
    return "Ok"
  
@app.post("/button_HOME", tags=["button"])
def press_button_X():
    gamepad.press(NSButton.HOME)
    time.sleep(0.5)
    gamepad.release(NSButton.HOME)
    return "Ok"
 
@app.post("/button_CAPTURE", tags=["button"])
def press_button_CAPTURE():
    gamepad.press(NSButton.CAPTURE)
    time.sleep(0.5)
    gamepad.release(NSButton.CAPTURE)
    return "Ok"

@app.post("/connect_controller", tags=["meta"])
def connect_controller():
    gamepad.press(NSButton.RIGHT_THROTTLE)
    gamepad.press(NSButton.LEFT_THROTTLE)
    time.sleep(2)
    gamepad.release(NSButton.RIGHT_THROTTLE)
    gamepad.release(NSButton.LEFT_THROTTLE)
    time.sleep(0.9)
    return "Ok"

@app.post("/release_buttons", tags=["meta"])
def release_button():
    gamepad.releaseAll()
    return "Ok"
