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
    with open(read_filename) as f:
        lines = f.readlines()
        write_line = lines[extract_line_num-1]
        del lines[extract_line_num-1]

    with open(write_filename1, 'w') as f:
        f.writelines(lines)

    with open(write_filename2, 'w') as f:
        f.write(write_line)


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
    with open(filename, 'w') as f:
        for vec in pos_vec:
            line = str(1)
            i = 1
            for feature in vec:
                line += ' ' + str(i) + ':' + str(feature)
                i += 1
            line += '\n'
            f.write(line)

        for vec in neg_vec:
            line = str(0)
            i = 1
            for feature in vec:
                line += ' ' + str(i) + ':' + str(feature)
                i += 1
            line += '\n'
            f.write(line)


if __name__ == '__main__':
    from repDNA.psenac import PseDNC

    # Generate the PseDNC feature vector.
    psednc = PseDNC(lamada=3, w=0.05)
    pos_vec = psednc.make_psednc_vec(open('hotspots.fasta'))
    neg_vec = psednc.make_psednc_vec(open('coldspots.fasta'))

    write_libsvm(pos_vec, neg_vec, 'libsvm_vec.txt')

    line_extract('libsvm_vec.txt', 2, 'extract1.txt', 'extract2.txt')