'''
2383. Minimum Hours of Training to Win a Competition

2022.08.21 Sunday 20:16
'''
from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        cnt = 0
        for en, ex in zip(energy, experience):
            if initialEnergy > en and initialExperience > ex:
                initialEnergy -= en
                initialExperience += ex
            elif initialEnergy > en and initialExperience <= ex:
                initialEnergy -= en
                training = ex - initialExperience + 1
                cnt += training
                initialExperience += training
                initialExperience += ex
            elif initialEnergy <= en and initialExperience > ex:
                initialExperience += ex
                training = en - initialEnergy + 1
                cnt += training
                initialEnergy += training
                initialEnergy -= en
            else:
                training_ex = ex - initialExperience + 1
                training_en = en - initialEnergy + 1
                cnt += training_en + training_ex

                initialEnergy += training_en
                initialEnergy -= en
                initialExperience += training_ex
                initialExperience += ex
        return cnt


if __name__ == "__main__":
    obj = Solution()
    assert obj.minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1])==8
    assert obj.minNumberOfHours(initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3])==0