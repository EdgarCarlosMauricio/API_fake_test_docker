FROM python:3.8.3-alpine3.12
COPY . /API_fake_test_docker
WORKDIR /API_fake_test_docker
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]