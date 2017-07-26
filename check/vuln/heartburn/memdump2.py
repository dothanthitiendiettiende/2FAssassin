#!/usr/bin/python

import sys, base64, gmpy
from pyasn1.codec.der import encoder
from pyasn1.type.univ import *

def main ():
        n = int (sys.argv[2], 16)
        keysize = n.bit_length() / 16
        with open (sys.argv[1], "rb") as f:
                chunk = f.read (16384)
                while chunk:
                        for offset in xrange (0, len (chunk) - keysize):
                                p = long (''.join (["%02x" % ord (chunk[x]) for x in xrange (offset + keysize - 1, offset - 1, -1)]).strip(), 16)
                                if gmpy.is_prime (p) and p != n and n % p == 0:
                                    e = 65537
                                    q = n / p
                                    phi = (p - 1) * (q - 1)
                                    d = gmpy.invert (e, phi)
                                    dp = d % (p - 1)
                                    dq = d % (q - 1)
                                    qinv = gmpy.invert (q, p)
                                    seq = Sequence()
                                    for x in [0, n, e, d, p, q, dp, dq, qinv]:
                                        seq.setComponentByPosition (len (seq), Integer (x))
                                        print "\n\n-----BEGIN RSA PRIVATE KEY-----\n%s-----END RSA PRIVATE KEY-----\n\n" % base64.encodestring(encoder.encode (seq))
                                        sys.exit (0)
                        chunk = f.read (16384)
                print "private key not found :("

                if __name__ == '__main__':
                    main()
