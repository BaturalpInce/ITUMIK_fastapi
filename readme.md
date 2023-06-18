## The Details
This API receive requests and respond with the related JSON data which will be taken from MongoDB.

## How to Use?
While the server is running, you can send requests and there are 4 request type that you can do currently.

- http://localhost:8000/api/topiclist

Provides all the topics with no values.

- http://localhost:8000/api/alldatalist

Provides the complete data containing all the floors.

- http://localhost:8000/api/Floor1

Provides all the desks on a spesific floor.

- http://localhost:8000/api/Floor1/Desk2

Provides a spesific desk on a spesific floor.

## How to Run?
Windows: 
conda create -n environment_name python=3.10 ; pip conda activate environment_name ; pip install -r requirements.txt ; uvicorn main:app --reload

Linux:
conda create -n environment_name python=3.10 pip -y conda activate environment_name pip install -r requirements.txt -y uvicorn main:app --reload