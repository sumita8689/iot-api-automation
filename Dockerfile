FROM python:3.13.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["sh", "-c", "python -m pytest -v && python -m behave"]