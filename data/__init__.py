import glob

from kivy.lang import Builder

for file in glob.glob('./*/*.kv'):
    Builder.load_file(file)
