import fileinput
import optparse


def canonicalize(input):
    for line in input:
        yield line.strip().lower()


def filter_nonwords(input, words):
    words = set(words)
    for word in input:
        if word in words:
            yield word


def main():
    parser = optparse.OptionParser("%prog [options] [file...]")
    parser.add_option("-w", "--words-file", default="/usr/share/dict/words",
                      help=("Path to words file. Any words in the input that"
                            " are not contained in WORDS_FILE will be filtered"
                            " out. [default = %default]"))
    opts, args = parser.parse_args()

    with open(opts.words_file) as words_file:
        for word in filter_nonwords(canonicalize(fileinput.input(args)),
                                    canonicalize(words_file)):
            print word


if __name__ == '__main__':
    main()
