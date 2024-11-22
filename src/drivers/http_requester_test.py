from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    url = 'https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnhxSThJSmhIdUI3dkxCNm5FT2sxc3JYLUtXd3xBQ3Jtc0ttVHZkRGRGZ3RKTWx2aWhYLW9MeHdHV0hEc0dJVGZzdkJGak1OQTc1ZTRQTGlwdUtjbW10YXAxUDZDYXZEUTNwdEg1TTUySVlzazh1YzZtSVBLYXRVR3R1WGtFWjk3SmdKX3RhS0FjX1lpYUNSMEU1dw&q=https%3A%2F%2Fweb.archive.org%2Fweb%2F20121007172955%2Fhttps%3A%2F%2Fwww.nga.gov%2Fcollection%2FanZ1.htm&v=MXUqKvEST8s'
    response_context = 'url text mock'
    requests_mock.get(url, status_code=200, text=response_context)

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()

    assert 'status_code' in request_response
    assert 'html' in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == response_context
