import tkinter as tk
import joblib
from PIL import ImageTk, Image
from tkinter.font import Font

# Load the trained model
rf_model = joblib.load('rf_model.joblib')
# Define the feature variable names
feature_names = ['O2_hours_day', 'asthma', 'bronchitis_attack', 'pneumonia',
                 'chronic_bronchitis', 'emphysema', 'FEV1_FVC_ratio', 'FEV1', 'FVC', 'FEV1_phase2']


# Define a function to predict the output based on user input
def predict_output():
    # Get the user input values for the 10 feature variables
    feature_values = []
    for i in range(10):
        if i in range(1,6):
            feature_value = 1 if selected_options[i-1].get()=="Yes" else 0
            feature_values.append(feature_value)
        else:
            feature_value = float(feature_entries[i].get())
            feature_values.append(feature_value)


    output = rf_model.predict([feature_values])
    if output ==1:
        output="COPD Presence is Detected Be careful"
    else:
        output="COPD Presence is not Detected"
    # Display the predicted output
    output_label.config(text="COPD Prediction: " + str(output))
    if output=="COPD Presence is Detected Be careful":
        ratio = float(feature_entries[6].get())
        if ratio >= 0.70:
            Classification_result.config(text="Disease Classification:\t: COPD Disease is in MILD Stage")
            Personalized_management.config(text="Diagnosis Measures:\tQuit smoking (if applicable),"+"Avoid respiratory irritants,\n"+ "Regular physical exercise,"+
                          "Use bronchodilators as needed\n,"+ "Consider pulmonary rehabilitation,"+
                          "Get vaccinated against flu and pneumonia")
        elif ratio <=0.69 and ratio >=0.60:
            Classification_result.config(text="Disease Classification:\t:COPD Disease is in Moderate Stage")
            Personalized_management.config(text="Diagnosis Measures:\tQuit smoking (if applicable),"+ "Avoid respiratory irritants,\n"+"Regular physical exercise,"+
                          "Use bronchodilators on a regular basis,"+ "Consider pulmonary rehabilitation,\n"+
                          "Get vaccinated against flu and pneumonia,"+ "Consider oxygen therapy if needed")
        elif ratio >=0.50 and ratio<=0.59:
            Classification_result.config(text="Disease Classification:\t:COPD Disease is in Severe Stage")
            Personalized_management.config(text="Diagnosis Measures:\tQuit smoking (if applicable),"+ "Avoid respiratory irritants,\n"+ "Regular physical exercise,"+
                          "Use bronchodilators on a regular basis\n"+ "Consider pulmonary rehabilitation"+
                          "Get vaccinated against flu and pneumonia,\n"+"Consider oxygen therapy,"+
                          "Consider surgical interventions, such as lung volume reduction surgery or lung transplant")
        elif ratio <=0.50:
            Classification_result.config(text="Disease Classification:\tCOPD Disease is in Very Severe Stage")
            Personalized_management.config(text="Diagnosis Measures:\tQuit smoking (if applicable),"+ "Avoid respiratory irritants,\n"+"Regular physical exercise."+
                          "Use bronchodilators on a regular basis,\n"+ "Consider pulmonary rehabilitation,"+
                          "Get vaccinated against flu and pneumonia,\n"+ "Consider oxygen therapy,"+
                          "Consider end-of-life care planning")
    else:
        Classification_result.config(text="At Present You are free from COPD Disease")
        Personalized_management.config(text="You are Healthy at Present. Continue doing Exercises and Practice Good Health Habits")


# Create a tkinter window
window = tk.Tk()

window.title("COPD Disease Prediction using Random Forest Model")




window.config(bg="white")
font = Font(family="Arial", size=18)

heading_font = Font(family="Arial", size=16, weight="bold")
heading_label = tk.Label(window, text="COPD Disease Prediction", font=heading_font, bg="lightgray")
heading_label.grid(row=0, column=0, columnspan=2, pady=20)
# Create a label and text entry box for each feature variable
feature_entries = []
selected_options = []
for i in range(10):
    feature_label = tk.Label(window, text=feature_names[i] + ":",font=font)
    feature_label.grid(row=i+1, column=0,sticky="e")

    if i in range(1, 6):
        # Create a dropdown list for categorical variables
        options = ["Yes", "No"]
        selected_option = tk.StringVar(value=options[0])
        selected_options.append(selected_option)  # Store the associated variable
        feature_entry = tk.OptionMenu(window, selected_option, *options)
        feature_entry.config(font=font)
        #feature_entry = tk.OptionMenu(window, tk.StringVar(value=options[0]), *options)
    else:
        feature_entry = tk.Entry(window)

    feature_entry.grid(row=i+1, column=1,sticky="e",padx=100,pady=5)
    feature_entries.append(feature_entry)

# Create a button to predict the output based on user input
predict_button1 = tk.Button(window, text="Predict Output", command=predict_output,font=font)
predict_button1.grid(row=11, column=1,pady=50)

# Create a label to display the predicted output
output_label = tk.Label(window, text="",font=font)
output_label.grid(row=12, column=1,pady=10)

Classification_result =  tk.Label(window,text="",font=font)
Classification_result.grid(row=13,column=1,pady=10)
Personalized_management=tk.Label(window,text="",font=font)
Personalized_management.grid(row=14,column=1,pady=10)
window.mainloop()
