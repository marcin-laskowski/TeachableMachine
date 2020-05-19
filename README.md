# TeachableMachine
play with Teachable Machine sample code


## Goal
Detect whether I am drinking a coffee or not.


## Try it out

### 1. Download repository
`git clone https://github.com/mlaskowski17/TeachableMachine.git`

### 2. Go to directory with sample data
`cd TeachableMachine/sample_data/input`

### 3. Run model in terminal via Curl
```
curl -X POST "http://35.234.95.174/models/m2005192131117b39ee6ebec/run" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@1.jpg;type=image/jpeg"
```



## Sample output

### class A
```
{
    "probability": 0.9999974966049194,
    "class": "drinking_coffee"
}
```
### class B
```
{
    "probability": 0.9993939959959959,
    "class": "NOT_drinking_coffee"   
}
```