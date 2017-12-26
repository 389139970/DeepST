import h5py
import numpy as np
def load_stdata(fname):
    f = h5py.File(fname, 'r')
    data = f['data'].value
    timestamps = f['date'].value
    f.close()
    return data, timestamps

data,timestamps = load_stdata('NYC14_M16x8_T60_NewEnd.h5')
# print(data,timestamps)
data = np.ndarray.tolist(data)
timestamps = np.ndarray.tolist(timestamps)
# print(timestamps)
for i in range(16):
    print(data[1][0][i])