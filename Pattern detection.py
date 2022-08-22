def match(str, pat, dict, i=0, j=0):
	n = len(str)
	m = len(pat)
	if n < m:
		return False
	if i == n and j == m:
		return True
	if i == n or j == m:
		return False
	curr = pat[j]
	if curr in dict:
		s = dict[curr]
		k = len(s)
		if i + k < len(str):
			ss = str[i:i + k]
		else:
			ss = str[i:]
		if ss != s:
			return False
		return match(str, pat, dict, i + k, j + 1)
	for k in range(1, n - i + 1):
		dict[curr] = str[i:i + k]
		if match(str, pat, dict, i + k, j + 1):
			return True
		dict.pop(curr)
	return False

def pattern_detector(a,b):
	dict = {}   
	if match(a, b, dict):
		return "Yes"
	else:
	    return "No"

def main():
    k = input()
    res = []
    for i in range(int(k)):
        a = input()
        b = input()
        res.append(pattern_detector(a,b))
    for i in res:
        print(i)


main()


