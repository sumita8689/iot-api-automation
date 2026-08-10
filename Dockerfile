FROM python:3.13.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-m", "pytest", "-v"]