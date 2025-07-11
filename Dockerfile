FROM python:3.11-alpine
RUN pip install requests
ENV API_KEY=""
COPY run.py /run.py
CMD ["python", "/run.py"]