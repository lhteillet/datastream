FROM python:3.9.6
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY app1.py /app
CMD ["python", "app1.py"]