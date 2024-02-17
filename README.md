# Cam-viewer
## Library installation:
```
pip install cam-viewer
```
## Functions:
To use the functions, import cam-viewer:
```
import cam_viewer
```
### Camera playback function:
```
cam_viewer.playback(command, parameters, cams_json, cam_name, cam_number, use_text, fontfile)
```
The output shows this list: [cam_proc, response]:
  1) ```cam_proc``` - the [subprocess.Popen()](https://docs.python.org/3/library/subprocess.html#subprocess.Popen) class (Popen)
  2) ```responce``` - a line with the result of starting camera playback (string)

Input parameters:
  1) ```command``` - main FFMPEG command [```ffmpeg```, ```ffplay```, ```ffprobe```] (string)
  2) ```parameters``` - FFMPEG flags (string)
  3) ```cams_json``` - json file containing cameras and their settings, [example](https://github.com/Vasysik/streetcat-viewer/blob/main/cams.json) (json data)
  4) ```cam_name``` - camera name (string)
  5) ```cam_number``` - camera number (integer)
  6) ```use_text``` - show camers name and number in video output (boolean True/False)
  7) ```font_file``` - font file path

### Get camera data function:
```
cam_data(cams_json, cam_name, cam_number)
```
The output shows this list: [cam_url, enabled, response]:
  1) ```cam_url``` - camera URL (string)
  2) ```enabled``` - is the camera enabled (boolean True/False)
  3) ```responce``` - a line with the result of getting camera data (string)

Input parameters:
  1) ```cams_json``` - json file containing cameras and their settings, [example](https://github.com/Vasysik/streetcat-viewer/blob/main/cams.json)https://github.com/Vasysik/streetcat-viewer/blob/main/cams.json (json data)
  2) ```cam_name``` - camera name (string)
  3) ```cam_number``` - camera number (integer)

### Checking camera URL for availability:
```
url_available(cam_url)
```
The output shows this: 
  1) ```available``` - True/False

Input parameters:
  1) ```cam_url``` - camera URL (string)

### Get current time:
```
current_time()
```
The output shows this: 
  1) ```time_str``` - current time in ```%H:%M:%S``` format (string)
