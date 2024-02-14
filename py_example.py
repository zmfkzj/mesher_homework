import ctypes

# 라이브러리 로드 (예: 'gpupixel.so' 또는 'gpupixel.dll')
gpupixel = ctypes.CDLL('./libgpupixel.so')

# 함수 인터페이스 정의
createSourceImage = gpupixel.createSourceImage
createSourceImage.restype = ctypes.c_void_p

deleteSourceImage = gpupixel.deleteSourceImage
deleteSourceImage.argtypes = [ctypes.c_void_p]

loadSourceImage = gpupixel.loadSourceImage
loadSourceImage.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

# BeautyFaceFilter 관련 함수
createBeautyFaceFilter = gpupixel.createBeautyFaceFilter
createBeautyFaceFilter.restype = ctypes.c_void_p

deleteBeautyFaceFilter = gpupixel.deleteBeautyFaceFilter
deleteBeautyFaceFilter.argtypes = [ctypes.c_void_p]

setBeautyLevel = gpupixel.setBeautyLevel
setBeautyLevel.argtypes = [ctypes.c_void_p, ctypes.c_float]

# TargetRawDataOutput 관련 함수
createTargetRawDataOutput = gpupixel.createTargetRawDataOutput
createTargetRawDataOutput.restype = ctypes.c_void_p

deleteTargetRawDataOutput = gpupixel.deleteTargetRawDataOutput
deleteTargetRawDataOutput.argtypes = [ctypes.c_void_p]

# 가정: 콜백 함수의 C 타입을 정의
CALLBACK_FUNC_TYPE = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int, ctypes.c_int)

setOutputCallback = gpupixel.setOutputCallback
setOutputCallback.argtypes = [ctypes.c_void_p, CALLBACK_FUNC_TYPE]




# SourceImage 인스턴스 생성 및 사용
source_image_instance = createSourceImage()
loadSourceImage(source_image_instance, b'tests/001_origin.jpg')

# 사용 예시
beauty_filter = createBeautyFaceFilter()
setBeautyLevel(beauty_filter, 0.5)  # 뷰티 레벨 설정
deleteBeautyFaceFilter(beauty_filter)

def raw_data_callback(data, width, height):
    # 여기에서 데이터 처리 로직 구현
    pass

target_output = createTargetRawDataOutput()
callback_func = CALLBACK_FUNC_TYPE(raw_data_callback)
setOutputCallback(target_output, callback_func)

with open('result.jpg', 'bw') as f:
    f.write(target_output)

deleteSourceImage(source_image_instance)
deleteTargetRawDataOutput(target_output)