## How to use to collect dynamic websit(with docker and splash)

1. First run docker in terminal

```
$ docker run -p 8050:8050 scrapinghub/splash
```

2. Run crawler

```
scrapy crawl sneaker -o (filename)
```

3. Import to database

```
python3 importToDb.py
```

## Two crawlers(one for upcomings, one for already released)

1. Both use the splash so running docker splash first
2. In sneaker.py uncomment program is used for released sneakers, comments are program to collect data from upcomings.
