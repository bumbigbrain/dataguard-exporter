

FROM python:latest
COPY . .
RUN pip install -r ./requirements.txt
CMD ["python3", "./src/main.py"]
EXPOSE 9110
