cdef inline int contains(Py_UCS4 ch, tuple chs):
    cdef Py_ssize_t i = 0
    cdef Py_ssize_t length = len(chs)
    while i < length:
        if ch == chs[i]:
            return 1
        i += 1
    return 0


def split(text, separates=None, crlf=True):
    """尊重引号与转义的字符串切分

    Args:
        text (str): 要切割的字符串
        separates (tuple[str, ...]): 切割符. 默认为 " ".
        crlf (bool): 是否去除 \n 与 \r，默认为 True

    Returns:
        List[str]: 切割后的字符串, 可能含有空格
    """
    # separates = separates or (" ",)
    # result, quotation, escape = "", "", False
    cdef char escape = 0
    cdef list result = []
    cdef tuple _separates = separates or (" ",)
    cdef Py_UCS4 quotation = 0
    cdef Py_UCS4 ch = 0
    cdef Py_ssize_t i = 0
    cdef Py_ssize_t length = len(text)

    while i < length:
        ch = text[i]
        i += 1
        if contains(ch, ('\\',)):
            escape = 1
            result.append(ch)
        elif contains(ch, ('"', "'")):
            if quotation == 0:
                quotation = ch
                if escape:
                    result[-1] = ch
            elif ch == quotation:
                quotation = 0
                if escape:
                    result[-1] = ch
        elif (not quotation and ch in _separates) or (crlf and contains(ch, ('\r', '\n'))):
            if result and result[-1] != '\0':
                result.append('\0')
        else:
            result.append(ch)
            escape = 0
    return ''.join(result).split('\0') if result else []
