#讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for text in f:
			chat.append(text.strip())
		return chat

def convert(lines):
	new = []
	person = None #先宣告變數，但無值
	for a in lines:
		if a == 'Allen':
			person = 'Allen'
			continue
		elif a == 'Tom':
			person = 'Tom'
			continue
		if person : # person若有值(不是none)，那就會執行
			new.append(person + ':' + a)
	return new

def write_file(filename, lines):
	with open(filename, 'w' ) as f:
		for line in lines:
			f.write(line + '\n')



def main():
	chats = read_file('input.txt')
	chats = convert(chats)
	write_file('finish.txt', chats)

main()