def checker(number, radix):
		num_to_str = str(number)
		i = 0
		while i < len(num_to_str):
			if int(num_to_str[i]) >= radix:
				raise ValueError('Number should be less than the radix')
			else:
				i += 1
		return True


def to_denary(num, radix):
	if checker(num, radix):
		i = -1
		in_denary = 0
		str_num = str(num)
		count = 0

		while i >= -len(str_num):
			the_conv = int(str_num[i]) * (radix**count)
			in_denary += the_conv
			i -= 1
			count += 1
		return in_denary

# double_digit_alpha = {
# 	10: 'A',
# 	11: 'B',
# 	12: 'C',
# 	13: 'D',
# 	14: 'E',
# 	15: 'F'
# }


class BaseConverter:
	double_digit_alpha = {
		10: 'A',
		11: 'B',
		12: 'C',
		13: 'D',
		14: 'E',
		15: 'F'
	}

	def __init__(self, number, from_base, to_base):
		self.to_base = to_base
		if not checker(number, from_base):
			raise ValueError('Invalid number')
		self.number = number
		self.from_base = from_base

	def conv(self):
		inDenary = to_denary(self.number, self.from_base)

