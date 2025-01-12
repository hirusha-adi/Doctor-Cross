# Doctor Cross

Create that green color cross for doctors thing easily.

<p align="center">
  <img src="https://github.com/hirusha-adi/Doctor-Cross/assets/36286877/74621cb3-2721-403b-a724-6166215a8ae9" width="400px"/>
</p>



# Setup

## Run from Source

1. Install Python
2. Run these command to use a Virtual Enviroment

   ```
   python -m pip install virtualenv
   ```

3. Create a virtual enviroment

   ```
   virtualenv env
   ```

4. Activate the virtual enviroment

   ```
   env\Scripts\activate.bat
   ```

5. Install requirements

   ```
   pip install -r requirements.txt
   ```

6. Start the web server

   ```
   python app.py
   ```

7. Open [this URL](http://127.0.0.1:8090/) in your browser

   ```
   http://127.0.0.1:8090/
   ```

## Using Docker

### from Docker Hub

1. Pull the image from Docker Hub
   ```
   docker pull hirushaadi/doctor-cross-generator
   ```

2. Run the Docker Container
    ```sh
    docker run -p 8090:8090 doctor-cross-app
    ```

### by Building

1. **Build the Docker Image**: Open a terminal, navigate to your project directory, and run:
    ```sh
    docker build -t doctor-cross-app .
    ```

2. **Run the Docker Container**: Once the image is built, run the container using:
    ```sh
    docker run -p 8090:8090 doctor-cross-app
    ```

# Images

![image](https://github.com/hirusha-adi/Doctor-Cross/assets/36286877/52f25f09-370b-4863-a677-dbd225a8c322)

![image](https://github.com/hirusha-adi/Doctor-Cross/assets/36286877/3c7e5bfc-1816-494d-910b-02845ae4de6c)

