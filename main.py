import argparse

def main():
	# set up command line arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('ROM_path', help="Provide path to ROM of choice")
    args = parser.parse_args()  

    # TODO: validate ROM path is correct
    print(args.ROM_path)  
 
    with open(args.ROM_path, 'rb') as file:
        contents = file.readlines()

    print(contents)


if __name__ == '__main__':
    main()
