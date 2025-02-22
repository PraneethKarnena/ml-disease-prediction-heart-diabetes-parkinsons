# ML Disease Predictor - Heart, Diabetes & Parkinson's

A very basic ML predictor for Heart, Diabetes and Parkinson's diseases.

## Running the project

1. Create a Python virtual environment: `python -m venv venv`
2. Activate the Python virtual environment (on Windows): `venv\Scripts\activate` 
3. Install project dependencies: `pip install -r requirements.txt`
4. Build the models:
    1. Install and configure `Jupyter`
    2. Run the notebooks inside the `train_models` directory
    3. After successfully running the notebooks, models would be created inside the `built-models` directory
4. Predict: `streamlit run predict.py`