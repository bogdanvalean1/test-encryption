import io
from os import stat

import h5py
import psutil
import pyAesCrypt

bufferSize = 64 * 1024
password = "some_dummy_password"

file = "/Users/bvalean/WORK/test-encryption/files/SimulationHistory.h5"
encrypted_file = file + ".aes"

if __name__ == '__main__':
    print("1. {}".format(psutil.virtual_memory()))
    h5_file = h5py.File(file, 'r', libver='latest')
    print("2. {}".format(psutil.virtual_memory()))
    print(h5_file["/"].attrs["TVB_gid"])

    pyAesCrypt.encryptFile(file, encrypted_file, password, bufferSize)
    fDec = io.BytesIO()

    print("3. {}".format(psutil.virtual_memory()))
    with open(encrypted_file, "rb") as fIn:
        try:
            try:
                inputFileSize = stat(encrypted_file).st_size
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fDec, password, bufferSize, inputFileSize)
            except ValueError as exd:
                raise ValueError(str(exd))
        except IOError:
            raise IOError("Unable to write output file.")
    print("4. {}".format(psutil.virtual_memory()))

    h5_file_stream = h5py.File(fDec, "r")
    print("5. {}".format(psutil.virtual_memory()))

    print(h5_file_stream["/"].attrs["TVB_gid"])

    with open(file + "decript.h5", "wb") as fout:
        fout.write(fDec.getbuffer())
