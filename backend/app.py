import pickle
from flask import Flask, request, jsonify


#loading the final model
model_file='model/final_model.bin'

with open(model_file, 'rb') as f_in:
    dv,model = pickle.load(f_in)

most_important_features=[
    'limb_movement',
    'sleeping_hours',
    'snoring_rate',
    'eye_movement',
    'body_temperature'
]

app=Flask('stress_level')#'stress_level to __name__
@app.route('/predict', methods=['POST'])

def predict():
    data = request.get_json()
    #only get expected features in the right order
    try:
        input_data={key:data[key] for key in most_important_features}
    except KeyError as e:
        return jsonify({'error':f'Missing feature:{e}'}), 400
    X = dv.transform([input_data])
    y_pred=model.predict(X)

    #return the prediction
    return jsonify({'stress_level': int(y_pred[0])})#fix

#running the server
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
#change the port

                        
