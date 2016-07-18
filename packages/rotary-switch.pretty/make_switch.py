import math

def pad(number, x, y, size, drill):
	return "  (pad {0:} thru_hole circle (at {1:.4f} {2:.4f}) (size {3:.4f} {3:.4f}) (drill {4:.4f}) (layers *.Cu *.Mask F.SilkS))".format(number, x, y, size, drill)

def get_pad_angle(pad):
	return math.radians(15 + ((n-1) *  30))

outer_r = 22
inner_r = 8

for n in range(1, 13):
	
	angle = get_pad_angle(n)

	x = -math.cos(angle) * outer_r
	y = -math.sin(angle) * outer_r

	print( pad(n, x, y, 2.4, 1.4) )

for n, c in enumerate(["A", "B", "C", "D"]):

	angle = math.radians(45 + (n * 90))

	x = -math.cos(angle) * inner_r
	y = -math.sin(angle) * inner_r

	print( pad(c, x, y, 2.4, 1.4) )

print(")")