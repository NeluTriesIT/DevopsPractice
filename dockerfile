FROM python:3.12-slim

WORKDIR /usr/src/app

COPY task1.py ./

ENV METHOD=0
ENV LIST_NUMBERS=0

CMD ["python3", "task1.py"]