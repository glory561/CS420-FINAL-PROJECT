from programming import glo

while True:
	text = input('glo > ')
	if text.strip() == "":
		continue

	if text.startswith("run "):
		filename = text[4:].strip()
		try:
			with open(filename, "r") as f:
				script = f.read()
			result, error = glo.run(filename, script)
		except FileNotFoundError:
			print(f"File '{filename}' not found.")
			continue
	else:
		result, error = glo.run("<stdin>", text)

	if error:
		print(error.as_string())
	elif result:
		if hasattr(result, 'elements') and len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))

