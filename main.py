import sys

from stats import report_findings_on

def main():
    if len(sys.argv) < 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    report_findings_on(sys.argv[1])

if __name__ == "__main__":
    main()
