#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import tensorflow as tf
print(tf.__version__)