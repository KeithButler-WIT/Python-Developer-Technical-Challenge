# aws-python-technical-challenge
An implementation of a simple Python API in AWS using an API Gateway, Lambda and DynamoDB.


# local setup

Deploy DynamoDB in Docker
```
docker network create technical-challenge
docker run --network technical-challenge --name dynamodb -d -p 8000:8000 amazon/dynamodb-local
aws dynamodb create-table --table-name documentTable --attribute-definitions AttributeName=chassis_no,AttributeType=S AttributeName=id,AttributeType=N --key-schema AttributeName=chassis_no,KeyType=HASH AttributeName=id,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --endpoint-url http://localhost:8000
```

<!-- aws dynamodb create-table --table-name documentTable --attribute-definitions AttributeName=make,AttributeType=S AttributeName=model,AttributeType=S AttributeName=year,AttributeType=S AttributeName=chassis_no,AttributeType=S AttributeName=id,AttributeType=N AttributeName=last_updated,AttributeType=S AttributeName=price,AttributeType=N --key-schema AttributeName=chassis_no,KeyType=HASH AttributeName=id,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --endpoint-url http://localhost:8000 -->

Build SAM application
```
sam build --use-container
```

Invoke load data function to load data in DynamoDB and verify
```
sam local invoke LoadDataFunction --parameter-overrides ParameterKey=Environment,ParameterValue=local ParameterKey=DDBTableName,ParameterValue=documentTable --docker-network technical-challenge
aws dynamodb scan --table-name documentTable --endpoint-url http://localhost:8000
```

Start local API Gateway
```
sam local start-api --parameter-overrides ParameterKey=Environment,ParameterValue=local ParameterKey=DDBTableName,ParameterValue=documentTable --docker-network technical-challenge
```


# Resources

- [Local dynamoDB](https://betterprogramming.pub/how-to-deploy-a-local-serverless-application-with-aws-sam-b7b314c3048c)
- [12 factor apps principles](https://betterprogramming.pub/how-to-deploy-a-local-serverless-application-with-aws-sam-b7b314c3048c)
