from fileclean import cleanfc as clean


def test_cleanwork():
    with open("./tests/from/file1.txt", "w") as f:
        f.write("from")
    fromPath = "./tests/from/"
    toPath = "./tests/to/"
    clean.cleanwork(fromPath, toPath, r".*\.txt", "move")
