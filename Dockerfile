FROM python:3.9
WORKDIR /parserapp
COPY . /parserapp
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "Problem1.py"]
