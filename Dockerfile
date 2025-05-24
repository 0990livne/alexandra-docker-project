FROM python:3.13.3-alpine3.21
WORKDIR /app
COPY HW.py .
RUN pip install --no-cache-dir Flask
EXPOSE 5000
CMD ["python", "HW.py"]