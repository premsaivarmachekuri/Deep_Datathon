from flask import Flask, render_template, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict
import pickle
import pandas as pd
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      # print(result)
      # print(result)
      values = [value for value in result.values()]
      # print(values)
      # Convert values to float
      x = [float(i) for i in values]
      x[0] = int(x[0])
      # print(x)
      # columns = ["GENDER", "WBC", "Platelets", "Neutrophils", "Lymphocytes", "Monocytes", "Eosinophils", "Basophils", "CRP", "AST", "ALT", "ALP", "GGT", "LDH"]
      # df = pd.DataFrame([x], columns=columns)  # Create a DataFrame with the row data
      # df.index = None  # Remove the index
      # print(df)
      # with open('/home/prem/data-miners/finalized_model.sav', 'rb') as file:  
      #    model = pickle.load(file)
      # csv_file_path = 'without_index.csv'
      # data = pd.read_csv(csv_file_path)
      # test = data.loc[0]
      # if isinstance(test, pd.DataFrame):
      #    print("df is a DataFrame")
      # else:
      #    print("df is not a DataFrame")
      # print(test)

      ## Code
      columns = ["GENDER", "WBC", "Platelets", "Neutrophils", "Lymphocytes", "Monocytes", "Eosinophils", "Basophils", "CRP", "AST", "ALT", "ALP", "GGT", "LDH"]
      df = pd.DataFrame([x], columns=columns) 
      print(df)
      loaded_model = pickle.load(open('/home/prem/data-miners/finalized_model.sav', 'rb'))
      output = loaded_model.predict(df)


      # output = model.predict(data).tolist()  # Convert predictions to a list

        # Return predictions as JSON
      # return str(output)
    #   m1=
    #   out=m1.predict()
      # return output
      res = 'Positive' if output[0] == 1 else 'Negative'
      return render_template("student.html",result = res)

if __name__ == '__main__':
   app.run(debug = True)