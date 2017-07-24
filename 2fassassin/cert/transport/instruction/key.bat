#!/bin/bash

certutil -user -p Password1 -importPFX ClientCert.pfx
"C:\Program Files\Internet Explorer\iexplore.exe" https://2fassassin.com
