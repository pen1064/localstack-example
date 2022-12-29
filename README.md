# meow testing localstack and pytest
Why localstack?

It can be expensive to test the whole service on AWS platform


1. Set up the container

```
docker-compose up
```

In the docker file, it is asking for both lambda and s3 services.
2. run unit test for simple lambda function
```
cd simple_lambda
pytest test_lambda.py
```

3. run unit test for lambda function which put some simple item into s3
```
cd s3_lambda
pytest test_lambda.oy
```
