from flask import Flask, render_template, request, send_file
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from datetime import datetime
from fpdf import FPDF

app = Flask(__name__)

# Loading the model
model = load_model('lung_cancer_detection_model.h5')

# Defining the classes
classes = ['Normal', 'Benign', 'Malignant']

# Creating a dictionary for patients' info
patient_data = {}

@app.route('/', methods= ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/diagnose', methods= ['POST'])
def predict():
    global patient_data
    
    # Getting the entered data from the form
    file = request.files.get('file')
    patient_name = request.form.get('name')
    patient_age = request.form.get('age')

    # Checking for missing files
    if not file or not patient_name or not patient_age:
        return "Missing Patient info or no file uploaded", 400

    # Saving the file temporarily to run through the model
    file_name = file.filename
    filepath = os.path.join('static', 'uploads', file_name)
    file.save(filepath)

    # Preprocessing the uploaded scan
    img = load_img(filepath, target_size= (128, 128), color_mode= 'grayscale')
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis= 0) # Adding patch dimension

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = classes[np.argmax(prediction)]

    # Storing the patient's info for the final report
    patient_data = {
        "name" : patient_name,
        "age" : patient_age,
        "prediction" : predicted_class,
        "confidence" : f"{np.max(prediction) * 100:.2f}%",
        "date" : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "file_name" : file_name
    }    

        # Rendering the result on the webpage
    return render_template('index.html',result= predicted_class)    

@app.route('/download-report', methods=['GET'])
def download_report():
    global patient_data

    if not patient_data:
        return "No Report to Download", 400
    
    # Generating the report as a PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', 'B', size=16)
    pdf.cell(0, 10, 'Lung Cancer Diagnosis Report', ln=True, align = 'C')
    pdf.ln(10)

    # Adding the patient's information
    pdf.set_font('Arial', size=12)
    pdf.cell(0, 10, f"Patient Name: {patient_data['name']}", ln=True)
    pdf.cell(0, 10, f"Patient Age: {patient_data['age']}", ln=True)
    pdf.cell(0, 10, f"Diagnosis: {patient_data['prediction']}", ln=True)
    pdf.cell(0,10, f"Confidence: {patient_data['confidence']}", ln=True)
    pdf.cell(0, 10, f"Date: {patient_data['date']}", ln=True)
    pdf.ln(10)

    # Adding the CT scan to the report
    ct_scan_path = os.path.join('static', 'uploads', patient_data['file_name'])
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'CT Scan: ', ln=True)
    pdf.ln(5)
    pdf.image(ct_scan_path, x = 10, y = None, w = 100)

    pdf.ln(20)
    pdf.cell(0, 10, "Thanks for using the Lung Cancer Diagnosis System!", ln=True)

    # Saving the PDF into a temporary file
    report_path = "static/report.pdf"
    pdf.output(report_path)

    # Sending the file to be available for download
    return send_file(report_path, as_attachment = True)

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    app.run(debug= True)