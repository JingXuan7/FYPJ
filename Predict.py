class Predict:
    count_id = 0

    def __init__(self, Mileage, Transmission, Vehicle_Make, Vehicle_Model, Open_Market_Value, First_Registration_Date,
                 Actual_ARF_Paid, COE_Category, COE_Period, Propellant, Engine_Capacity, Selected_Price):
        Predict.count_id += 1
        self.__predict_id = Predict.count_id
        self.__Mileage = Mileage
        self.__Transmission = Transmission
        self.__Vehicle_Make = Vehicle_Make
        self.__Vehicle_Model = Vehicle_Model
        self.__Open_Market_Value = Open_Market_Value
        self.__First_Registration_Date = First_Registration_Date
        self.__Actual_ARF_Paid = Actual_ARF_Paid
        self.__COE_Category = COE_Category
        self.__COE_Period = COE_Period
        self.__Propellant = Propellant
        self.__Engine_Capacity = Engine_Capacity
        self.__Selected_Price = Selected_Price

    def get_predict_id(self):
        return self.__predict_id

    def get_Mileage(self):
        return self.__Mileage

    def get_Transmission(self):
        return self.__Transmission

    def get_Vehicle_Make(self):
        return self.__Vehicle_Make

    def get_Vehicle_Model(self):
        return self.__Vehicle_Model

    def get_Open_Market_Value(self):
        return self.__Open_Market_Value

    def get_First_Registration_Date(self):
        return self.__First_Registration_Date

    def get_Actual_ARF_Paid(self):
        return self.__Actual_ARF_Paid

    def get_COE_Category(self):
        return self.__COE_Category

    def get_COE_Period(self):
        return self.__COE_Period

    def get_Propellant(self):
        return self.__Propellant

    def get_Engine_Capacity(self):
        return self.__Engine_Capacity

    def get_Selected_Price(self):
        return self.__Selected_Price

    def set_Mileage(self):
        return self.__Mileage

    def set_Transmission(self):
        return self.__Transmission

    def set_Vehicle_Make(self):
        return self.__Vehicle_Make

    def set_Vehicle_Model(self):
        return self.__Vehicle_Model

    def set_Open_Market_Value(self):
        return self.__Open_Market_Value

    def set_First_Registration_Date(self):
        return self.__First_Registration_Date

    def set_Actual_ARF_Paid(self):
        return self.__Actual_ARF_Paid

    def set_COE_Category(self):
        return self.__COE_Category

    def set_COE_Period(self):
        return self.__COE_Period

    def set_Propellant(self):
        return self.__Propellant

    def set_Engine_Capacity(self):
        return self.__Engine_Capacity

    def set_Selected_Price(self):
        return self.__Selected_Price
