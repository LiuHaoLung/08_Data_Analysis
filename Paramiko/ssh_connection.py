import paramiko
import os.path
import time
import sys
import re

# 檢查使用者姓名及密碼
# 讓使用者提供該檔案之路徑
user_file = input("\n# Enter user file path and name: ")
 
# 確認這個檔案是否有存在
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid.\n")
else:
    print("\n* File {} does not exist.Please check and try again.\n".format(user_file))
    sys.exit() 

# 檢查指令檔案
# 讓使用者提供該檔案之路徑
cmd_file = input("\n# Enter commands file path and name: ")
 
# 確認這個檔案是否有存在
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid.Sending command(s) to device(s)...\n")

else:
    print("\n* File {} does not exist.Please check and try again.\n".format(cmd_file))
    sys.exit()

# 打開SSH
def ssh_connection(ip):
    
    global user_file
    global cmd_file
    
    # 建立SSH連結
    try:
        
        # 定義SSH的參數
        selected_user_file = open(user_file, 'r')
        
        # user檔案從頭開始讀取
        selected_user_file.seek(0)
        
        # 讀取使用者帳號(username)
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        
        # user檔案從頭開始讀取
        selected_user_file.seek(0)
        
        # 讀取使用者密碼(password)
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
        
        # 登入裝置
        session = paramiko.SSHClient()
        
        # 測試目的，就算用不知名的host key，也會被接受
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # 利用讀取到的帳號及密碼進行登入         
        session.connect(ip.rstrip("\n"), username = username, password = password)
        
        # 在路由器上啟動互動式的對話
        connection = session.invoke_shell()
        
        # 進入enable模式
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)
        
        # 進入configure terminal模式
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        
        # 打開要讀取的cmd檔案
        selected_cmd_file = open(cmd_file, 'r')
            
        # cmd檔案從頭開始讀取
        selected_cmd_file.seek(0)
        
        # 將cmd內的內容寫入
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
        
        # 關閉user檔案
        selected_user_file.close()
        
        # 關閉cmd檔案
        selected_cmd_file.close()
        
        # 確認輸入指令是否有錯誤
        router_output = connection.recv(65535)
        
        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))
            
        else:
            print("\nDONE for device {} :)\n".format(ip))
            
        # 測試是否可以順利輸出
        print(str(router_output) + "\n")
        
        # 結束此連結
        session.close()
     
    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")