# 計算地球上兩點的距離
"""
有兩點座標在地球表面上, 要計算兩點的距離, 會用到 haversine (半正矢公式)來進行計算.
"""

import numpy as np


def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = (
        np.sin(delta_phi / 2) ** 2
        + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    )
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)


lat1, lon1, lat2, lon2 = 40.6976637, -74.1197643, 25.7825453, -80.2994985

print(haversine_distance(lat1, lon1, lat2, lon2))


import haversine as hs

loc1 = (40.6976637, -74.1197643)
loc2 = (25.7825453, -80.2994985)
print(hs.haversine(loc1, loc2))
