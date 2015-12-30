# encoding=utf-8
__author__ = 'Fule Liu'


import os

import const

"""File line statistic model."""


def code_statistic(filename):
    """Code line statistic."""
    try:
        with open(filename) as fp:
            lines = fp.readlines()
            const.CODE_LINES += len(lines)
            print(filename, len(lines))
    except UnicodeDecodeError:
        const.ERROR_INFO = "\n".join([const.ERROR_INFO, "".join(["UnicodeDecodeError: ", filename])])


def path_walk(fold, ban_fold, ban_suffix, ban_file, spe_suffix=None):
    """Recursive traverse the folds and files."""
    files = os.listdir(fold)

    # recursive end.
    if not files:
        return

    for cur_file in files:
        cur_path = os.path.join(fold, cur_file)
        suffix = cur_path.split(".")[-1]

        # Ban specified fold and file.
        if cur_path in ban_fold or cur_path in ban_file:
            continue

        if not os.path.isdir(cur_path):
            # Ban not specific file.
            if spe_suffix and suffix not in spe_suffix:
                continue

            # Ban specified suffix
            if suffix in ban_suffix:
                continue

            code_statistic(cur_path)
        else:
            # recursive walk.
            path_walk(cur_path, ban_fold, ban_suffix, ban_file, spe_suffix)


if __name__ == "__main__":
    FOLD = "F:\GitHub\Pse-in-One"
    BAN_FOLD = ["F:\GitHub\Pse-in-One\.git", "F:\GitHub\Pse-in-One\.idea"]
    BAN_SUFFIX = ["pyc", "pdf", "md", "txt", "res", "fasta"]
    BAN_FILE = []
    SPE_SUFFIX = ["py"]

    print("Traverse file:")
    path_walk(FOLD, BAN_FOLD, BAN_SUFFIX, BAN_FILE, SPE_SUFFIX)
    print("File lines:")
    print(const.CODE_LINES)
    print(const.ERROR_INFO)
