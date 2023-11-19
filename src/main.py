import threading
from WatchFolder import WatchFolder
from log.Generating_dataset import GenerateDataset
import os


def thread_folderCapture(src_path, callback):
    WatchFolder(src_path=src_path, callback=callback)


def callbackExample(): 
    print("hello")

def callbackConvertCSV(src_path):
    print(src_path)

def callbackCapturePcap(src_path):
    print(src_path)
    # GenerateDataset(['../../capture/captures_cic_2023_00001_20231118144846.pcap'])
    

if __name__ == "__main__":
    print("Khởi tạo chương trình")
    abs_path = os.getcwd()
    print(abs_path)
    capture_folders = [
        {
            'folder': '../captures', 
            'callback': callbackCapturePcap
        }, 
        {
            'folder': '../csv', 
            'callback': callbackConvertCSV
        }
    ]



    threads = []

    for capture_folder in capture_folders:
        folder = capture_folder['folder']
        callback = capture_folder['callback']
        threadFolderCapture = threading.Thread(target=thread_folderCapture, args=(folder,callback))
        threadFolderCapture.start()
        threads.append(threadFolderCapture)

    for thread in threads:
        thread.join()

    