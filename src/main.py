
from json import loads

# LOADING_TIP_0:0


TEMPLATE_TEXT: str = "LOADING_TIP_{}:0 "


class FileHandler(object):
	@staticmethod
	def read_file(file_name: str, prefix: str = "") -> str:
		with open(f"{prefix}{file_name}", 'r') as fp:
			return "".join(fp.readlines())


	@staticmethod
	def write_file(template_file: str, data: list[str], prefix: str = "") -> None:
		n: int = 0
		with open(f"{prefix}{template_file}", 'a') as fp:
			for line in data:
				line = "\t{} \"{}\"\n".format(TEMPLATE_TEXT.format(n), line)
				fp.write(line)
				n += 1
		return


def case_handler(data: str) -> list[str]:
	data = loads(data)
	r: list[str] = []
	for key, val in data.items():
		r += [ key ] * val
	return r


def main():
	data: str = FileHandler.read_file("bin/case.json")
	data = case_handler(data)
	FileHandler.write_file(
		template_file="bin/template.txt",
		data=data
	)


if __name__ == '__main__':
	main()
	exit(0)
