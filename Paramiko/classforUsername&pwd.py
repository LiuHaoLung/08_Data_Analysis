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