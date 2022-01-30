FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./spelling_bee /code/spelling_bee

CMD ["uvicorn", "spelling_bee.main:app", "--host", "0.0.0.0", "--port", "80"]
