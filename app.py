from flask import Flask , render_template, request
import pickle

app=Flask(__name__)
model=pickle.load(open('classifer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        pH = float(request.form['pH'])
        rainfall = float(request.form['rainfall'])

        input_features = [[Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, rainfall]]
        prediction = model.predict(input_features)

        return render_template('index.html', prediction_text='Predicted Crop: {}'.format(prediction[0]))


if __name__ == '__main__':
    app.run(debug=True)


