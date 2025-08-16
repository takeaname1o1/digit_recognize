# Digit Recognizer Web App

This is a web application built with Python and Flask that serves a machine learning model for digit recognition. The application is configured for production deployment on the Render platform using Gunicorn.

-----

## Technologies Used

  * **Backend**: **Flask**
  * **Machine Learning**: **TensorFlow**
  * **WSGI Server**: **Gunicorn**
  * **Database Connector**: **Psycopg2**
  * **Core Libraries**: **NumPy**, **Matplotlib**

-----

## Project Structure

```
.
├── app.py                  # Main Flask application file
├── requirements.txt        # Python dependencies for pip
├── render.yaml             # Deployment configuration for Render
├── environment.yml         # (Alternative) Conda environment definition
├── run.sh                  # Script for local development setup
└── README.md               # Project documentation
```

-----

## How to Run Locally

This project uses `uv` for fast environment setup, but you can use any virtual environment manager.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/takeaname1o1/digit_recognize.git
    cd digit_recognize
    ```

2.  **Create and activate a virtual environment:** The included `run.sh` script uses `uv`, a fast Python package installer.

    ```bash
    # Create the virtual environment for Python 3.8
    python3.8 -m venv .venv

    # Activate it
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    python app.py
    ```

    The application will be running on `http://0.0.0.0:5000`.

-----

## Deployment on Render

This application is configured for easy deployment on Render using a `render.yaml` file.

1.  **Push your code** to a GitHub, GitLab, or Bitbucket repository.
2.  On the **Render Dashboard**, click **"New +"** and select **"Web Service"**.
3.  Connect your repository.
4.  Render will automatically detect and use the `render.yaml` file to configure the service. The key settings from the file are:
      * **Python Version**: `3.8.10`
      * **Build Command**: `pip install -r requirements.txt`
      * **Start Command**: `gunicorn app:app`
5.  Click **"Create Web Service"** to deploy. The application will be live at the URL provided by Render upon successful build.
