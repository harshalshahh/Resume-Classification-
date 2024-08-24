# Resume-Classification-
## Resume Classifier Project
This project develops a machine learning model to classify resumes into categories based on the job descriptions. It utilizes several algorithms like Support Vector Machine (SVM), Multinomial Naive Bayes, Random Forest, and DistilBERT to achieve this.

## Table of Contents
- [Installation](#installation)
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

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.

## License

This project is licensed under the MIT License.
