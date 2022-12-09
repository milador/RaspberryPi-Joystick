"""
HTTP Fast API for 16 button joystick.
"""
from typing import Optional
import time
from fastapi import FastAPI,Path
from fastapi.middleware.cors import CORSMiddleware
from Joystick_16 import *

joystick = Joystick_16()
joystick.begin('/dev/hidg0')

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


@app.post('/stick_l', tags=["sticks"])
def lstick(
        x: int = Path(default=0,ge=-127, le=127),
        y: int = Path(default=0,ge=-127, le=127)
    ):
    joystick.leftXAxis(x)
    joystick.leftYAxis(y)
    return "Ok"

@app.post('/stick_r', tags=["sticks"])
def rstick(
        x: int = Path(default=0,ge=-127, le=127),
        y: int = Path(default=0,ge=-127, le=127)
    ):
    joystick.rightXAxis(x)
    joystick.rightYAxis(y)
    return "Ok"


@app.post("/button_0", tags=["button"])
def press_button_0():
    joystick.press(0)
    time.sleep(0.5)
    joystick.release(0)
    return "Ok"


@app.post("/button_1", tags=["button"])
def press_button_1():
    joystick.press(1)
    time.sleep(0.5)
    joystick.release(1)
    return "Ok"


@app.post("/button_2", tags=["button"])
def press_button_2():
    joystick.press(2)
    time.sleep(0.5)
    joystick.release(2)
    return "Ok"


@app.post("/button_3", tags=["button"])
def press_button_3():
    joystick.press(3)
    time.sleep(0.5)
    joystick.release(3)
    return "Ok"


@app.post("/button_4", tags=["button"])
def press_button_4():
    joystick.press(4)
    time.sleep(0.5)
    joystick.release(4)
    return "Ok"


@app.post("/button_5", tags=["button"])
def press_button_5():
    joystick.press(5)
    time.sleep(0.5)
    joystick.release(5)
    return "Ok"


@app.post("/button_6", tags=["button"])
def press_button_6():
    joystick.press(6)
    time.sleep(0.5)
    joystick.release(6)
    return "Ok"


@app.post("/button_7", tags=["button"])
def press_button_7():
    joystick.press(7)
    time.sleep(0.5)
    joystick.release(7)
    return "Ok"


@app.post("/button_8", tags=["button"])
def press_button_8():
    joystick.press(8)
    time.sleep(0.5)
    joystick.release(8)
    return "Ok"

@app.post("/button_9", tags=["button"])
def press_button_9():
    joystick.press(9)
    time.sleep(0.5)
    joystick.release(9)
    return "Ok"


@app.post("/button_10", tags=["button"])
def press_button_10():
    joystick.press(10)
    time.sleep(0.5)
    joystick.release(10)
    return "Ok"


@app.post("/button_11", tags=["button"])
def press_button_11():
    joystick.press(11)
    time.sleep(0.5)
    joystick.release(11)
    return "Ok"


@app.post("/button_12", tags=["button"])
def press_button_12():
    joystick.press(12)
    time.sleep(0.5)
    joystick.release(12)
    return "Ok"


@app.post("/button_13", tags=["button"])
def press_button_13():
    joystick.press(13)
    time.sleep(0.5)
    joystick.release(13)
    return "Ok"


@app.post("/button_14", tags=["button"])
def press_button_14():
    joystick.press(14)
    time.sleep(0.5)
    joystick.release(14)
    return "Ok"


@app.post("/button_15", tags=["button"])
def press_button_15():
    joystick.press(15)
    time.sleep(0.5)
    joystick.release(15)
    return "Ok"


@app.post("/button_16", tags=["button"])
def press_button_16():
    joystick.press(16)
    time.sleep(0.5)
    joystick.release(16)
    return "Ok"

@app.post("/release_buttons", tags=["meta"])
def release_button():
    joystick.releaseAll()
    return "Ok"
