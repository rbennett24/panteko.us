import re

gloss_div = """<div data-gloss>
	<p>{l1}</p>
	<p>{gls}</p>
	<p>{l2}</p>
</div><br>"""

html = """<html>
	<head>
		<link rel="stylesheet" href="leipzig.js/dist/leipzig.css">
	</head>
	<body>
		{exs}
		<script src="leipzig.js/dist/leipzig.js"></script>
    	<script>
    		document.addEventListener('DOMContentLoaded', function(){{
        		Leipzig().gloss();
        	}});
        </script>
    </body>
</html>"""

def format_gls(f):
	gloss_list = []
	for line in f:
		x = re.split(r'\t+', line)
		gloss_block = gloss_div.format(l1 = x[0], gls = x[1], l2 = x[2])
		gloss_list.append(gloss_block)

	return '\n'.join(gloss_list)


def main():

	with open("xoqoneb_examples_tab.txt", "r") as txtfile:
		s = format_gls(txtfile)
		h = html.format(exs = s)


	with open("examples.html", "w") as htmlfile:
		htmlfile.write(h)
		
if __name__ == '__main__':
	main() 