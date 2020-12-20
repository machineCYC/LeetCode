'''
1694. Reformat Phone Number

2020.12.20 Sunday 13:00
'''


class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [i for i in number if (i!=" " and i!="-" and i!="/" and i!=".")]
        n = len(digits)
        s = ""
        while len(digits)>4:
            s += "".join(digits[:3])
            digits = digits[3:]
            s += "-"

        if len(digits)==4:
            s += "".join(digits[:2])
            s += "-"
            s += "".join(digits[2:])
        else:
            s += "".join(digits)
        return s

if __name__ == "__main__":
    obj = Solution()
    assert obj.reformatNumber(number="1-23-45 6")=="123-456"
    assert obj.reformatNumber(number="123 4-567")=="123-45-67"
    assert obj.reformatNumber(number="123 4-5678")=="123-456-78"
    assert obj.reformatNumber(number="12")=="12"
    assert obj.reformatNumber(number="--17-5 229 35-39475 ")=="175-229-353-94-75"
