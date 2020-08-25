from time import time

from syncrypto import Crypto, Syncrypto

bufferSize = 64 * 1024
password = "some_dummy_password"

folder = "/Users/bvalean/WORK/test-encryption/Default_Project"
folder_encrypted = "/Users/bvalean/WORK/test-encryption/Default_Project_encrypted"
folder_decrypted = "/Users/bvalean/WORK/test-encryption/Default_Project_decrypted"


if __name__ == '__main__':
    crypto = Crypto(password)
    syncro1 = Syncrypto(crypto,folder_encrypted,folder)
    t = time()
    syncro1.sync_folder()
    print("Ecrypted: {} seconds".format(time()-t))

    syncro1 = Syncrypto(crypto,folder_encrypted,folder_decrypted)
    t = time()
    syncro1.sync_folder()
    print("Decrypted: {} seconds".format(time()-t))

