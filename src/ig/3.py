"""
input_pad는 반드시 직(정)사각형의 형태로 온다고 전제합니다.
벽 = #, 길 = O
"""


def refine_pad(input_pad):
	pad = []
	area_id = 0
	for i in range(len(input_pad[0])):
		for j in range(len(input_pad)):
			if input_pad[j][i] == '#':
				area_id += 1
			else:
				input_pad[j][i] = area_id
		area_id += 1

	area_id = 0
	for i in range(len(input_pad)):
		for j in range(len(input_pad[0])):
			if input_pad[i][j] == '#':
				area_id += 1
			else:
				pad.append((area_id, input_pad[i][j]))
		area_id += 1
	return pad


def tracking(
		num, start_i,
		max_horizon, vertical_area,
		pad, pad_len, answer
):
	for i in range(start_i, pad_len):
		if pad[i][0] > max_horizon and pad[i][1] not in vertical_area:
			tracking(
				num + 1, i + 1,
				pad[i][0],
				vertical_area + [pad[i][1]],
				pad, pad_len, answer
			)
	if answer['p_num'] == num:
		answer['case'] += 1
	elif answer['p_num'] < num:
		answer['p_num'], answer['case'] = num, 1


def solution(input_pad):
	answer = {'p_num': 0, 'case': 0}
	pad = refine_pad(input_pad)
	tracking(0, 0, -1, [], pad, len(pad), answer)
	return f"최대 {answer['p_num']}명, {answer['case']}가지"


if __name__ == '__main__':
	import time
	# 벽 = #, 길 = O
	print(solution([
		["O", "O", ],
		["O", "O", ],
	]))
	print(solution([
	    ["#","#","#","O",],
	    ["O","O","O","O",],
	    ["O","#","O","O",],
	    ["#","#","#","O",],
	]))
	print(solution([
		["O","O","O","#","O","O","O","O",],
		["O","O","O","O","O","#","O","#",],
		["O","#","O","O","O","O","O","O",],
		["O","O","O","O","#","O","#","O",],
	]))
	start = time.time()
	print(solution([
		["O","#", "O", "#", "O", "#", "O", "#"],
		["O","O", "O", "O", "O", "#", "O", "O"],
		["#","O", "#", "O", "O", "#", "O", "#"],
		["O","O", "O", "O", "O", "O", "O", "O"],
	    ["O","O", "O", "#", "O", "O", "O", "O"],
	    ["O","O", "O", "O", "O", "#", "O", "#"],
	    ["O","#", "O", "O", "O", "O", "O", "O"],
	    ["O","O", "O", "O", "#", "O", "#", "O"],
	]))
	print("time:", time.time() - start)