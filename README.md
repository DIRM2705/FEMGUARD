<p align="center">
    <img src="https://github.com/DIRM2705/FEMGUARD/blob/main/images/Logo%20Transparent.png"/>
</p>

<h2> Abstract </h2>

Violence against women remains a focus of concern in our community. The alarming increase of women affected by psychological, phisical, sexual, economical or patrimonial violence has spurred victims to take actions towards the assurance of their safety. FEMGUARD created a solution in the form of a security device that incorpores a hidden camera, a heart rate sensor and Near-Field Communication (NFC) aiming to safeguards women's integrity, reducing violent crimes as well as, promoting an equitative and effective justice system.

<h2> Developement Environment configuration </h2>

Firstly, clone the repository to your PC.

You may need Python 3.12.4 to work in this project. If you have already satisfied this requirement, you now may create a virtual environment using:

```
py -m venv venv
```
Then, activate the environment:

```
venv/Scripts/activate
```
To install the remaining requirements, run the following command:

```
pip install -r requirements.txt
```

<h2> Design </h2>
The following image of the first prototype shows the disposition of electronic components inside the device.
<p align="center">
    <img src="https://imgur.com/hiHfNrf.jpeg"/>
</p>

<h2> Algorithm </h2>
<p align="center">
    <img src="https://imgur.com/Almqsjn.jpeg"/>
</p>

<h2>App Screens </h2>
The app contains the following screens

<h3> Home screen </h3>
It shows a small greeting to the FEMGUARD's user and the device state (either connected or disconnected). Device's state is also represented by the icon.

<h3> Directory screen </h3>
Shows Puebla's city emergency numbers so users can have an easy acces to them. Moreover, there are templates where FEMGUARD's corporation contact information would be available.

<h3> Connections screen </h3>
This screen discovers the nearby Bluetooth Low Energy devices and filters them by reading the advertise data and looking for the specific UUID.

<h3> User's information screen </h3>
User's basic medical information is shown and editable in this screen. The data collected in this screen, should be stored in the NFC included in the physical device. Also, here users can set their emergency contacts. This persons, may receive an SMS with user's geolocation information in case of emergency.

<h3> Video screen </h3>
Here users may find the videos filmed by the hidden camera.

<h3> Cancel button screen </h3>
When the device triggers an emergency, this screen will pop out. Users will have 15 seconds to press the button to cancel the event, delete the video and avoid alarming their emergency contacts.