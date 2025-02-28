# Real Time Distributed Trading System

## Installation Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate 
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure Kaggle API:
    Download your Kaggle API token from your Kaggle account settings
    Place the kaggle.json file in ~/.kaggle/ directory
    Ensure the API token has appropriate permissions
    ```bash
    chmod 600 ~/.kaggle/kaggle.json
    ```
4. Data import script:
 ```bash
    python kaggle_dataset_import.py
    ```


    