__author__ = 'liufule12'


def line_extract(read_filename, extract_line_num, write_filename1, write_filename2):
    """Extract a line form a file, and the other lines write into another file.

    Parameters:
    -----------

    read_filename: string
        The read file name.

    extract_line_num: int
        The extracted line num.

    write_filename1: string
        The only one line write file name.

    write_filename2: string
        The other lines write file name.
    """
    with open(read_filename) as f_read:
        lines = f_read.readlines()
        write_line = lines[extract_line_num-1]
        del lines[extract_line_num-1]

    with open(write_filename1, 'w') as f_write:
        f_write.writelines(lines)

    with open(write_filename2, 'w') as f_write:
        f_write.write(write_line)


def write_libsvm(pos_vec, neg_vec, filename):
    """Write the positive feature vector and negative feature vector into the libsvm format.

    Parameters
    ----------

    pos_vec : a 1-D list of list
        Each element in the list is a feature vector.

    neg_vec : a 1-D list of list
        The same as pos_vec.

    filename : string
        The write file name.

    """
    with open(filename, 'w') as f_write:
        for vec in pos_vec:
            line = str(1)
            i = 1
            for feature in vec:
                line += ' ' + str(i) + ':' + str(feature)
                i += 1
            line += '\n'
            f_write.write(line)

        for vec in neg_vec:
            line = str(0)
            i = 1
            for feature in vec:
                line += ' ' + str(i) + ':' + str(feature)
                i += 1
            line += '\n'
            f_write.write(line)


def generate_fasta(read_filename, write_filename):
    """Transform a file into a FASTA format file.

    Parameters:
    -----------

    read_filename: string
        The file name need to transform. The file format is same as file 'H_sapiens_pos.txt'

    write_filename: string
        The transformed file name.

    """
    with open(read_filename) as f_read:
        with open(write_filename, 'w') as f_write:
            lines = f_read.readlines()
            line_num = 1

            # Process the first line.
            if 0 < len(lines[0]) <= 70:
                write_line = ''.join(['>', str(line_num), '\n'])
                f_write.write(write_line)
                line_num += 1
            else:
                print 'generate_fasta error! The first line is None!'
                return
            del lines[0]

            # Process the last line.
            last_line = lines[-1]
            del lines[-1]

            # Process the other lines.
            for line in lines:
                if line[0] < '0' or line[0] > '9':
                    write_line = ''.join([line])
                    f_write.write(write_line)
                    if 0 < len(line) < 70:
                        f_write.write('\n')
                        write_title = ''.join(['>', str(line_num), '\n'])
                        f_write.write(write_title)
                        line_num += 1

            if (last_line[0] < '0' or last_line > '9') and 0 < len(last_line) <= 70:
                write_line = ''.join([last_line, '\n'])
                f_write.write(write_line)


if __name__ == '__main__':
    # from repDNA.psenac import PseDNC
    #
    # # Generate the PseDNC feature vector.
    # psednc = PseDNC(lamada=3, w=0.05)
    # pos_vec = psednc.make_psednc_vec(open('hotspots.fasta'))
    # neg_vec = psednc.make_psednc_vec(open('coldspots.fasta'))
    #
    # write_libsvm(pos_vec, neg_vec, 'libsvm_vec.txt')
    #
    # line_extract('libsvm_vec.txt', 2, 'extract1.txt', 'extract2.txt')

    generate_fasta('H_sapiens_pos.txt', 'H_sapiens_pos.fasta')
    generate_fasta('H_sapiens_neg.txt', 'H_sapiens_neg.fasta')