class PatientFileManager:
    def __init__(self):
        self.__patients = {}
        
    def _add_patient(self, patient_id, data):
        self.__patients[patient_id] = data
        
    def _get_patient(self, patient_id):
        return self.__patients[patient_id]


class AccessManager(PatientFileManager):
    def __init__(self, fm):
        self.fm = fm
    
    def add_patient(self, patient_id, data, password):
        if password == 'sudo':
            self.fm._add_patient(patient_id, data)
        else:
            print("Wrong password.")
            
    def get_patient(self, patient_id, password):
        if password == 'totallytheirdoctor' or password == 'sudo':
            return self.fm._get_patient(patient_id)
        else:
            print("Only their doctor can access this patients data.")


am = AccessManager(PatientFileManager())
am.add_patient('Jessica', ['pneumonia 2020-23-03', 'shortsighted'], 'sudo')

print(am.get_patient('Jessica', 'totallytheirdoctor'))