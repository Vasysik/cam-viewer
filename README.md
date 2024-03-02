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
cam_viewer.playback(command, parameters, cams_json, cam_group, cam_id, use_title, fontfile, custom_title)
```
The output shows this list: [cam_proc, response]:
  1) ```cam_proc``` - the [subprocess.Popen()](https://docs.python.org/3/library/subprocess.html#subprocess.Popen) class (Popen)
  2) ```responce``` - a line with the result of starting camera playback (string)

Input parameters:
  1) ```command``` - main FFMPEG command [```ffmpeg```, ```ffplay```, ```ffprobe```] (string)
  2) ```parameters``` - FFMPEG flags (string)
  3) ```cams_json``` - json file containing cameras and their settings, [example](https://github.com/Vasysik/streetcat-viewer/blob/main/cams.json) (json data)
  4) ```cam_group``` - camera group (string)
  5) ```cam_id``` - camera ID (integer)
  6) ```use_title``` - show camera group and camera ID in video output (boolean True/False)
  7) ```font_file``` - font file path (string)
  8) ```custom_title``` - your custom title (string)

### Get camera data function:
```
cam_viewer.cam_data(cams_json, cam_group, cam_id)
```
The output shows this list: [cam_url, enabled, response]:
  1) ```cam_url``` - camera URL (string)
  2) ```enabled``` - is the camera enabled (boolean True/False)
  3) ```responce``` - a line with the result of getting camera data (string)

Input parameters:
  1) ```cams_json``` - json file containing cameras and their settings, [example](https://github.com/Vasysik/streetcat-viewer/blob/main/cams.json) (json data)
  2) ```cam_group``` - camera group (string)
  3) ```cam_id``` - camera ID (integer)

### Checking camera URL for availability:
```
cam_viewer.url_available(cam_url)
```
The output shows this: 
  1) ```available``` - is the camera available (boolean True/False)

Input parameters:
  1) ```cam_url``` - camera URL (string)

### Get current time:
```
cam_viewer.current_time()
```
The output shows this: 
  1) ```time_str``` - current time in ```%H:%M:%S``` format (string)

## Examples of using:
- [streetcat-console](https://github.com/Vasysik/streetcat-console) (simple usage)
- [streetcat-youtube](https://github.com/Vasysik/streetcat-youtube)
