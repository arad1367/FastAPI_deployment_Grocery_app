# Prediction of Preferable Grocery App in Hungary
This FastAPI application is designed to predict the preferable grocery app in Hungary based on user inputs such as age, gender, education level, 
years of experience with online shopping, and years of experience with using grocery apps.

## How to Run
To run the application, use the following command:
`uvicorn FastAPI:app --reload`

Once the server is running, you can access the interactive API documentation at:
`http://localhost:8000/docs`

Alternatively, you can use the alternative API documentation at:
`http://localhost:8000/redoc`

## API Endpoints
- GET /: Returns information about the project, including its goal, version, and author.
- GET /predict: Endpoint for predicting the preferable grocery app based on user inputs. Requires the following parameters:
- age: Age of the user.
- gender: Gender of the user (1 for male, 2 for female).
- education: Education level of the user (1 for under diploma, 2 for associate, 3 for bachelor, 4 for master, 5 for PhD).
- exp_online: Years of experience with online shopping.
- exp_app: Years of experience with using grocery apps.

## Author
Pejman Ebrahimi

## Contact
email: `info@giltecg-support.co.uk` & `pejman.ebrahimi77@gmail.com`
website: `https://giltech-megoldasok.com/`
Hugging Face: `https://huggingface.co/arad1367`

# Happy code :)
