from flask import Flask, render_template, url_for, jsonify,request
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
    input_text=request.json.get("text")
   
    
    if not input_text:
        # Response to send if the input_text is undefined
        response={
            'status':"error",
            "message":"Please enter text to predict emotion"
        }
        return jsonify(response)
       
        
        # Response to send if the input_text is not undefined
    else:
        predicted_emotion,predicted_emotion_imagUrl=predict(input_text)
        response={
            'status':"success",
            "data":{
                "predicted_emotion":predicted_emotion,
                "predicted_emotion_imagUrl":predicted_emotion_imagUrl
            }
        }
        return jsonify(response)
        # Send Response         
        
if __name__==("__main__"):     
    app.run(debug=True)



    