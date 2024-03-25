# run: uvicorn FastAPI:app --reload
# Interactive API docs: localhost:8000/docs
# Alternative API docs: localhost:8000/redoc

from fastapi import FastAPI, Query, HTTPException
import uvicorn
import os
import pickle

app = FastAPI(debug=True)

@app.get("/")
def home():
    return {
        "Project": "Prediction of preferable grocery app in Hungary",
        "Goal": "Educational App",
        "Version": "0.1.0",
        "Author": "Pejman Ebrahimi"
    }

@app.get("/predict")
def predict(age: int = Query(..., description="Age of the user"),
            gender: int = Query(..., description="Gender: 1 for male, 2 for female"),
            education: int = Query(..., description="Education level: 1 for under diploma, 2 for associate, 3 for bachelor, 4 for master, 5 for PhD"),
            exp_online: int = Query(..., description="Years of experience with online shopping"),
            exp_app: int = Query(..., description="Years of experience with using grocery apps")):
    """
    Predicts the grocery app based on user inputs.

    :param age: Age of the user.
    :param gender: Gender of the user (1 for male, 2 for female).
    :param education: Education level of the user (1 for under diploma, 2 for Associate, 3 for bachelor, 4 for master, 5 for PhD).
    :param exp_online: Years of experience with online shopping.
    :param exp_app: Years of experience with using grocery apps.
    """
    # Check if gender and education values are within allowed range
    if gender not in [1, 2] or education not in [1, 2, 3, 4, 5]:
        raise HTTPException(status_code=400, detail="Invalid input. Gender should be 1 or 2, and education should be between 1 and 5.")

    # Check if all inputs are integers
    if not all(isinstance(val, int) for val in [age, gender, education, exp_online, exp_app]):
        raise HTTPException(status_code=400, detail="Only integer inputs are allowed.")

    # Load model from absolute path
    app_names = ["FoodPanda", "Wolt", "Spar", "Tesco Online", "myLidl"]
    model_path = os.path.join(os.getcwd(), 'clfmodel.pkl')
    loaded_model = pickle.load(open(model_path, 'rb'))
    
    prediction = loaded_model.predict([[gender, education, age, exp_online, exp_app]])
    predicted_app = app_names[int(prediction[0])]
    
    return {'The predicted grocery app is': predicted_app}

if __name__ == "__main__":
    uvicorn.run(app)
