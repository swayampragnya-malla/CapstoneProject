from flask import Flask,render_template,request
import pickle 
import warnings


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        data=request.form
        satisfaction_level=data['satisfaction_level']
        last_evaluation=data['last_evaluation']
        number_project=data['number_project']
        average_monthly_hours=data['average_monthly_hours']
        time_spend_company=data['time_spend_company']
        work_acident=data['Work_accident']
        promotion_last_5years=data['promotion_last_5years']
        department=data['Department']
        salary=data['salary']
    
        user_input=[[float(satisfaction_level),float(last_evaluation),int(number_project),int(average_monthly_hours),int(time_spend_company),int(work_acident),int(promotion_last_5years),int(department),int(salary)]]
        filename=r"D:\\pragnya\\AIML\\Project\\CapstoneProject\\RandomForestModel.pkl"
        model = pickle.load(open(filename, 'rb'))
        warnings.filterwarnings("ignore", message="X does not have valid feature names")

        predicted_class = model.predict(user_input)
        if predicted_class[0] == 1:
            result = "Employee will leave"
        elif predicted_class[0] == 0:
            result = "Employee will not leave"
        else:
            result = "Cannot predict"
        return render_template('index.html', prediction=result)
     
         
if __name__=='__main__':
    app.run(debug=True)
