# meow testing localstack and pytest 
Why localstack?

It can be expensive to test the whole service on AWS platform


1. Set up the container 

```
docker-compose up
```

2. run unit test
```
cd simple_lambda
pytest test_lambda.py
```

 
