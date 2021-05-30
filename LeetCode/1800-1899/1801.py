'''
1801. Number of Orders in the Backlog

2021.03.21 Sunday 13:47
'''
from typing import List
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []
        for price, amount, orderType in orders:
            if orderType == 0:
                # buy
                while (amount > 0) and (len(sell) > 0):
                    choose = sell[0]
                    if choose[0] > price:
                        break

                    deal = min(choose[1], amount)
                    amount -= deal
                    choose[1] -= deal

                    if choose[1] == 0:
                        heapq.heappop(sell)

                if amount > 0:
                    heapq.heappush(buy, [-price, amount])
            else:
                # sell
                while (amount > 0) and len(buy) > 0:
                    choose = buy[0]
                    if -choose[0] < price:
                        break

                    deal = min(choose[1], amount)
                    amount -= deal
                    choose[1] -= deal
                    if choose[1] == 0:
                        heapq.heappop(buy)

                if amount > 0:
                    heapq.heappush(sell, [price, amount])

        ret = sum([b[1] for b in buy]) + sum([s[1] for s in sell])
        ret = ret % (10**9 + 7)
        return ret


if __name__ == "__main__":
    obj = Solution()
    assert obj.getNumberOfBacklogOrders(orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]) == 6
    assert obj.getNumberOfBacklogOrders(orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]) == 999999984
    assert obj.getNumberOfBacklogOrders(orders = [[175891835,952269593,0],[759005039,631739681,1],[197966583,969787362,0],[250009004,123225423,0],[629989859,543571572,0],[774752939,286256149,1],[210777294,839031371,0],[387949845,489757871,1],[995422058,659809937,1],[235975421,993870556,0],[14978578,524782272,0],[176511890,271993132,0],[9854547,247056741,0],[562966683,877339786,0],[37693010,567105026,0],[224881238,475656687,1],[260941236,526653630,1],[348857806,420885379,0],[209638847,638146286,0],[201354822,734862469,1],[624124060,457671816,1],[390280826,24878863,1],[22178703,998617751,0],[707765727,671763052,1],[888322751,759855486,1],[363880803,79523394,1],[209694848,753363385,1],[904070790,893538886,1],[644210042,730672235,1],[648242454,505920215,0],[893438346,288049939,1],[604996078,821351816,1],[652171460,579509270,1],[274217850,333121117,0],[649189636,813223274,0],[839575338,491318873,1],[957677703,381755153,0],[545444479,476908928,0],[751087334,511100390,1],[747617674,671980249,0],[412204080,925920238,1],[58250732,689285277,0],[382595561,935798867,0],[274667802,806828526,0],[329037510,406666329,0],[348405490,363095219,1],[632633450,942703984,0],[223942989,769429332,0],[352875699,128726737,0],[137830703,838648165,1],[439870153,652230584,1],[249722388,29212886,0],[811242137,822720237,1],[324823226,315413300,1],[451440331,995508446,1],[870464013,930145653,0],[213663147,437774371,0],[652682640,45336979,0],[676188855,241113758,0],[765739194,423783585,1],[225645142,667732050,0],[773187268,321322186,1],[1571129,765220857,1],[477033467,534627573,0],[725045703,157181228,0],[398099791,469217022,1],[938856461,860274494,1],[341002405,648283160,0],[626648535,693444857,1],[870161336,588466038,1],[461208253,12125751,1],[807726643,92804416,1],[123443799,538104541,0],[934393687,650288970,1],[468981837,400221791,0],[58207862,110044378,0],[139291081,313594051,0],[949487491,73342835,0],[3404839,722023218,0],[454129687,785689556,0],[71045843,59070283,0],[37447315,577615810,1],[357246128,843047533,0],[656612769,9448120,0],[503540463,214866249,1],[317143754,624607010,1],[954332270,250736491,0],[226289862,420319060,0],[256185491,596281223,1],[37953432,355843365,1],[436755403,128577918,0],[604029628,198693611,0],[817640822,198482548,0],[241477023,189547224,1],[972480012,865475621,0],[63132275,853474897,1]]) == 623185516