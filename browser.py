import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style

#dir for test
directory = "C:/Users/main/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs/"

# directory = sys.argv[1]
if not os.path.exists(directory):
    os.mkdir(directory)

url_stack = []


def get_site_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.get_text()


def save_site_content(data, path):
    url_stack.append(path)
    with open(os.path.join(directory, path), 'w') as f:
        f.write(data)


def go_site(site):
    address = site if site.startswith("https://") else f"https://{site}"
    site_content = get_site_content(address)
    save_site_content(site_content, site)
    print(Fore.BLUE + site_content)


def go_back():
    url_stack.pop()
    with open(os.path.join(directory, url_stack.pop())) as f:
        print(f.read())


while True:
    command = input()
    if command == 'exit':
        break
    if command == 'back':
        go_back()
    elif '.' in command:
        go_site(command)
    else:
        print('Error: Incorrect URL')



# nytimes_com = '''
# This New Liquid Is Magnetic, and Mesmerizing
#
# Scientists have created “soft” magnets that can flow
# and change shape, and that could be a boon to medicine
# and robotics. (Source: New York Times)
#
#
# Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
#
# Jessica Wade has added nearly 700 Wikipedia biographies for
#  important female and minority scientists in less than two
#  years.
#
# '''
#
# bloomberg_com = '''
# The Space Race: From Apollo 11 to Elon Musk
#
# It's 50 years since the world was gripped by historic images
#  of Apollo 11, and Neil Armstrong -- the first man to walk
#  on the moon. It was the height of the Cold War, and the charts
#  were filled with David Bowie's Space Oddity, and Creedence's
#  Bad Moon Rising. The world is a very different place than
#  it was 5 decades ago. But how has the space race changed since
#  the summer of '69? (Source: Bloomberg)
#
#
# Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
#
# Twitter and Square Chief Executive Officer Jack Dorsey
#  addressed Apple Inc. employees at the iPhone maker’s headquarters
#  Tuesday, a signal of the strong ties between the Silicon Valley giants.
# '''
