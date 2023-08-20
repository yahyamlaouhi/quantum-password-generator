# Quantum Password Generator App

The Quantum Password Generator is an application that leverages quantum computing principles to create secure and unpredictable passwords. This project combines the power of Python, Django, and the Qiskit quantum python library to generate robust passwords that are difficult to predict.

## Setup

To set up and run the Quantum Password Generator app using Docker, follow these steps:

1. **Clone the Repository:**

    Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/yahyamlaouhi/quantum-password-generator.git
    cd quantum-password-generator
    ```

2. **Build the Docker Image:**

    Build the Docker image for the app by running the following command:

    ```bash
    docker-compose build --no-cache
    ```

3. **Run Database Migrations:**

    Apply the database migrations to set up the necessary database schema:

    ```bash
    docker-compose run app sh -c "python manage.py makemigrations"
    docker-compose run app sh -c "python manage.py migrate"
    ```

5. **Run the Application:**

    Finally, start the application using Docker Compose:

    ```bash
    docker-compose up
    ```

    The app should now be accessible at http://localhost:8000/.

## Usage

1. **Generate Quantum Passwords:**

    Navigate to the password generation section of the app and provide the required input parameters. The Quantum Password Generator will use the Qiskit library to create a secure password that utilizes quantum randomness.

2. **Explore the App:**

    The app also features a restaurant recommendation feature (populated with sample data) to showcase the broader functionality of the Django application.

## Contributions and Issues

If you encounter any issues with the app or would like to contribute to its development, feel free to submit issues and pull requests on the GitHub repository: [Quantum Password Generator Repository](https://github.com/yourusername/quantum-password-generator).

## Credits

This project was developed as a demonstration by Yahya Mlaouhi. It utilizes the Django framework and Qiskit quantum python library to showcase the capabilities of quantum password generation.

## License

This project is licensed under the [MIT License](LICENSE).
