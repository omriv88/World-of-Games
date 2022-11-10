FROM python:alpine
COPY main.py /app/
COPY Score1.txt /app/
RUN mkdir /app/templates
COPY Score1.html /app/templates
RUN pip install flask
CMD python /app/main.py
