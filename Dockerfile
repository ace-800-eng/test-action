FROM python

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 3000

CMD ["python", "app.py"]