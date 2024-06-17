# Mango Quality Analysis System

Welcome to the Mango Quality Analysis System! This project leverages machine learning to analyze and classify mango images into "Good Quality" or "Bad Quality" categories. 
Whether you're a researcher, developer, or mango enthusiast, this system provides a powerful tool for assessing mango quality using advanced image analysis techniques.

<p>&nbsp;</p>

## Table of Contents

<ul>
    <li>Introduction</li>
    <li>Features</li>
    <li>Getting Started</li>
    <li>Prerequisites</li>
    <li>Installation</li>
    <li>Usage</li>
    <li>Training the Model</li>
    <li>Using the Model</li>
    <li>Dataset</li>
    <li>Results</li>
</ul>

## Introduction
The Mango Quality Analysis System uses a machine learning model to classify mango images based on their quality. 
This project aims to assist farmers, vendors, and consumers in ensuring that they get the best quality mangoes by leveraging modern image processing and deep learning techniques.

## Features
<li>Image Classification: Categorize mango images into "Good Quality" or "Bad Quality".</li>
<li>Model Training: Train a custom model using your own dataset of mango images.</li>
<li>REST API: Easily integrate the system with other applications via a RESTful API.</li>
<li>Visualization: Visualize the results and model performance using various metrics.</li>

## Getting Started
### Prerequisites
<li>Python 3.7+</li>
<li>pip (Python package installer)</li>
<li>Git (for cloning the repository)</li>

Installation
Clone the Repository

### bash
git clone https://github.com/yourusername/mango-quality-analysis.git
cd mango-quality-analysis
Create a Virtual Environment

### bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies

bash
pip install -r requirements.txt
Download Dataset
    
### Usage
### Training the Model
Configure the Training Settings

Open config.yaml and set your training parameters, such as batch size, number of epochs, and learning rate.

### Start Training

bash
python train.py
This command will train a convolutional neural network on your dataset and save the model to the models directory.

## Using the Model
Run the API Server

uvicorn app:app --host 0.0.0.0 --port 8000
Send a Request

You can send an image to the API to get the quality classification:

curl -X POST "http://localhost:8000/analyze" -F "image=@path/to/mango_image.jpg"
The API will respond with a JSON object containing the classification result.

## Dataset
The dataset should consist of mango images classified into two categories: "Good" and "Bad". Ensure that the images are well-labeled and organized into separate directories as described in the Installation section.

## Results
The system provides detailed metrics on model performance, including accuracy, precision, recall, and confusion matrix visualization. Results will be saved in the results directory after training.

<p>&nbsp;</p>
<p>&nbsp;</p>
Thank you for using the Mango Quality Analysis System! We hope it helps you ensure the best quality mangoes.
