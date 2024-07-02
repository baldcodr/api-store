FROM python:3.9-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./api/ /code/api/
EXPOSE 8000
CMD ["fastapi", "run", "api/main.py"]