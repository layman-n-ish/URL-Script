import webbrowser 
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--link_to_txt", required = True, 
help = "Link to the text file to open.")
args = vars(parser.parse_args())

with open(args["link_to_txt"], 'r') as f:
    for (i, l) in enumerate(f): 
        try:
            url = l.rstrip('\n')
            if (i == 0):
                webbrowser.open(url, new=1)
            else:
                webbrowser.open_new_tab(url)
        except Exception as e:
            print(str(e))

