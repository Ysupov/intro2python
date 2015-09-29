print "vvedite tekushii god",
cyear = raw_input (">")
print "vvedite god rojdenia"
byear = raw_input (">")
age = int (cyear) - int (byear)
print "vash vozrast",age
if age > 0 and age <=6:
	print "idi v det sad"
if 7<=17:
	print "uchis v shkole horosho"
if 18<=19:
	print "podumai postupit ili rabotat"
if 20<=24:
	print "ty student ili ty rabotaesh"
if 25<=35:
	print "ty jenilsya i rabotaew"
if 36<=45:
	print "u tebya est deti"
if 46<=70:
	print "ty hochew spokoino do zhit do 100"
if 70<=90:
	print "ty pencioner"
