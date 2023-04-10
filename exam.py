from example import split
import time

print(split("a b c d e f g h i j k l m n o p q r s t u v w x y z"))

QUOTATION = {"'", '"', "’", "“"}

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
    split1("a b c d e f g h i j k l m n o p q r s t u v w x y z")
print(time.perf_counter() - st)

st = time.perf_counter()
for i in range(10000):
    split("a b c d e f g h i j k l m n o p q r s t u v w x y z")
print(time.perf_counter() - st)