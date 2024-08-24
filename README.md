# Resume-Classification-
## Resume Classifier Project
This project develops a machine learning model to classify resumes into categories based on the job descriptions. It utilizes several algorithms like Support Vector Machine (SVM), Multinomial Naive Bayes, Random Forest, and DistilBERT to achieve this.

## Table of Contents
- [Installation](#installation)
- [Data](#Data)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/Resume-Classification.git
    cd Resume-Classification
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Data 
The dataset for this project is collected by scraping resume data from LiveCareer.com. Approximately 8,350 resumes are collected across 10 job categories including Python Developer, Java Developer, Web Developer, Database Administrator, Security Analyst, Project Manager, Frontend Developer, Network Administrator, and Software Developer.

## Data Collection Process

Resumes are scraped using Selenium with the Chrome WebDriver. The process involves navigating to specific URLs constructed for each job category and extracting links to individual resumes. Here’s a brief outline of the steps involved in the scraping process:

Set up Selenium WebDriver: Configure Selenium with ChromeDriver to interact with web pages.
Navigate through job categories: For each category, generate URLs to navigate through pages of listings on LiveCareer.com.
Extract resume links: Collect the href attribute of each resume link on the listing pages.
Visit each resume link: For each extracted link, navigate to the corresponding page to access the full resume.
Extract resume text: Parse the HTML content of each resume page to extract the textual data.
Store data: Save the collected resume texts and their corresponding categories to a DataFrame, then export to a CSV file named Resume.csv.
This scraping process ensures the collection of a diverse and extensive dataset that represents various sectors in the job market, suitable for training our classification models.

## Data Structure

The resulting dataset comprises columns for Resume text and the corresponding Category. It's stored in a CSV file to facilitate easy access and manipulation for training machine learning models.

## Usage

1. Prepare the dataset by placing it in the `data/` directory.
2. Run the preprocessing script:
    ```bash
    python preprocess.py
    ```
3. Train the model:
    ```bash
    python train.py
    ```
4. Make predictions:
    ```bash
    python predict.py --resume path/to/resume.pdf
    ```

## Model Training

1. The model is trained using [scikit-learn](https://scikit-learn.org/) and [TensorFlow](https://www.tensorflow.org/).
2. The `train.py` script can be configured to adjust hyperparameters.

This project includes several classification models:

Support Vector Machine (SVM): Used for high accuracy in categorical classification.

Multinomial Naive Bayes: Effective for word counts or frequency data.

Random Forest: Provides a good benchmark for complex classification tasks.

DistilBERT: Not implemented in the project's current scope but recommended for future scaling to handle contextual embeddings from text data.

## Performance
The models are evaluated based on accuracy, precision, recall, and F1-score. Random Forest showed a significant performance with an accuracy of 83%, followed by SVM at 88% and Multinomial Naive Bayes at 79% and DistilBERT at 93%.
## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

