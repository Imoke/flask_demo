# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7

EXPOSE 9006

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

# During debugging, this entry point will be overridden. For more information, refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "hello_app.webapp:app"]
CMD [ "gunicorn", "hello_app.webapp:app", "-c", "./gunicorn.conf.py" ]