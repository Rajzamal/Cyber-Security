f = open("C:/Windows/System32/drivers/etc/hosts", "a")
str = "\n127.0.0.1         www.facebook.com\n127.0.0.1         facebook.com\n127.0.0.1         m.facebook.com"
f.write(str)
f.close()
