# coding: utf-8
# triangular_pentagonal_hexagonal.py

from lib.X_number import triangle_num, is_pentagon, is_hexagon

n = 286

while(True):
	tri_num = triangle_num(n)
	if is_pentagon(tri_num) and is_hexagon(tri_num):
		print(tri_num)
		break
	n += 1




