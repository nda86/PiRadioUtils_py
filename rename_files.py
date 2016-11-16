import os

def run():
	# cwd = os.path.dirname(os.path.abspath(__file__))
	[os.rename(f, f.replace(' ', '_')) for f in os.listdir(.)]

if __name__ == "__main__":
	run()

