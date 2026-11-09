from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Device Job Manager")

DeviceStatus = Literal["online", "offline", "busy"]


class DeviceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    status: DeviceStatus = "offline"


class Device(DeviceCreate):
    id: int


# Temporary storage: data is lost when the server restarts
devices: dict[int, Device] = {}
next_id = 1


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/devices")
async def list_devices() -> list[Device]:
    return list(devices.values())


@app.get("/devices/{device_id}")
async def get_device(device_id: int) -> Device:
    device = devices.get(device_id)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@app.post("/devices", status_code=201)
async def create_device(payload: DeviceCreate) -> Device:
    global next_id

    device = Device(id=next_id, **payload.model_dump())
    devices[device.id] = device
    next_id += 1
    return device