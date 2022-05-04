from flask import Flask, render_template, request, redirect, url_for
from Forms import PredictionForm
import shelve, Predict

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    prediction_form = PredictionForm(request.form)
    if request.method == 'POST' and prediction_form.validate():
        return redirect(url_for('home'))
    return render_template('predictionForm.html', form=prediction_form)


# @app.route('/prediction', methods=['GET', 'POST'])
# def prediction():
#     prediction_form = PredictionForm(request.form)
#     if request.method == 'POST' and prediction_form.validate():
#         predicts_dict = {}
#         db = shelve.open('storage.db', 'c')
#
#         try:
#             predicts_dict = db['Predicts']
#         except:
#             print("Error in retrieving Users from storage.db.")
#
#         predict = Predict.Predict(prediction_form.Mileage.data, prediction_form.Transmission.data,
#                                   prediction_form.Vehicle_Make.data, prediction_form.Vehicle_Model.data,
#                                   prediction_form.Open_Market_Value.data, prediction_form.First_Registration_Date.data,
#                                   prediction_form.Actual_ARF_Paid.data, prediction_form.COE_Category.data,
#                                   prediction_form.COE_Period.data, prediction_form.Propellant.data,
#                                   prediction_form.Engine_Capacity.data, prediction_form.Selected_Price.data)
#         predicts_dict[predict.get_predict_id()] = predict
#         db['Predicts'] = predicts_dict
#
#         # Test codes
#         predicts_dict = db['Users']
#         user = predicts_dict[predict.get_predict_id()]
#         print(user.get_first_name(), user.get_last_name(), "was stored in storage.db successfully with user_id ==",
#               user.get_user_id())
#
#         db.close()
#
#         return redirect(url_for('home'))
#     return render_template('predictionForm.html', form=prediction_form)


if __name__ == '__main__':
    app.run()
