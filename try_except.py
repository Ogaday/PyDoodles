try:
    raise Exception("hah")
except Exception as e:
    print e
    assert(e.args[0] == "hah")
