#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/19 13:43
# @Author : Zhibin
# @Description : 通知服务入口文件
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
