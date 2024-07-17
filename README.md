# Flights Around 
A small project leveraging the FlightRadarAPI to provide summarized data on planes within a specified radius around a given point on the map.
![image](https://github.com/user-attachments/assets/3420568b-9517-4cf0-a2d3-110b309ed77f)

## Installation

For this project, Python >= 3.11 is required.

Required packages:
- pip ~= 22.3.1
- wheel ~= 0.38.4
- geopy ~= 2.4.1
- requests ~= 2.31.0
- geographiclib ~= 2.0
- setuptools ~= 65.5.1
- certifi ~= 2024.2.2
- urllib3 ~= 2.2.1
- idna ~= 3.7
- dearpygui ~= 1.11.1
- pyperclip ~= 1.8.2
- screeninfo ~= 0.8.1
- Brotli ~= 1.1.0

Clone repo and navigate to the project directory

```bash
git clone https://github.com/mikalaytsepl/FlightsAround.git
```
Navigate to the prject directory
```bash
cd FlightsAround
```
install the depengences
```bash
pip install -r requirements.txt
```

## Usage 

In view_controller directory run 
```bash
python main.py
```
Alternatively, just open project via your editor (I've used Pycharm) and run it like that. 

## Interface 

Interface is pretty straight-forward in this one: 
At the top, there are three text fields. Two of these fields are mandatory, and an error popup will be displayed if they are left empty.
![image](https://github.com/user-attachments/assets/08022729-9711-4bdb-9f32-5d364dd39e02)
The last field is for filter preferences. Filters can be applied to the current results by pressing the "Apply" button, or to new results by starting a new scan with the Enter key while the preferences field is not empty.

Each element of the table is represented by a button. Clicking on any button will copy the corresponding text to the clipboard.

Finally, the last button under the controls will open the FlightRadar site in your default browser, allowing you to conveniently view the flight you are interested in on the map.

## Project Status and Other Info
Currently, I am not actively working on this project. However, if you would like to propose changes or fixes, please feel free to do so! :)
