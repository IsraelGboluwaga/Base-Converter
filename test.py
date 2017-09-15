def int_breaker(from_no):
	from_no_str = str(from_no)
	broken_list = []
	for no in from_no_str:
		broken_list.append(no)
	return broken_list


def base_ten_conv(from_no, base):
	broken_from_no = int_breaker(from_no)
	total = 0
	i = -1
	count = 0
	while i >= -len(broken_from_no):
		to_denary = (int(broken_from_no[i]) * (base**count))
		total += to_denary
		i -= 1
		count += 1
	return total



print(base_ten_conv(1001,2))