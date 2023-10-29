from typing import List
from collections import defaultdict


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        # def search(offers, i, m): # Brute Force
        #     k = -1
        #     for j in range(i+1, m):
        #         if offers[j][0] > offers[i][1]:
        #             k = j
        #             break
        #     return k

        def search(offers, i, m): # binary search
            l, h = i + 1, m - 1
            k = -1
            while l <= h:
                mid = (l + h) // 2
                if offers[mid][0] > offers[i][1]:
                    k = mid
                    h = mid - 1
                else:
                    l = mid + 1
            return k

        def solve(i, m, offers):
            if i >= m:
                return 0

            if dp[i] != -1:
                return dp[i]

            k = search(offers, i, m)
            a = solve(i+1, m, offers)
            b = offers[i][2] if k == -1 else offers[i][2] + solve(k, m, offers)
            dp[i] = max(a, b)
            return dp[i]

        dp = [-1] * 100001
        offers.sort(key=lambda x: x[0])
        m = len(offers)
        ans = solve(0, m, offers)
        return ans


if __name__ == "__main__":
    obj = Solution()
    assert obj.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]) == 3
    assert obj.maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]) == 10
    assert obj.maximizeTheProfit(n = 780, offers = [[57,168,128],[54,280,536],[559,634,527],[225,484,874],[29,579,99],[0,383,33],[83,733,717],[261,581,707],[253,553,356],[56,580,725],[22,154,735],[107,722,505],[304,484,684],[195,371,529],[401,516,926],[587,639,904],[337,765,880],[70,588,824],[139,442,325],[384,708,593],[84,705,511],[21,32,822],[248,487,907],[482,582,738],[21,201,643],[105,534,988],[157,402,419],[308,380,12],[234,712,648],[218,733,377],[68,734,142],[454,760,711],[110,457,56],[172,293,929],[63,269,438],[147,381,138],[186,607,937],[5,220,600],[369,754,151],[152,617,86],[319,589,66],[196,519,705],[172,330,332],[495,648,17],[197,736,473],[440,645,584],[313,359,1],[168,566,466],[624,684,947],[306,676,946],[149,662,175],[252,769,278],[629,667,737],[35,582,51],[407,564,245],[3,731,547],[13,145,254],[432,690,692],[65,241,434],[253,584,158],[420,478,1000],[500,562,532],[43,683,167],[473,734,747],[205,518,283],[46,467,483],[668,758,30],[218,636,445],[256,449,407],[485,568,993],[432,760,575],[633,759,763],[422,493,794],[224,370,170],[474,492,24],[274,467,51],[678,748,15],[173,582,139],[572,766,264],[142,407,47],[699,743,481],[21,411,840],[176,670,611],[391,478,754],[206,407,585],[575,725,108],[366,632,877],[175,559,583],[304,492,722],[262,387,478],[241,318,144],[52,304,253],[227,614,839],[103,152,668],[328,686,535],[236,326,463],[0,184,721],[45,166,671],[251,627,97],[398,745,200],[92,585,69],[335,721,147],[360,448,695],[213,556,491],[166,462,86],[143,197,992],[41,764,22],[271,760,459],[313,680,469],[115,749,293],[240,529,763],[532,596,473],[528,647,514],[441,761,810],[158,384,648],[558,672,363],[82,755,197],[690,765,329],[35,444,93],[523,688,794],[95,135,500],[152,182,19],[75,312,364],[442,708,720],[7,430,203],[293,755,169],[100,225,805],[30,664,92],[150,290,682],[85,761,181],[150,713,64],[450,547,497],[196,446,371],[370,425,191],[378,619,31],[216,421,140],[254,750,577],[362,564,62],[314,735,985],[62,410,205],[493,777,770],[92,232,681],[231,758,535],[135,756,545],[92,528,298],[648,683,624],[73,395,25],[78,345,831],[138,752,20],[427,543,104],[287,728,612],[390,436,353],[145,324,499],[300,313,42],[53,764,798],[27,83,522],[169,603,659],[316,656,873],[139,635,347],[253,516,277],[431,546,551],[72,311,855],[273,309,671],[7,498,862],[128,634,326],[425,467,53],[82,443,808],[114,146,579],[115,399,364],[33,597,227],[223,701,550],[669,766,18],[182,626,276],[136,581,648],[355,508,650],[5,146,287],[58,220,367],[136,653,911],[35,685,783],[165,581,109],[652,774,433],[342,664,855],[350,433,831],[48,452,137],[507,630,348],[204,620,176],[77,730,535],[227,442,258],[148,161,495],[184,212,689],[396,622,322],[72,283,846],[238,768,557],[463,474,433],[34,584,46],[346,596,817],[138,555,910],[223,448,521],[140,522,729],[554,662,830],[37,39,686],[37,580,439],[10,409,87],[370,472,125],[118,348,770],[339,556,877],[16,732,378],[564,626,544],[5,234,879],[392,589,211],[118,429,885],[262,388,466],[385,721,471],[389,517,178],[342,438,17],[244,775,926],[77,198,851],[477,670,319],[204,294,691],[457,501,631],[380,759,88],[118,147,103],[126,674,546],[147,260,951],[523,698,709],[552,726,999],[234,313,284],[248,250,720],[86,508,749],[126,401,763],[168,169,435],[116,540,102],[83,98,750],[344,556,371],[518,765,852],[3,635,750],[200,290,593],[91,226,978],[226,756,244],[29,650,951],[22,182,860],[268,760,568],[31,356,401],[443,687,910],[520,746,368],[225,264,615],[204,402,564],[139,164,833],[250,268,149],[434,470,155],[335,693,285],[163,536,346],[506,727,370],[107,360,785],[59,694,468],[31,56,341],[349,711,763],[275,618,501],[42,115,217],[53,446,973],[569,696,730],[421,751,717],[257,606,117],[410,654,669],[667,754,842],[574,752,2],[312,728,948],[315,655,565],[115,289,882],[250,495,425],[16,419,967],[95,570,828],[118,546,136],[589,593,172],[367,367,577],[131,755,641],[468,539,80],[453,608,420],[417,467,937],[58,120,703],[522,634,264],[393,610,638],[143,660,418],[556,655,366],[22,606,455],[373,617,403],[131,710,78],[106,210,868],[95,644,82],[138,574,134],[473,596,89],[260,456,235],[629,701,855],[753,761,597],[135,331,132],[103,383,632],[416,628,352],[680,740,728],[273,403,341],[174,507,748],[152,715,301],[26,357,696],[187,371,462],[330,333,800],[24,44,782],[230,269,491],[252,575,22],[20,118,486],[108,607,504],[544,607,519],[304,658,272],[551,689,643],[203,672,369],[521,634,394],[363,543,715],[250,482,852],[483,542,633],[35,668,594],[40,282,874],[392,724,117],[78,594,779],[283,668,613],[115,605,554],[165,694,878],[27,79,625],[114,541,373],[278,319,638],[26,395,383],[254,504,517],[212,362,315],[562,584,910],[161,509,636],[257,664,790],[96,375,573],[142,734,493],[271,544,450],[378,396,432],[85,297,695],[96,127,946],[386,473,406],[484,632,89],[4,734,245],[181,496,384],[176,198,406],[530,689,537],[108,291,238],[462,548,732],[429,751,375],[371,497,977],[28,749,5],[68,684,505],[170,457,756],[73,626,209],[47,243,576],[318,775,862],[429,633,317],[151,446,589],[51,236,494],[621,779,225],[57,339,234],[306,576,600],[520,601,924],[473,566,241],[223,670,960],[335,496,864],[721,723,761],[582,691,963],[336,700,307],[240,451,323],[541,700,498],[5,164,316],[370,722,635],[668,706,206],[22,461,444],[229,692,308],[300,637,105],[373,531,277],[77,562,713],[643,714,102],[174,439,471],[297,404,398],[56,162,937],[97,272,401],[388,482,447],[193,517,749],[280,289,283],[152,293,683],[67,375,179],[51,521,742],[128,533,424],[186,292,657],[200,713,319],[602,638,588],[542,731,206],[101,617,714],[183,368,128],[436,517,361],[390,657,372],[119,420,946],[210,667,47],[179,289,597],[133,725,740],[42,264,10],[71,432,438],[1,515,106],[422,689,319],[510,671,117],[89,448,920],[202,487,369],[155,271,193],[107,287,989],[35,705,769],[446,484,588],[34,131,22],[50,371,947],[59,71,424],[9,657,29],[41,315,147],[297,326,197],[262,744,588],[72,409,504],[498,629,417],[722,768,656],[122,421,850],[71,339,24],[136,602,231],[472,731,993],[606,659,577],[210,498,987],[324,544,737],[252,552,182],[675,775,233],[692,693,223],[418,453,697],[139,278,102],[16,523,915],[98,369,277],[59,716,604],[66,685,70],[227,571,51],[82,575,314],[582,765,469],[136,379,866],[156,181,957],[619,761,177],[218,706,621],[93,612,552],[613,737,497],[2,293,155],[26,483,63],[456,617,874],[372,575,566],[98,657,621],[262,512,55],[320,777,898],[351,406,81],[21,730,388],[52,588,296],[142,496,376],[734,768,630],[497,697,836],[443,775,414],[265,319,665],[139,602,939],[365,371,123],[91,756,137],[214,645,853],[192,238,1000],[160,523,675],[96,582,399],[119,462,636],[131,303,278],[309,713,601],[34,582,85],[57,397,343],[256,677,109],[510,719,897],[106,514,553],[22,90,740],[358,579,440],[56,76,317],[330,608,567],[446,624,832],[446,705,426],[23,431,6]]) == 14322