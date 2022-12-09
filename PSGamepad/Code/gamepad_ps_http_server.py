"""
HTTP Fast API for PS Gamepad.
"""
from typing import Optional
import time
from fastapi import FastAPI,Path
from fastapi.middleware.cors import CORSMiddleware
from MFGamepad import *

Gamepad = MFGamepad()
Gamepad.begin('/dev/hidg0')

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

@app.post("/button_SQUARE", tags=["button"])
def press_button_SQUARE():
    gamepad.press(DS4Button.SQUARE)
    time.sleep(0.5)
    gamepad.release(DS4Button.SQUARE)
    return "Ok"


@app.post("/button_CROSS", tags=["button"])
def press_button_CROSS():
    gamepad.press(DS4Button.CROSS)
    time.sleep(0.5)
    gamepad.release(DS4Button.CROSS)
    return "Ok"


@app.post("/button_CIRCLE", tags=["button"])
def press_button_CIRCLE():
    gamepad.press(DS4Button.CIRCLE)
    time.sleep(0.5)
    gamepad.release(DS4Button.CIRCLE)
    return "Ok"

@app.post("/button_TRIANGLE", tags=["button"])
def press_button_TRIANGLE():
    gamepad.press(DS4Button.TRIANGLE)
    time.sleep(0.5)
    gamepad.release(DS4Button.TRIANGLE)
    return "Ok"

@app.post("/button_L1", tags=["button"])
def press_button_L1():
    gamepad.press(DS4Button.L1)
    time.sleep(0.5)
    gamepad.release(DS4Button.L1)
    return "Ok"
 
@app.post("/button_R1", tags=["button"])
def press_button_R1():
    gamepad.press(DS4Button.R1)
    time.sleep(0.5)
    gamepad.release(DS4Button.R1)
    return "Ok"
 
@app.post("/button_L2", tags=["button"])
def press_button_L2():
    gamepad.press(DS4Button.L2)
    time.sleep(0.5)
    gamepad.release(DS4Button.L2)
    return "Ok"
 
@app.post("/button_R2", tags=["button"])
def press_button_R2():
    gamepad.press(DS4Button.R2)
    time.sleep(0.5)
    gamepad.release(DS4Button.R2)
    return "Ok"
 
@app.post("/button_SHARE", tags=["button"])
def press_button_SHARE():
    gamepad.press(DS4Button.SHARE)
    time.sleep(0.5)
    gamepad.release(DS4Button.SHARE)
    return "Ok"
  
@app.post("/button_OPTIONS", tags=["button"])
def press_button_OPTIONS():
    gamepad.press(DS4Button.OPTIONS)
    time.sleep(0.5)
    gamepad.release(DS4Button.OPTIONS)
    return "Ok"

@app.post("/button_L3", tags=["button"])
def press_button_L3():
    gamepad.press(DS4Button.L3)
    time.sleep(0.5)
    gamepad.release(DS4Button.L3)
    return "Ok"

@app.post("/button_R3", tags=["button"])
def press_button_R3():
    gamepad.press(DS4Button.R3)
    time.sleep(0.5)
    gamepad.release(DS4Button.R3)
    return "Ok"
  
@app.post("/button_LOGO", tags=["button"])
def press_button_LOGO():
    gamepad.press(DS4Button.LOGO)
    time.sleep(0.5)
    gamepad.release(DS4Button.LOGO)
    return "Ok"
 
@app.post("/button_TPAD", tags=["button"])
def press_button_CAPTURE():
    gamepad.press(DS4Button.TPAD)
    time.sleep(0.5)
    gamepad.release(DS4Button.TPAD)
    return "Ok"

@app.post("/connect_controller", tags=["meta"])
def connect_controller():
    gamepad.press(DS4Button.R2)
    gamepad.press(DS4Button.L2)
    time.sleep(2)
    gamepad.release(DS4Button.R2)
    gamepad.release(DS4Button.L2)
    time.sleep(0.9)
    return "Ok"

@app.post("/release_buttons", tags=["meta"])
def release_button():
    gamepad.releaseAll()
    return "Ok"