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



shares = conn.listShares()

for share in shares:
    if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
        sharedfiles = conn.listPath(share.name, '/')
        for sharedfile in sharedfiles:
            print(sharedfile.filename)

conn.close()
