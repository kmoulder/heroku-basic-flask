import json
import requests
import isodate

def get_duration(video_id):
                api_key = "AIzaSyAkkv6vi28XBoRknHMW2V9BTI6y-XNeMpo"
                response = requests.get("https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=contentDetails")
                data = json.loads(response.text)
                try:
                    duration = data["items"][0]["contentDetails"]["duration"]
                except IndexError:
                    duration = "PT1S"

                dur = str(isodate.parse_duration(duration))
                if dur[0:2] == "0:":
                    dur = dur[2:]
                duration = dur

                return duration
