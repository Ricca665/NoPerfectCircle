# PerfectCircleTwist
This is a program that does the perfect circle but with a twist...

# Whats the twist?
The twist is that its going to open neal.fun Perfect circle and click the go button and then draw the circle, also after its going to close the webbrowser and shutdown the pc

# A much more detailed view of the code
The first thing that the code its gonna do is to open up the Neal.fun Perfect cirle game, its going to wait 4 seconds for the page to load and then its going to click the go button and then its going to draw the circle, after that its going to wait 0.3 seconds before closing the browser and then shut down the pc with the shutdown program in windows with the arguments "-s -t 0" 

# Compatibility list
Supported Browsers: chrome, firefox or edge
Supported os: Windows, in the future its going to have linux support, or at least that what i hope

# How to set itup

To set this up you need to first have python and then have installed pyautogui with this commad:
pip install pyautogui

This code is adapted for a 1366x768 screen

If you want to use this with any other display resolution follow the tutorial down below

You have to adapt the center of the screen to your screen, to do this download and open up Coordinates.py, and then its going to display coordinates of x and y (Also you need pyautogui for the coordinates.py app)

And its going to be something like this:
![image](https://github.com/Ricca665/NoPerfectCircle/assets/84286914/63571742-54b3-4bde-9c7e-2e0657fc4b80)

After that open up this site: https://neal.fun/perfect-circle/
And with the program open up go over the go button on the site, and save the coordinates of the go button coordinates

To modify the x and y values Open up circle.py in notepad and find the x,y values and its going to be like this if you did not modify the coordinates

![image](https://github.com/Ricca665/NoPerfectCircle/assets/84286914/83c76abd-5850-44f9-93f0-2f20bd993121)

After that modify the x and y values with your own's coordinates
Then save the file and you are done

# Running the code
Just double click the Circle.py app and let it do its thing

# Reuse this code
The code is open source but if you want to use this code in your progect mention my github account in any way


