from time import time

from syncrypto import Crypto, Syncrypto

bufferSize = 64 * 1024
password = "some_dummy_password"

folder = "/Users/bvalean/TVB/PROJECTS/Default_Project"
folder_encrypted = "/Users/bvalean/WORK/test-encryption/Default_Project_encrypted"
folder_decrypted = "/Users/bvalean/WORK/test-encryption/Default_Project_decrypted"


if __name__ == '__main__':
    print("========== ENCRYPTION ==========")
    crypto = Crypto(password)
    syncro1 = Syncrypto(crypto,folder_encrypted,folder)
    t = time()
    syncro1.sync_folder()
    print("========== FINISH ENCRYPTION ==========")
    encryption = time()-t

    print("========== DECRYPTION ==========")
    syncro1 = Syncrypto(crypto,folder_encrypted,folder_decrypted)
    t = time()
    syncro1.sync_folder()
    print("========== FINISH DECRYPTION ==========")
    decryption = time() - t

    print("========== RESULTS ==========")
    print("Ecrypted: {} seconds".format(encryption))
    print("Decrypted: {} seconds".format(decryption))

