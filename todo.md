# TODO

## 2021-07-30

- gunicorn sem uvicorn - falhou por causa do async

      exec gunicorn --timeout 1000 --bind 0.0.0.0:8000 main:app


- uvicorn com timeout - ok!

      uvicorn main:app --host 0.0.0.0 --port 8000 --timeout-keep-alive 20


## 2021-07-29

Demo


## 2021-07-28

- prepare readme
