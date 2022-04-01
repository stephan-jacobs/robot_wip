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

