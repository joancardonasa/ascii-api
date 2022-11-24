import logging
import os
import uuid

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from PIL import Image, UnidentifiedImageError

from image_processing.processor import process_image

logger = logging.getLogger(__name__)

IMAGEDIR = 'tmp_images/'
app = FastAPI()


@app.get('/')

def read_root():
    return {'Hello': 'World'}


@app.post('/images/')
async def create_upload_file(file: UploadFile = File(...)):
    file.filename = f'{uuid.uuid4()}'
    contents = await file.read()

    destination_file = f'../{IMAGEDIR}{file.filename}'
    with open(destination_file, 'wb') as f:
        f.write(contents)

    try:
        raw_im = Image.open(destination_file)
    except UnidentifiedImageError:
        error_msg = 'File is not an image file'
        raise HTTPException(status_code=400, detail=error_msg)

    process_image(raw_im)

    return {'filename': file.filename}
