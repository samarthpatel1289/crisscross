from rest_framework.response import Response


def create_response(data, code, message=None, extra={}):
    # extra["media_url"] = dj_settings.MEDIA_URL
    return Response({"data": data, "code": code}, code)
