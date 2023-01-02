# Raspberry Pi Self-Driving car

In this project, we used a Raspberry Pi 4B and various sensors to build a self-driving car. 
The Raspberry Pi Cam v.2 was used for image processing and lane tracking which working together with lane tracking sensors, while ultrasonic sensors were used to detect obstacles in the car's path. Temperature sensors were also included to monitor the car's internal and external temperature. Using these sensors and the Raspberry Pi's powerful processing capabilities, 
we were able to develop a fully autonomous vehicle that can navigate its surroundings and make decisions on its own.

## Getting Started
Here are the detailed instructions for getting started with your Raspberry Pi 4B self-driving car project:

1. Format the SD card and Install Raspberry Pi OS (legacy):
   * First, insert the SD card into your computer and format it using SD Card Formatter.
   * Next, download the Raspberry Pi OS (legacy) image from the official Raspberry Pi website and burn it onto the SD card      using balenaEtcher.
   * Once the image has been burned, insert the SD card into the Raspberry Pi and power it on.    
   * Follow the on-screen instructions to set up the operating system and configure your Raspberry Pi.
2. Set up VNC to remote desktop raspberry pi from our personal computer:
   * On your Raspberry Pi, open the VNC Server app.
   * Click the gear icon to open the Server Preferences, and click the Security tab.
   * In the Security tab, set a password that will be used to access the Raspberry Pi from your computer.
   * On your computer, download and install the VNC Viewer app.    
   * In the VNC Viewer app, enter the IP address of your Raspberry Pi and the password that you set earlier.
   * Click "Connect" to establish a remote desktop connection to your Raspberry Pi.
3. Sudo update and upgrade the raspberry pi:
   * Open the Terminal on your Raspberry Pi and enter the following commands:
      `sudo apt-get update`
      `sudo apt-get upgrade`
   * These commands will update the package list and upgrade any outdated packages to the latest version.
4. Install opencv-python and its dependencies:
   * Open the Terminal on your Raspberry Pi and enter the following command:
      `pip3 install opencv-python`
   * This will install the opencv-python package, which is required for image processing.
5. Assemble the car:
   * Follow the instructions for assembling the car. Make sure to connect all the necessary sensors, including the              Raspberry Pi Cam v.2, ultrasonic sensors, lane tracking sensors, and temperature sensors.
6. Connect all the required sensors to the raspberry pi:
   * Refer to the documentation for your sensors to determine the correct pin connections on the Raspberry Pi.
   * Connect the sensors to the Raspberry Pi using jumper wires.
7. Run the code through Python IDE on raspberry pi:
   * Open the Python IDE on your Raspberry Pi and navigate to the location of the code for your self-driving car.
   * Run the code by clicking the "Run" button or by pressing F5 on your keyboard.

## Prerequisites
Here is a list of the tools and libraries that are required for your Raspberry Pi 4B self-driving car project:

Tools:
* Raspberry Pi 4B
* DHT-11 temperature sensors
* M5-stack or Arduino
* At least 3 ultrasonic sensors
* Raspberry Pi Camera v2.1
* Breadboard
* Jumper wires
* Power bank (must be 5V and 3 Amp output)
* Motor Driver HAT MDD10
* Heatsink case
* Micro SD card (32 GB)
* Resistor 330 Ω and 470 Ω
* Micro Servo Motor set (MG995)
* T stand and spacer set
* Chassis
* 2 motors
* 4 wheels

Libraries:
* opencv-python
* pyserial

## Installing 
One of the most challenging aspects of this project will be getting opencv to work with Python on your Raspberry Pi. It is crucial that you know how to troubleshoot and reformat your Raspberry Pi when things go wrong, and that you carefully follow all instructions without skipping any steps.

1. Open the Terminal on your Raspberry Pi and update the package list by entering the following command:
   `sudo apt-get update`
2. Install the dependencies for opencv-python by entering the following command:
   `sudo apt-get install python3-opencv`
3. To verify that opencv-python has been installed correctly, open the Python interpreter by entering the following            command:
   `python3`
4. In the Python interpreter, enter the following command:
   `import cv2`
5. If the import statement executes without any errors, opencv-python has been installed successfully.

## Running the tests
