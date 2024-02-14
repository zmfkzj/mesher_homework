import ctypes

# 라이브러리 로드 (예: 'gpupixel.so' 또는 'gpupixel.dll')
gpupixel = ctypes.CDLL('./libgpupixel.so')

# 함수 인터페이스 정의
createSourceImage = gpupixel.createSourceImage
createSourceImage.argtypes = [ctypes.c_char_p]
createSourceImage.restype = ctypes.c_char_p


# SourceImage 인스턴스 생성 및 사용
source_image_instance = createSourceImage(b'tests/001_origin.jpg')
print(source_image_instance)