import base64
import requests


def send_image_to_server(filename):
    img_b64 = encode_image_to_b64_string(filename)
    send_b64_string_to_server(img_b64)


def encode_image_to_b64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def send_b64_string_to_server(b64_string):
    out_data = {"image": b64_string, "net_id": "daw742", "id_no": 1}
    r = requests.post("http://vcm-6764.vm.duke.edu/add_image", json=out_data)
    print(r.status_code)
    print(r.text)


def get_watermark_image():
    r = requests.get("http://vcm-6764.vm.duke.edu/get_image/daw742/1")
    if r.status_code != 200:
        print(r.text)
        return "There was an error"
    else:
        b64_string = r.text
    convert_b64_to_file(b64_string)


def convert_b64_to_file(b64_string):
    image_bytes = base64.b64decode(b64_string)
    with open("new_file.png", "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == '__main__':
    send_image_to_server("acl1.jpg")
    get_watermark_image()