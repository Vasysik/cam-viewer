# cam-viewer
## Library installation:
```
pip install cam-viewer
```
## Functions:
To use the functions, import cam-viewer:
```
import cam_viewer
```
1) Camera playback function
   ```
   cam_viewer.playback(command, parameters, cams_json, cam_name, cam_number, use_text, fontfile)
   ```
   The output shows this list: [cam_proc, response]:
     1) ```cam_proc``` - the [subprocess.Popen()](https://docs.python.org/3/library/subprocess.html#subprocess.Popen)https://docs.python.org/3/library/subprocess.html#subprocess.Popen class
     2) ```responce``` - a line with the result of starting camera playback
   
   Input parameters:
     1) ```command``` - main ffmpeg command (```ffmpeg```, ```ffplay```, ```ffprobe```)
     2) ```parameters``` - ffmpeg flags
     3) ```cams_json``` - json file containing cameras and their settings, [example](https://github.com/Vasysik/streetcat-viewer/blob/main/cams.json)https://github.com/Vasysik/streetcat-viewer/blob/main/cams.json
     4) ```cam_name``` - camera name
     5) ```cam_number``` - camera number
