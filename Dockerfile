FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV DATABASE_URI=sqlite:///data.db
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]