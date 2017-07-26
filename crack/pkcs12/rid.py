
# check if crack.log existed. If existed means cracking was performed
def median():
    _file= "/root/2fassassin/crack/pkcs12/crack.log"
    if ( not os.path.isfile(_file)):
        print("\n Error: Record not found. Please crack the passwords on client certificate first! \n")
        crack()
    else:
        print("\n Record is found. Start removing the passwords from client certificate .... ...\n")
        try:
            strip()
        except:
            print "\n Error: Failed to remove passwords from client certificate! \n"
            sys.exit()


# grep the cracked password. return the password
def identifier():
    '''
    COMMAND = "cat crack.log | grep 'Password found:' | awk '{print $9}'"
    subprocess.call(COMMAND, shell=True);return answer
    '''
    blowjob = "cat crack.log | grep 'Password found:' | awk '{print $9}'"
    p = subprocess.Popen(blowjob, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return output


# most important functio - to remove the passphrase from pfx
def strip():
    # grab the log, variable secret is the cracked password
    answer = identifier()
    print "\n Cracked password: ", answer



# clean up -delete crack.log
def restart():


'''
# this script doesn't work, need to generate pexpect to handle it.

#openssl pkcs12 -in <protected.p12.orig> -nodes -out <temp.pem>   # decrypts the original pkcs12 into a temporary pem file ( pem is a base64 encoded format)
#openssl pkcs12 -export -in <temp.pem>  -out <unprotected.p12>    # picks up pem file and constructs a new pkcs12 file
#rm <temp.pem>

    target = "/root/2fassassin/loot/*.pfx"

    mark = ""
    mark += "openssl pkcs12 -in "
    mark += target
    mark += " "
    mark += "-nodes -out temp.pem"
    os.system(mark)
    #time.sleep(2)
    stain = ""
    stain += "openssl pkcs12 -export -in temp.pem -out"
    stain += " "
    stain += "cracked_ClientCert.pfx"
    os.system(stain)
    #time.sleep(2)
    spot = ""
    spot += "rm temp.pem"
    os.system(spot)
    sys.exit()
'''





__all__ = [identifier', 'strip', 'median']
