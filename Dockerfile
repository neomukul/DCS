# getting base image for docker
FROM python:3 


WORKDIR /home/neo/DCS
COPY . .


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000 

CMD ["python","hello.py"]

