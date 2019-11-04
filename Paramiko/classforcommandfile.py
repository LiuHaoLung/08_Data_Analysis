import paramiko
import os.path
import time
import sys
import re

# 檢查指令檔案
# 讓使用者提供該檔案之路徑
cmd_file = input("\n# Enter commands file path and name (e.g. D:\\MyApps\\myfile.txt): ")
 
# 確認這個檔案是否有存在
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid.Sending command(s) to device(s)...\n")

else:
    print("\n* File {} does not exist.Please check and try again.\n".format(cmd_file))
    sys.exit()
