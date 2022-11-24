FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN mkdir tmp_images
RUN mkdir tmp_result
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
