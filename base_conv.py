# todo: Write a program to convert numbers from on radix to another

class Breaker:
	def __init__(self, from_no):
		self.from_no = from_no

	def int_breaker(self):
		return list((str(self)[i] for i in range(len(str(self)))))
		# from_no_str = str(self)
		# broken_list = []
		# for no in from_no_str:
		# 	broken_list.append(no)
		# return broken_list

	def base_ten_conv(self):
		broken_from_no = Breaker.int_breaker(self)
		base10 = 0
		i = -1
		count = 0
		while i >= -len(broken_from_no):
			to_denary = (int(broken_from_no[i]) * (10 ** count))
			base10 += to_denary
			i -= 1
			count += 1
		return base10


class Convert(Breaker):
		def __init__(self, from_no, from_base, to_base):
			self.from_no = from_no
			# self.to_no = to_no
			self.from_base = from_base
			self.to_base = to_base

		def in_denary(self):
			return Breaker.base_ten_conv(self.from_no)

		def __str__(self):
			return str(Breaker.base_ten_conv(self.from_no))


# myConvert = Convert(1001, 2, 10)
# print(myConvert.in_denary())


print(Breaker.int_breaker(23))
# print(Breaker.int_breaker(2345))
