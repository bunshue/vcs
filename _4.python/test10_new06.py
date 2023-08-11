
_size_factors = {
    "kb": 1000, "mb": 1000 * 1000, "gb": 1000 * 1000 * 1000,
    "kib": 1024, "mib": 1024 * 1024, "gib": 1024 * 1024 * 1024,
}

for aaa in _size_factors:
    print(aaa, _size_factors[aaa])




_deprecations = {
    "JPEGBaseline": "JPEGBaseline8Bit",
    "JPEGExtended": "JPEGExtended12Bit",
    "JPEGLossless": "JPEGLosslessSV1",
    "JPEGLSLossy": "JPEGLSNearLossless",
    "JPEG2000MultiComponentLossless": "JPEG2000MCLossless",
    "JPEG2000MultiComponent": "JPEG2000MC",
}

for name in _deprecations:
    print(name)



import hashlib



hash_val = hashlib.sha512('aaaaaaa'.encode("utf-8"))
print(hash_val)

dicom_uid = str(int(hash_val.hexdigest(), 16))
print(dicom_uid)



import random

tttt = hex(random.getrandbits(64))  # 64 bits randomness
print(tttt)


