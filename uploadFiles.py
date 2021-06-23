from os import access
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token  =access_token
    def upload_file(self,file_from, file_to):
        dbx  =dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = '7uqwtol0TCUAAAAAAAAAAd8pbIVqwnn42WrHXKG0ijXtfu_ICHqAH3hMeYsa0jXB'
    transferData = TransferData(access_token)
    file_from = input("Enter the source file: ")
    file_to  = input("Enetr the destination path: ")
    transferData.upload_file(file_from, file_to)
    print("File has been moved")


main()