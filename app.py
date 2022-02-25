from flask import Flask,render_template,app, request
import pandas as pd
import pickle as pkl

app=Flask(__name__,template_folder="templates")

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":
        try:
            gre_score=float(request.form["gre_score"])
            toefl_score=float(request.form["toefl_score"])
            university_rating=float(request.form["university_rating"])
            sop=float(request.form["sop"])
            lor=float(request.form["lor"])
            cgpa=float(request.form["cgpa"])
            is_research=request.form["research"]
            if (is_research=="yes"):
                research=1
            else:
                research=0
            filename="finalized_model.pickle"
            loaded_model = pkl.load(open(filename, 'rb')) # loading the model file from the storage

            prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            print('prediction is', prediction)
            
            return render_template('results.html',prediction=round(100*prediction[0]))

            
        except Exception as e :
            print("Exception occured",e)
            return "Something is wrong check debug ur backend code once again"
    else:
        render_template("index.html")

if __name__=="__main__":
    app.run(debug=False)
            
            
            
            