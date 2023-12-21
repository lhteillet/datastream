FROM python:3.9.6
COPY requirements.txt .
# Install gcc and python3-dev for building certain Python packages 
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app2.py"]