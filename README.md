# WeatherCrimeHouston

## Getting Started

Follow these steps to get the "WeatherCrimeHouston" project up and running on your local machine.

### Prerequisites

- Git
- Conda (Anaconda/Miniconda)
- Python 3.9 or 3.10

### Installation

1. Clone the repository to your local machine:

    ```shell
    git clone https://dagshub.com/XuanQin/WeatherCrimeHouston.git
    ```

2. Open your terminal and navigate to the project directory:

    ```shell
    cd WeatherCrimeHouston
    ```

3. Create a new Conda environment (replace `myenv` with your preferred environment name):

    ```shell
    conda create -n myenv python=3.9
    ```

4. Activate the Conda environment:

    ```shell
    conda activate myenv
    ```

5. Install the required Python packages:

    ```shell
    pip install -r requirements.txt
    ```

### Running the App

To run the application, use the following command:

```shell
streamlit run app.py
```

### Optional: Retraining the Model

If you want to retrain the model, use the following steps:

1. Make sure you have activated your Conda environment (if not already activated):

    ```shell
    conda activate myenv
    ```

2. Navigate to the `src/WeatherCrimeHouston/pipeline` directory:

    ```shell
    cd src/WeatherCrimeHouston/pipeline
    ```

3. Run the model retraining script:

    ```shell
    python train_pipeline.py
    ```

This will retrain the model using the specified data.

## Contributors

- [Milan Kumar Behera](https://github.com/milanbeherazyx) - [Dagshub Profile](https://dagshub.com/milanbeherazyx)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.