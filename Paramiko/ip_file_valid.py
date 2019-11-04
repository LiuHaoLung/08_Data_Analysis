import os.path
import sys

# 檢查IP位址和內容的有效性
def ip_file_valid():
    
    # 讓使用者自行輸入相關檔案路徑
    ip_file = input('\n# Enter IP file path and name: ')
    
    # 確定檔案是否存在
    if os.path.isfile(ip_file) == True:
        print('\n* IP file is valid\n')
    else:
        print(f'\n* File {ip_file} does not exist. Please check and try again\n')
        # 如果不存在的話，除了叫使用者重新輸入外，也會直接離開這個執行
        sys.exit()
    
    # 讀取使用者所輸入的檔案
    selected_iP_file = open(ip_file,'r')
    
    # 從頭開始讀取這個檔案，並且確保讀取時不會跳掉任何一行
    selected_iP_file.seek(0)
    
    # 將一行一行讀取這個檔案（Ip address），並丟在ip_list裡面
    ip_list = selected_iP_file.readlines()
    
    # 將原本讀取的檔案關閉
    selected_iP_file.close()
    
    # 回傳所讀取到的所有資料
    return ip_list