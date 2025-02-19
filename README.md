# Flights Around 
A small project leveraging the FlightRadarAPI & geopy to provide summarized data on planes within a specified radius around a given point on the map.
The UI is made using PyQt6 (the older version uses DearPyGUI and can be found in the old_UI_DPG branch).

![image](https://github.com/user-attachments/assets/ec66b35d-7a8d-4636-9cb3-430f2dd3a41e)

## Installation and startup

For this project, Python >= 3.11 is required.

# Clone repo and navigate to the project directory

```bash
git clone https://github.com/mikalaytsepl/FlightsAround.git
```
# Navigate to the prject directory
```bash
cd FlightsAround
```
# Install the depengences 
```bash
pip install -r requirements.txt
```
this will istall them sysem wide, if you want to do that locally, create and activate virual environment first:
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```
After that you can run the application lika any other python script.

# To automate the process you can simply make the setup script executable and run it.
```bash
chmod +x setup.sh
./setup.sh
```
And do the same for the run script:
```bash
chmod +x FlightsAroundRun.sh
./FlightsAroundRun.sh
```
Note that .sh scripts are used for the venv approach. 

## Interface 

Interface is pretty straight-forward : 
At the top, there are two text fields. They are mandatory in order to conduct the search.
While geolocation may come in many forms, radius must always be the int number (there's a drop down selection for the metric), and the error will occure if it's not:

![image](https://github.com/user-attachments/assets/7b9e5492-543c-4919-8e51-b9386fd92630)

In this version filter configuration is moved to the separate window and a toggle added to switch it on and off.
After toggling the filter on, all the flights which do not pass the filter requirements are hidden. Note, that the new search is not being conducted, so you can get to see the exact same reults cluster by dasbling filters. You can work with the same data set for as long as you want unless the search button is pressed again. 

![image](https://github.com/user-attachments/assets/827fda7b-e441-451a-bcd0-f0a1f24be8e3)

![image](https://github.com/user-attachments/assets/611c55ca-0eef-4e37-b9b6-cee443f6011c)

"No info" means that FlightRadar does not have or did not provide the information for the security reasons, or simply because there's none. The most common examples of such behaviour are private or military aircrafts.

With the more convinient table view users now can select multiple rows and columns at the same time, aswell as save the table as the excel file.

![image](https://github.com/user-attachments/assets/8f6546a4-3677-4e73-bceb-9b19de8b908c)

![image](https://github.com/user-attachments/assets/3bf0c180-9845-43f8-b32e-7b56f566d8c2)

![image](https://github.com/user-attachments/assets/54b558d5-63df-4cee-bfd7-940c0c7ec46d)


"Go to FlightRadar" and "Go to GoogleMaps" are kinda self explanatory and are so users would be able to see the locations and flights they are interested in right away, conviniountly switching from the statisticall approach this app provides to move specific things.

## Project Status and Other Info
If you would like to propose any changes or fixes, please feel free to do so! :)
