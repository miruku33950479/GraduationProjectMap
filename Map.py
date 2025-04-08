from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

class Pin(BaseModel):
    lat: float
    lng: float
    title: str
    description: str

pins = []

# 創建圖釘的端點
@app.post("/pins/")
async def create_pin(pin: Pin):
    pins.append(pin)  # 儲存圖釘資料
    return pin  # 返回包含座標和圖片 URL 的圖釘資料

# 取得所有圖釘資料的端點
@app.get("/pins/", response_model=List[Pin])
async def read_pins():
    return pins

@app.post("/pins/")
async def create_pin(pin: Pin):
    pin_id = str(uuid4())  # 生成唯一的 ID
    new_pin = pin.dict()
    new_pin["id"] = pin_id
    pins.append(new_pin)
    return new_pin

@app.get("/pins/", response_model=List[Pin])
async def read_pins():
    return pins

@app.delete("/pins/{pin_id}")
async def delete_pin(pin_id: str):
    for pin in pins:
        if pin["id"] == pin_id:
            pins.remove(pin)
            return {"deleted": pin}
    raise HTTPException(status_code=404, detail="pin not found")
