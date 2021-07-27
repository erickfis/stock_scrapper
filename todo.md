# TODO


## 2021-07-27

docker build -t sscrapper . -f Dockerfile.prod
docker run -it sscrapper bash
docker run --name scraper-container -p 80:80 sscrapper
