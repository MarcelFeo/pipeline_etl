from typing import Dict
import requests

class HttpRequester:

    def __init__(self) -> None:
        self.__url = 'https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnhxSThJSmhIdUI3dkxCNm5FT2sxc3JYLUtXd3xBQ3Jtc0ttVHZkRGRGZ3RKTWx2aWhYLW9MeHdHV0hEc0dJVGZzdkJGak1OQTc1ZTRQTGlwdUtjbW10YXAxUDZDYXZEUTNwdEg1TTUySVlzazh1YzZtSVBLYXRVR3R1WGtFWjk3SmdKX3RhS0FjX1lpYUNSMEU1dw&q=https%3A%2F%2Fweb.archive.org%2Fweb%2F20121007172955%2Fhttps%3A%2F%2Fwww.nga.gov%2Fcollection%2FanZ1.htm&v=MXUqKvEST8s'

    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
