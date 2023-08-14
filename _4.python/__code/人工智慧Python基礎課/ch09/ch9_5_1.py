# coding: utf-8
import pickle
fp = open("note.dat", "wb")
pickle.dump(11, fp)
pickle.dump("陳會安", fp)
pickle.dump([1, 2, 3, 4], fp)
fp.close()
