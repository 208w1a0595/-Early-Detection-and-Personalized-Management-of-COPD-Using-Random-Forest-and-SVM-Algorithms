import tkinter as tk
import joblib

# Load the trained model
rf_model = joblib.load('svm_model.joblib')
# Define the feature variable names
feature_names = ['O2_hours_day', 'asthma', 'bronchitis_attack', 'pneumonia',
                 'chronic_bronchitis', 'emphysema', 'FEV1_FVC_ratio', 'FEV1', 'FVC', 'FEV1_phase2']





# Define a function to predict the output based on user input
def predict_output():
    # Get the user input values for the 10 feature variables
    feature_values = []
    for i in range(10):
        if i in range(1,6):
            if feature_entries[i].get()=='Yes':
                feature_values.append(1)
            else:
                feature_values.append(0)
        else:
            feature_value = float(feature_entries[i].get())
            feature_values.append(feature_value)

    # Use the loaded model to predict the output
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
            Classification_result.config(text="COPD Disease is in MILD Stage")
            Personalized_management.config(text="Quit smoking (if applicable),"+"Avoid respiratory irritants,"+ "Regular physical exercise,"+
                          "Use bronchodilators as needed,"+ "Consider pulmonary rehabilitation,"+
                          "Get vaccinated against flu and pneumonia")
        elif ratio <=0.69 and ratio >=0.60:
            Classification_result.config(text="COPD Disease is in Moderate Stage")
            Personalized_management.config(text="Quit smoking (if applicable),"+ "Avoid respiratory irritants,"+"Regular physical exercise,"+
                          "Use bronchodilators on a regular basis,"+ "Consider pulmonary rehabilitation,"+
                          "Get vaccinated against flu and pneumonia,"+ "Consider oxygen therapy if needed")
        elif ratio >=0.50 and ratio<=0.59:
            Classification_result.config(text="COPD Disease is in Severe Stage")
            Personalized_management.config(text="Quit smoking (if applicable),"+ "Avoid respiratory irritants,"+ "Regular physical exercise,"+
                          "Use bronchodilators on a regular basis"+ "Consider pulmonary rehabilitation"+
                          "Get vaccinated against flu and pneumonia,"+"Consider oxygen therapy,"+
                          "Consider surgical interventions, such as lung volume reduction surgery or lung transplant")
        elif ratio <=0.50:
            Classification_result.config(text="COPD Disease is in Very Severe Stage")
            Personalized_management.config(text="Quit smoking (if applicable),"+ "Avoid respiratory irritants,"+"Regular physical exercise."+
                          "Use bronchodilators on a regular basis,"+ "Consider pulmonary rehabilitation,"+
                          "Get vaccinated against flu and pneumonia,"+ "Consider oxygen therapy,"+
                          "Consider end-of-life care planning")
    else:
        Classification_result.config(text="At Present You are free from COPD Disease")
        Personalized_management.config("You are Healthy at Present. Continue doing Exercises and Practice Good Health Habits")


# Create a tkinter window
window = tk.Tk()

window.title("COPD Disease Prediction using SVM Machine Learning Model")


# Create a label and text entry box for each feature variable
feature_entries = []
for i in range(10):
    feature_label = tk.Label(window, text=feature_names[i] + ":")
    feature_label.grid(row=i, column=0)

    feature_entry = tk.Entry(window)
    feature_entry.grid(row=i, column=1)
    feature_entries.append(feature_entry)

# Create a button to predict the output based on user input
predict_button = tk.Button(window, text="Predict Output", command=predict_output)
predict_button.grid(row=10, column=1)

# Create a label to display the predicted output
output_label = tk.Label(window, text="")
output_label.grid(row=11, column=1)
Classification_result =  tk.Label(window,text="")
Classification_result.grid(row=12,column=1)
Personalized_management=tk.Label(window,text="")
Personalized_management.grid(row=13,column=1)
window.mainloop()
