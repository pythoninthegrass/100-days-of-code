#!/usr/bin/env python3

import argparse
import arrow
import sys
import textwrap
from icecream import ic
from pathlib import Path
from time import sleep
from tqdm.auto import trange

# verbose icecream
ic.configureOutput(includeContext=True)

# env
home = Path.home()
cwd = Path.cwd()
env = Path('.env')
notes = Path('../notes').mkdir(exist_ok=True)
today = arrow.now().format('YYYY/MM/DD')

# accept args
parser = argparse.ArgumentParser(description='Generate 100 markdown files under the notes directory.')
parser.add_argument('-s', '--start', help='start date', default=f'{today}')
args = parser.parse_args()


def gen_notes(start_date):
    """
    Generates 100 markdown files under the notes directory.

    Fills in boilerplate details with the filename, day, date, and example number.
    """
    fn = 'log'
    day = 0

    example = 0
    start = arrow.get(start_date).shift(days=-1)

    total = range(1, 101)

    for num in total:
        day += 1
        date = start.shift(days=day).format('MMMM DD, YYYY')
        example += 1

        # file format
        md_file = Path(f'../notes/{fn}_{num}.md')

        # create file if it doesn't exist
        md_file.touch(mode=0o700, exist_ok=True)

        md_fmt = textwrap.dedent(f"""
        # 100 Days Of Code - Log

        ### Day {day}: {date} (Example {example})
        ##### (delete me or comment me out)

        **Today's Progress**: ...

        **Thoughts:** ...

        **Link to work:** [Calculator App](https://github.com/username/reponame)
        """)

        # write to file
        md_file.write_text(md_fmt, encoding='utf-8', errors=None)

        # progress bar
        bar = trange(100, desc=f'{fn}_{num}', position=0, leave=True)
        for i in bar:
            bar.update()


if __name__ == '__main__':
    # check if args were passed or default value
    if len(sys.argv) > 1:
        print(f'Generating notes from {args.start}')
    else:
        print('Generating notes from today')

    # validate input then generate notes
    try:
        prompt = input('Continue? (y/n): ').lower()
        match prompt:
            case 'y' | 'yes':
                start_date = args.start
                if not start_date:
                    print('No date provided, using current date')
                else:
                    print(f'Using date: {start_date}')
                gen_notes(start_date)
            case 'n' | 'no':
                print('Exiting...')
                exit()
            case _:
                print('Invalid input, exiting...')
                exit()
    except KeyboardInterrupt as k:
        print(f"\nError {k}: User canceled. Exiting...")
        exit()
