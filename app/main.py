from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
from random import randint
import uuid

from image_processing.processor import check_image_size

IMAGEDIR = "tmp_images/"

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):
    # No extension validation yet, accepts anything
    file.filename = f"{uuid.uuid4()}"
    contents = await file.read()

    destination_file = f"../{IMAGEDIR}{file.filename}"
    with open(destination_file, "wb") as f:
        f.write(contents)

    check_image_size(destination_file)

    return {"filename": file.filename}

