import argparse
import sys

from cv import data, render


def main() -> None:
  parser = argparse.ArgumentParser(description='Generate CV as PDF')
  parser.add_argument('--lang', choices=['sv', 'en'], default='sv')
  parser.add_argument('--template', default='classic')
  args = parser.parse_args()

  try:
    resume = data.load(args.lang)
    output = render.render(resume, args.lang, args.template)
    print(f'Generated: {output}')
  except ValueError as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
  main()
