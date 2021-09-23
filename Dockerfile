FROM python:3.9-alpine
COPY minesweeper.py .

ENTRYPOINT ["python3","./minesweeper.py"]