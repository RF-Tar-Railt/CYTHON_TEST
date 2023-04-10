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
    escape = False
    cdef str result = ""
    cdef tuple _separates = separates or (" ",)
    cdef Py_UCS4 quotation = ''
    cdef Py_UCS4 ch
    cdef Py_ssize_t i = 0
    cdef Py_ssize_t length = len(text)

    while i < length:
        ch = text[i]
        i += 1
        if ch == '\\':
            escape = True
            result += ch
        elif ch in "\'\"":
            if not quotation:
                quotation = ch
                if escape:
                    result = result[:-1] + ch
            elif ch == quotation:
                quotation = ''
                if escape:
                    result = result[:-1] + ch
        elif (not quotation and ch in _separates) or (crlf and ch in {"\n", "\r"}):
            if result and result[-1] != "\0":
                result += "\0"
        else:
            result += ch
            escape = False
    return result.split('\0') if result else []
