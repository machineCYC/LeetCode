'''
1592. Rearrange Spaces Between Words

2020.09.20 Sunday 15:03
'''

class Solution:
    def reorderSpaces(self, text: str) -> str:
        nbr_spaces = sum([1 for i in text if i==" "])
        stext = text.split(" ")
        words = [i for i in stext if i!=""]
        nbr_words = len([i for i in stext if i!=""])

        if nbr_words == 1:
            ret = text.strip() + nbr_spaces * " "
        else:
            nbr_adjacent_spcace = int(nbr_spaces / (nbr_words-1))
            nbr_extra_spcace = nbr_spaces % (nbr_words-1)

            adjacent_spcace = " "*nbr_adjacent_spcace
            ret = adjacent_spcace.join(words)
            ret += nbr_extra_spcace * " "
        return ret


if __name__ == "__main__":
    obj = Solution()
    assert obj.reorderSpaces(text="  this   is  a sentence ")=="this   is   a   sentence"
    assert obj.reorderSpaces(text=" practice   makes   perfect")=="practice   makes   perfect "
    assert obj.reorderSpaces(text="hello   world")=="hello   world"
    assert obj.reorderSpaces(text="  walks  udp package   into  bar a")=="walks  udp  package  into  bar  a "
    assert obj.reorderSpaces(text="a")=="a"
    assert obj.reorderSpaces(text="  hello")=="hello  "
