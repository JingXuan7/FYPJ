from wtforms import Form, StringField, RadioField, DateField, DecimalField, IntegerField, validators
import re


class PredictionForm(Form):
    Mileage = IntegerField('Mileage', [validators.DataRequired()])  # need to know if its possible to have decimal for mileage
    Transmission = RadioField('Transmission', choices=[('A', 'Auto'), ('M', 'Manual'), validators.DataRequired()])
    Vehicle_Make = StringField('Vehicle Make (brand)',[validators.Length(min=1, max=150), validators.DataRequired()])
    Vehicle_Model = StringField('Vehicle Model',[validators.DataRequired()])
    Open_Market_Value = DecimalField('Open Market Value($)', [validators.DataRequired()])
    First_Registration_Date = DateField('Date of First Registration', format='%Y-%m-%d', validators=[validators.DataRequired()])  # find date format from excel to match
    Actual_ARF_Paid = DecimalField('ARF Paid($)', places=[2, validators.DataRequired()])  # double chk whether needed
    COE_Category = RadioField('COE Category', choices=[('A', 'Class A'), ('B', 'Class B'), ('C', 'Class C'), validators.DataRequired()])
    COE_Period = IntegerField('COE Period', [validators.DataRequired()])
    Propellant = RadioField('Propellant', [validators.DataRequired()], choices=['Petrol', 'Diesel', 'Electric'], default='')
    Engine_Capacity = IntegerField('Engine Capacity (CC)', [validators.DataRequired()])
    Selected_Price = IntegerField('Price paid for COE($)', [validators.DataRequired()])
