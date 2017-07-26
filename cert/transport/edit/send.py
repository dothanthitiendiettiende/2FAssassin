from smb.SMBConnection import SMBConnection



userID = 'client'
password = 'password'
client_machine_name = 'kali'

server_name = 'box'
server_ip = '172.16.173.180'

domain_name = ''

conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True,
                     is_direct_tcp=True)

conn.connect(server_ip, 445)

filename = "trust.bat"
share = "2fassassin"
path = "instruction"
file2transfer = open(filename,"r")
conn.storeFile(share,path + filename, file2transfer, timeout=30 )

conn.close()
