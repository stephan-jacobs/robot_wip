# Things I had to do and links I found/will hopefully find useful

## Guide

### Setting up python environment for opencv:

You can just install opencv with pip. It's by far the easiest way to do it but you have to have a pretty recent version of pip so start with:

`pip3 install --upgrade pip`

And then install opencv:

`pip3 install opencv-contrib-python` (See note 1)

## Useful Links

### Taking and comparing images:

* [Taking basic images](https://techoverflow.net/2018/12/18/how-to-take-a-webcam-picture-using-opencv-in-python/)
* [Colour Conversion in OpenCV](https://docs.opencv.org/3.4/db/d64/tutorial_js_colorspaces.html)
* [Stereo Images Robot Operating System](http://wiki.ros.org/stereo_image_proc/Tutorials/ChoosingGoodStereoParameters)
* [Stereo Images OpenCV](https://docs.opencv.org/3.4.12/dd/d53/tutorial_py_depthmap.html)
* [Capturing multiple images at once](https://stackoverflow.com/questions/29664399/capturing-video-from-two-cameras-in-opencv-at-once)


### Using the HC-SR04 Ultrasonic Distance Meter 

* [Wiring up and using HC-SR04](https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)

### Using the Adafruit DC Motor HAT

* [Official Adafruit Guide](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-dc-motors) (see note 2)

### Using Midas Monocular Depth Estimation on RPi

* Use this guide: [Midas v2.1 small TFLite Inference](https://github.com/ibaiGorordo/Midasv2_1_small-TFLite-Inference) (see note 3)

## Notes

*Note1:* If you get this warning:

  `WARNING: The scripts f2py, f2py3 and f2py3.7 are installed in '/home/pi/.local/bin' which is not on PATH.
    Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  `
  
  Then you might find [this webpage](https://help.ubuntu.com/community/EnvironmentVariables#Persistent_environment_variables) helpful. Basically all you need to do is:
  
  `cd etc/profile.d`
  
  `vim myenvvars.sh`
  
  Once you're in vim just add this line:
  
  `` export `PATH=/home/pi/.local/bin` ``

*Note2:* On Linux, hence on the Raspberry Pi, the `keyboard` python package requires root permissions to run. So to run this script you have to run it as root.
I had an issue though where running `sudo python3 motor_control_keyboard.py` said that `keyboard` wasn't installed. What I had to do was uninstall keyboard from pip, then run `sudo pip3 install keyboard`.
Now I can run `sudo python3 motor_control_keyboard.py` and it works.

*Note3:* The regular version of MIDAS does not seem to be compatible with RPi. It might have something to do with ARM but I'm not sure.
