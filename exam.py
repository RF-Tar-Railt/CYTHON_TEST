from example import split, split_once
import time

print(split("abc def ghi jk l m n o p q r s t u v w x y z", (" ",)))
text1 = "rrr b bbbb"
text2 = "\'rrr b\' bbbb"
text3 = "\\\'rrr b\\\' bbbb"
assert split(text1, (" ",)) == ["rrr", "b", "bbbb"]
assert split(text2, (" ",)) == ["rrr b", "bbbb"]
assert split(text3, (" ",)) == ["'rrr b'", "bbbb"]
assert split("", (" ",)) == []
assert split("  ", (" ",)) == []

print(split_once("abc def ghi jk l m n o p q r s t u v w x y z", (" ",)))
print(split_once(text1, (" ",)))
print(split_once(text2, (" ",)))
print(split_once(text3, (" ",)))
QUOTATION = {"'", '"', "’", "“"}


def split_once1(text: str, separates: tuple, crlf: bool = True):
    """单次分隔字符串"""
    index, out_text, quotation, escape = 0, "", "", False
    separates = tuple(separates)
    text = text.lstrip()
    for char in text:
        if char == "\\":
            escape = True
            out_text += char
        elif char in QUOTATION:  # 遇到引号括起来的部分跳过分隔
            if not quotation:
                quotation = char
                if escape:
                    out_text = out_text[:-1] + char
            elif char == quotation:
                quotation = ""
                if escape:
                    out_text = out_text[:-1] + char
        elif (char in separates or (crlf and char in {"\n", "\r"})) and not quotation:
            break
        else:
            out_text += char
            escape = False
        index += 1
    return out_text, text[index + 1:]


def split1(text: str, separates = None, crlf: bool = True):
    """尊重引号与转义的字符串切分

    Args:
        text (str): 要切割的字符串
        separates (tuple[str, ...]): 切割符. 默认为 " ".
        crlf (bool): 是否去除 \n 与 \r，默认为 True

    Returns:
        List[str]: 切割后的字符串, 可能含有空格
    """
    separates = separates or (" ",)
    result, quotation, escape = "", "", False
    for char in text:
        if char == "\\":
            escape = True
            result += char
        elif char in QUOTATION:
            if not quotation:
                quotation = char
                if escape:
                    result = result[:-1] + char
            elif char == quotation:
                quotation = ""
                if escape:
                    result = result[:-1] + char
        elif (not quotation and char in separates) or (crlf and char in {"\n", "\r"}):
            if result and result[-1] != "\0":
                result += "\0"
        else:
            result += char
            escape = False
    return result.split('\0') if result else []


st = time.perf_counter()
for i in range(10000):
    split_once1("a b c d e f g h i j k l m n o p q r s t u v w x y z", (" ",))
print(time.perf_counter() - st)


st = time.perf_counter()
for i in range(10000):
    split_once("a b c d e f g h i j k l m n o p q r s t u v w x y z", (" ",))
print(time.perf_counter() - st)