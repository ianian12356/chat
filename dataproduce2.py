#讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for text in f:
			chat.append(text.strip())
		return chat

def convert(lines):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_img_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_img_count = 0
	for a in lines:
		s = a.split(' ')
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count +=1
			elif s[2] == '圖片':
				allen_img_count +=1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count +=1
			elif s[2] == '圖片':
				viki_img_count +=1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen says', allen_word_count, 'words')
	print('Viki says', viki_word_count, 'words')
	print('Allen uses', allen_sticker_count, 'stickers')
	print('Viki uses', viki_sticker_count, 'stickers')
	print('Allen uses', allen_img_count, 'imgs')
	print('Viki uses', viki_img_count, 'imgs')


def write_file(filename, lines):
	with open(filename, 'w' ) as f:
		for line in lines:
			f.write(line + '\n')


def main():
	a = read_file('LINE-Viki.txt')
	convert(a)

main()