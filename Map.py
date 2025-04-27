from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from uuid import uuid4

app = FastAPI()

# 定義圖釘的資料格式
class Pin(BaseModel):
    lat: float
    lng: float
    title: str
    description: str

# 暫存所有圖釘（用字典格式來存ID）
pins: List[Dict] = []

# 新增圖釘
@app.post("/pins/")
async def create_pin(pin: Pin):
    pin_id = str(uuid4())  # 自動生成唯一 ID
    new_pin = pin.dict()
    new_pin["id"] = pin_id
    pins.append(new_pin)
    return new_pin

# 取得所有圖釘
@app.get("/pins/")
async def read_pins():
    return pins

# 刪除特定 ID 的圖釘
@app.delete("/pins/{pin_id}")
async def delete_pin(pin_id: str):
    for pin in pins:
        if pin["id"] == pin_id:
            pins.remove(pin)
            return {"deleted": pin}
    raise HTTPException(status_code=404, detail="pin not found")
