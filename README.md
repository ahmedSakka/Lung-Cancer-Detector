# **Lung Cancer Detection System**

This project focuses on developing a machine learning-based web application to detect lung cancer from CT scan images. The system classifies the scans into three categories: **Normal**, **Benign**, and **Malignant**. The primary goal is to assist medical professionals with an accessible, reliable, and cost-effective diagnostic tool to aid early lung cancer detection.

---

## **Part 1: Machine Learning Model Development**

### **Data Collection**

The dataset used for training and evaluating the model is the **IQ-OTH/NCCD Lung Cancer Dataset**. It contains labeled CT scan images categorized into:
- **Normal**: 120 images  
- **Benign**: 561 images  
- **Malignant**: 416 images  

This dataset was preprocessed to ensure consistency and compatibility for machine learning model development.

---

### **Libraries Used**

The following Python libraries were utilized for data preprocessing, model training, and evaluation:
- **pandas**  
- **numpy**  
- **matplotlib**  
- **tensorflow**  
- **keras**  
- **sklearn**  

---

### **Data Preprocessing and Cleaning**

- The CT scan images were resized to **128x128** pixels to standardize input dimensions.  
- Pixel values were **normalized** to the range `[0, 1]` for optimal training.  
- Data augmentation techniques (e.g., flipping, rotation) were applied to enhance the dataset diversity and improve model generalization.  

---

### **Model Development**

A **Convolutional Neural Network (CNN)** was implemented using TensorFlow/Keras to classify the CT scan images. The model architecture consists of:  
- Convolutional layers for feature extraction.  
- Pooling layers to reduce dimensionality.  
- Dense layers for final classification into three categories.  

The model was trained using the **Adam optimizer** with a categorical cross-entropy loss function.

---

### **Model Evaluation**

The model achieved the following performance on the test dataset:  
- **Accuracy**: 97.6%  
- **Precision, Recall, and F1-Score**: Evaluated for all three classes.  

The classification report and confusion matrix provide detailed insights into the model's performance.  

---

## **Part 2: Web Application Development**

### **Framework and Tools**

The web application was built using Flask and integrates the trained CNN model for real-time predictions. Key tools and libraries include:
- **Flask**: Backend framework for handling user requests.  
- **HTML/CSS**: Frontend development for user interaction.  
- **ReportLab**: To generate downloadable PDF reports with diagnostic results.  
- **TensorFlow**: For loading and running the machine learning model.  

---

### **Features of the Web Application**

1. **CT Scan Upload**:  
   Users can upload CT scan images for analysis.  

2. **Real-time Prediction**:  
   The system classifies the uploaded scan as **Normal**, **Benign**, or **Malignant**, with confidence scores displayed alongside results.  

3. **Report Generation**:  
   Diagnostic results can be downloaded as a **PDF report** for medical records.  

4. **User-Friendly Interface**:  
   The web interface is designed to be intuitive and straightforward for medical professionals.

---

### **Usage**

To run the project locally, follow these steps:

1. **Install Required Libraries**:  
   Install the necessary libraries using `pip`:  
   ```bash pip install pandas numpy tensorflow flask matplotlib reportlab```
2. **Run the Flask Application**:  
   IExecute the `project.py` file to start the web server:  
   ```python project.py```
3. **Access the Web Interface**:  
   Open your browser and navigate to http://127.0.0.1:5000 to upload CT scans and view predictions.

### **Contributing**

Contributions are welcome! If you have suggestions for improving the system, enhancing the model, or adding new features to the web application, feel free to:

- **Open an issue.**
- **Submit a pull request.**

### **Author**

[Ahmed AlSakka](https://github.com/ahmedSakka)

---

### **References**

1. **IQ-OTH/NCCD Lung Cancer Dataset**  
   [Dataset Link](https://www.kaggle.com/datasets/hamdallak/the-iqothnccd-lung-cancer-dataset)

2. **TensorFlow Documentation**  
   [TensorFlow](https://www.tensorflow.org/)

3. **Flask Documentation**  
   [Flask](https://flask.palletsprojects.com/)

4. **ReportLab for PDF Generation**  
   [ReportLab](https://www.reportlab.com/)

---

### **Acknowledgements**

Special thanks to the developers of TensorFlow, Flask, and the contributors to the IQ-OTH/NCCD dataset for enabling this project.
