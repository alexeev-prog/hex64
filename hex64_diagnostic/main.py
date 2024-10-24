import sys
from hex64_diagnostic.utils.other import print_msg
from hex64_diagnostic.interfaces.gui.hex64gui import launch_app


def main():
	try:
		launch_app()
	except Exception as ex:
		print_msg(f'Error: {ex}', 'error')
		sys.exit(1)


if __name__ == '__main__':
	main()
