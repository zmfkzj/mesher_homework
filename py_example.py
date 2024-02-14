import ctypes
from PIL import Image

# 라이브러리 로드 (예: 'gpupixel.so' 또는 'gpupixel.dll')
gpupixel = ctypes.CDLL('./libgpupixel.so')

# 함수 인터페이스 정의
createSourceImage = gpupixel.createSourceImage
createSourceImage.argtypes = [
    # ctypes.POINTER(ctypes.c_ubyte),  # 또는 ctypes.c_void_p
    ctypes.c_char_p,  # 또는 ctypes.c_void_p
    ctypes.c_int,
    ctypes.c_int,
]


image = Image.open('tests/001_origin.jpg')
bytes_image = image.tobytes()
# bytes_image = (ctypes.c_ubyte * len(bytes_image)).from_buffer_copy(bytes_image)

# source_image_instance = createSourceImage(bytes_image, image.width, image.height, image.width*len(image.mode))
source_image_instance = createSourceImage(bytes_image, image.width, image.height)
print(source_image_instance)