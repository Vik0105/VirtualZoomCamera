# VirtualZoomCamera
A public repo for a virtual zoom camera to (not) pretend to have a glitch/lag on Zoom. I repeat, do (not) use it for that purpose.

## How to set it up
First, install `pyvirtualcam` or install using Command Prompt using `pip install pyvirtualcam`

Next, you'll need to download [obs-virtual-cam](https://github.com/Fenrirthviti/obs-virtual-cam/releases). If you only want the virtual cam without downloading OBS, use [this link](https://github.com/CatxFish/obs-virtual-cam/releases) for the ZIP

After unzipping the obs-virtual-cam, open Command Prompt as Admin and type in `regsvr32 /n /i:1 "<Path to obs-virtual-cam folder>\obs-virtualcam\bin\64bit\obs-virtualsource.dll"`

Then, just run the Python code and change your camera on Zoom to "OBS-Camera" and everything should be in order

Check out [this repository for pyvirtualcam](https://github.com/letmaik/pyvirtualcam) for more info

PS. The RGBA values are currently set to the actual Zoom colours so you can easily run the code with very few to no changes, and if you desire another colour, just change the RGBA
