def pre_process(strr):
    """
    Write preprocessing to be performed on string to normalize string
    For now: string needs to be lower case
    Ideas:
        Group similar character by unsupervised learning, require CV and replace appropriate alphabet
    """
    strr = strr.lower()
    return strr

