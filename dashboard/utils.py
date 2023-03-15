import base64
import uuid
from django.core.files.base import ContentFile
# import extcolors
# import matplotlib.colors as mcolors

def get_report_image(data):
    _, str_image = data.split(";base64")
    decoded_img = base64.b64decode(str_image)
    img_name = str(uuid.uuid4())[:10] + ".png"
    data = ContentFile(decoded_img, name=img_name)

    return data


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


# def get_colors_in_hex(image: str) -> list:
#     colors = extcolors.extract_from_path(image,tolerance = 12,limit=5)[0]
#     colors = [color[0] for color in colors]
#     colors = [tuple(color / 255 for color in color) for color in colors]
#     hex_colors = [mcolors.to_hex(color) for color in colors]
#     return hex_colors

