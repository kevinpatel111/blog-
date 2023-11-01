FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir /myapp
WORKDIR /myapp
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
# EXPOSE 8000
# CMD [ "python", "manage.py" ,"runserver" ]