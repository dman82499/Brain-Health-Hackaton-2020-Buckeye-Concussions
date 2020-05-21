  
import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


db = sqlite3.connect('patientdata.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS PHQ9(Questions TEXT, Symptoms INTEGER)")
db.commit()

class MyGrid(Widget):
    phq9=[]
    # for i in range(9):
    #     phq9.append(ObjectProperty(None))
    phq91 = ObjectProperty(None)
    phq92 = ObjectProperty(None)
    phq93 = ObjectProperty(None)
    phq94 = ObjectProperty(None)
    phq95 = ObjectProperty(None)
    phq96 = ObjectProperty(None)
    phq97 = ObjectProperty(None)
    phq98 = ObjectProperty(None)
    phq99 = ObjectProperty(None)
    symptoms = [phq91, phq92, phq93, phq94, phq95, phq96, phq97, phq98, phq99]
    def insert(self, symptoms):
        print(symptoms[1])
        # results=[]
        # for i in range(len(symptoms)):
        #     results.append(symptoms[i])
        #     conn = sqlite3.connect('patientdata.db')
        #     with conn:
        #         cursor = conn.cursor()
        #         cursor.execute('INSERT INTO Patient(Questions, Symptoms) VALUES(?,?)',
        #         (i+1, results[i]))  

class patientdata(App):

    def build(self):
        return MyGrid()


    


if __name__ == "__main__":
    patientdata().run()
