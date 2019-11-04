import sys
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

# 將ip.txt裡的IP address存為list
ip_list = ip_file_valid()
 
# 驗證在這個list裡面的IP是否有效
try:
    ip_addr_valid(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# 驗證在這個list裡面的IP是否都可以達到
try:
    ip_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# 呼叫threading
create_threads(ip_list, ssh_connection)
 
#End of program