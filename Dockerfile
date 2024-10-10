# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3

# Cài đặt java
# RUN apt-get update && apt-get install -y openjdk-8-jdk wget curl

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Cấu hình môi trường spark
# ENV SPARK_HOME=/usr/local/spark
# ENV PATH=$SPARK_HOME/bin:$PATH

# Install pip requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.23.jar -P /usr/local/spark/jars

WORKDIR /usr/src/app
COPY . .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["sh", "-c", "sleep 60 && python -m scrapy runspider scrapyjob/spiders/myscraper.py"]
