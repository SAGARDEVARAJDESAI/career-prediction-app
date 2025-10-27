from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('../model/career_model.pkl')



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Get input values safely
            python_skill = int(request.form.get('python', 0))
            java_skill = int(request.form.get('java', 0))
            sql_skill = int(request.form.get('sql', 0))
            interest_ai = int(request.form.get('ai', 0))
            interest_web = int(request.form.get('web', 0))
            comm_score = int(request.form.get('comm', 0))

            # Basic validation
            values = [python_skill, java_skill, sql_skill, interest_ai, interest_web, comm_score]
            if any(v < 1 or v > 10 for v in values):
                raise ValueError("All values must be between 1 and 10.")

            # Prepare input for model
            input_data = np.array([values])

            # Predict career
            prediction = model.predict(input_data)[0]

            return render_template('index.html', result=prediction)

        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
