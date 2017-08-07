# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import jieba
from jieba import analyse

def segment(input, output):
    input_file = open(input, "r")
    output_file = open(output, "w")
    count = 0
    while True:
        line = input_file.readline()
        if count % 10000 == 0:
            print "segment lines: %d" % count
        if line:
            line = line.strip()
            seg_list = jieba.cut(line)
            segments = []

            for seg in seg_list:
                segments.append(seg + " ")

            segments.append("\n")
            output_file.write("".join(segments))
        else:
            break

        count += 1

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    if 3 != len(sys.argv):
        print "Usage: ", sys.argv[0], "input output"
        sys.exit(-1)
    segment(sys.argv[1], sys.argv[2]);
