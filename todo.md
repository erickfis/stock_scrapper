# TODO


## 2021-07-27

docker build -t sscrapper . -f Dockerfile.prod
docker run -it -p 8000:8000 sscrapper bash
uvicorn main:app
docker run --name scrapper-c -p 8000:8000 sscrapper
