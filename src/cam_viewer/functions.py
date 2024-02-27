import subprocess
import time
import urllib.request
import logging

cam_proc = None

def current_time():
    return time.strftime("%H:%M:%S", time.localtime())

def cam_data(cams_json = None, cam_group = "", cam_number = 0):
    cam_url = ""
    enabled = True
    response = f"Cam {cam_group} {cam_number} is turned on"
    if cam_group in cams_json and cams_json[cam_group]:
        if 1 <= cam_number <= len(cams_json[cam_group]["cameras"]):
            cam_url = cams_json[cam_group]["cameras"][cam_number - 1]
            logging.info(f"{current_time()} | {response} url: {cam_url}")
            if(not url_available(cam_url)):
                enabled = False
                response = f"Cam {cam_group} {cam_number} not available - no response from url"
                logging.error(f"{current_time()} | {response} url: {cam_url}")
        else:
            enabled = False
            response = f"Cam {cam_group} {cam_number} does not exist - invalid number"
            logging.error(f"{current_time()} | {response}")
    else:
        enabled = False
        response = f"Cam {cam_group} {cam_number} does not exist - invalid group name"
        logging.error(f"{current_time()} | {response}")
    return [cam_url, enabled, response]

def url_available(cam_url = ""):
    try: 
        urllib.request.urlopen(cam_url)
        return True
    except: return False

def playback(command = "ffplay", parameters = "", cams_json = None, cam_group = "", cam_number = 1, use_title = False, font_file = "", custom_title = ""):
    logging.info(f"{current_time()} | Play {command} {parameters} {cam_group} {cam_number} {use_title} {font_file} {custom_title}")
    cam_url = ""
    text = ""
    global cam_proc
    cam_url, enabled, response = cam_data(cams_json, cam_group, cam_number)
    if enabled: 
        if use_title and font_file != "": 
            title = f"Camera\: {cam_group} {cam_number}"
            if custom_title != "": title = custom_title
            text = f"-vf \"drawtext=fontfile={font_file}:fontsize=18:fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=5:y=5:text='{title}'\""
        if cam_proc:
            try:
                logging.info(f"{current_time()} | FFMPEG killing...")
                cam_proc.stdin.write('q'.encode('utf-8'))
                cam_proc.stdin.flush()
                logging.info(f"{current_time()} | FFMPEG killed successfully!")
            except: logging.error(f"{current_time()} | FFMPEG killing ERROR")
        try:
            logging.info(f"{current_time()} | FFMPEG launch: {command} {cam_url} {text} {parameters}")
            cam_proc = subprocess.Popen(f"{command} {cam_url} {text} {parameters}", shell=True, stdin=subprocess.PIPE)
        except: logging.error(f"{current_time()} | FFMPEG launch ERROR")
    return [cam_proc, response]