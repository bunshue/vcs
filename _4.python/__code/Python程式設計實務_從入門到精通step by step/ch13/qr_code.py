# -*- coding: utf-8 -*-

import qrcode
im = qrcode.make("https://pmm.zct.com.tw/trial/")
im.save( "pic/qrcode.jpg")
