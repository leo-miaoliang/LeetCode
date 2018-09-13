class Solution(object):
    def lenLongestFibSubseqTLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[-1 for i in xrange(n)] for j in xrange(n)]
        s = {}
        for j in xrange(n - 1, -1, -1):
            b = A[j]
            for i in xrange(j - 1, -1, -1):
                a = A[i]
                c = a + b
                if c in s:
                    # print "{} + {} = {} in s at {}, dp[{}][{}] = {}".format(a, b, c, s[c], i, j, s[c])
                    dp[i][j] = s[c]
            s[b] = j
            # print "Insert {}".format(b)
        # print "++", dp[0][1]
        # print "++", dp[1][2]
        ans = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                ii = i
                jj = j
                ll = 0
                # print "== start {} {}".format(ii, jj)
                while dp[ii][jj] != -1:
                    t = dp[ii][jj]
                    ii = jj
                    jj = t
                    ll += 1
                    # print "== now {} {}".format(ii, jj)
                ans = max(ans, ll)
        if ans == 0:
            return ans
        else:
            return ans + 2


    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[(-1, 0) for i in xrange(n)] for j in xrange(n)]
        s = {}
        for j in xrange(n - 1, -1, -1):
            b = A[j]
            for i in xrange(j - 1, -1, -1):
                a = A[i]
                c = a + b
                if c in s:
                    dp[i][j] = s[c], dp[j][s[c]][1] + 1
            s[b] = j

        ans = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                ans = max(ans, dp[i][j][1])
        if ans == 0:
            return ans
        else:
            return ans + 2

# sln = Solution()
# print sln.lenLongestFibSubseq([1,2]) # 0
# print sln.lenLongestFibSubseq([1,2,3]) # 3
# print sln.lenLongestFibSubseq([1,2,3,5]) # 4
# print sln.lenLongestFibSubseq([1,2,3,4,5,6,7,8]) # 5
# print sln.lenLongestFibSubseq([1,3,7,11,12,14,18]) # 3
print sln.lenLongestFibSubseq([4,6,8,10,25,32,35,41,48,52,53,60,66,72,80,84,88,91,95,96,97,98,99,102,129,132,138,149,151,152,155,179,200,203,210,216,226,232,235,245,250,270,302,348,354,355,373,384,394,405,449,502,557,558,564,581,608,616,639,655,719,804,906,911,912,936,981,1000,1033,1060,1168,1306,1464,1468,1476,1589,1616,1672,1715,1887,2110,2370,2388,2570,2616,2705,2775,3055,3416,3834,3864,4159,4232,4377,4490,4942,5526,6204,6252,6729,6848,7082,7265,7997,8942,10038,10116,10888,11080,11459,11755,12939,16242,16368,17617,17928,18541,19020,20936,26280,26484,28505,29008,30000,30775,33875,42522,42852,46122,46936,49795,54811,68802,69336,74627,75944,80570,88686,112188,120749,122880,143497,181524,195376,198824,232183,293712,316125,321704,375680,475236,511501,520528,607863,768948,827626,842232,983543,1244184,1339127,1362760,1591406,2013132,2166753,2204992,2574949,3257316,3505880,3567752,4166355,4800404,5270448,5672633,5772744,6741304,7299063,8527764,9100163,9178513,9340496,10907659,11138789,11327609,13477294,13798212,15040181,15149078,15261924,15323833,16867589,17410438,17648963,18385969,19958649,21543311,22887650,23649965,26467867,26543337,27259692,27330750,28530282,29037113,30066010,33798768,34395757,35725831,37504825,41969915,42018564,44391387,44404575,45455592,46654192,50731454,50865572,54395791,54437496,55810259,58302572,59440987,60711487,61072024,65078581,65985311,67370856,67750874,69161512,70911615,72549611,73314198,73787981,75282450,79479140,79918445,81909737,82269553,83729078,83766649,85759160,87258785,87963227,88124553,91717991,96260891,97270103,97480538,97580271,97904042,98742073,98878101,102666974,102741463,103691671,104832402,109169122,110927182,112512866,115080235,116943653,117235239,117760216,118017527,118297384,118714748,118790606,119218785,120806539,121433749,124317236,124771538,128378885,128599251,129105071,129625626,130918156,131212488,133001893,134669557,135124244,136772396,142517347,144859662,146237839,146542001,146926536,150404283,150916806,151862190,153485432,155832601,158417907,159253707,159812008,160268461,160753590,160887305,161450507,162448183,163554024,164028673,165275244,165476351,165622031,169240984,169517421,170199562,170704489,171294766,171551924,172692939,172695420,173416477,173666977,175847138,176078812,177751788,178483707,178491131,180739367,180777827,182454194,182983382,183530436,190411978,191130573,191611328,191884595,196166745,196210035,196564145,200459127,201312573,203779405,205176046,205711341,206685559,206726241,207443248,207697821,209927165,210204714,210320485,210736494,210952949,211573378,212740220,213472195,215254349,216135838,216800397,218197824,218496062,220035577,220790805,224703722,224809215,224896395,225116763,227428599,227758738,228750058,228986293,233195485,233715294,234011673,234406451,235039818,235240014,236184340,237343844,238678977,242207557,243116208,244121334,244529507,245951789,246686880,248110238,248625387,249046530,249736144,250299194,252546104,253692740,254921069,255618001,255946038,258885156,259488813,260052136,262303187,262499188,264469273,267298837,267337671,268140560,268509252,269256744,269294076,272129223,272574277,273192828,275314647,275900227,276377422,278129691,278380897,278779466,279135025,279232518,279526827,280218827,280370720,282000408,285126290,286538157,287483322,288040573,292736236,292823702,296156047,297338228,298074868,303386115,303918991,304735791,305505311,306319462,309470524,309720240,309874897,310432369,310861584,311612236,315320772,317743590,320452467,322188832,322199018,323032337,325586691,326664187,331252731,332248911,334323274,334880541,336222352,337626212,338932326,339476642,341765077,342123517,343431954,344428293,345049707,346028709,348104648,350334156,352872340,352996465,353733278,355628399,356165993,356174582,358544966,361762454,365960807,369049595,370730723,374980120,378563921,382033834,382504514,382622079,383637428,384991564,385093946,386455207,387068389,389212742,390349622,390953824,391153221,391742131,392685885,393165821,393441827,394289999,394295957,394302842,395554769,395935333,396274252,396537087,400723689,401657143,402417525,403199031,404978496,405225432,405782514,408170872,408193404,408525576,410484555,412339114,413804997,414966034,415702044,418427452,422135420,423623842,427957023,427982003,428707804,428719346,428738284,428770355,428801319,428865254,430034100,432477408,437534712,438116952,438823203,441741551,441887377,443562374,443720685,444741343,444882351,445926727,446493142,447507490,448661066,448704720,450001237,458617544,459034493,459970640,461911263,466694778,467146270,467931837,468611695,468932608,470683899,475298539,475305235,477714384,478508293,478509775,480560793,480781663,482550331,483417018,484159983,484736963,485261137,488955991,489378772,490172047,490935183,495537732,497780315,498133769,502095129,502099701,503116131,503764222,504719738,506569321,507041664,508172640,509404505,510676131,511473682,511839543,512597312,513436011,515470276,515774875,516064973,518349323,518833532,519569264,519678426,522507209,523092948,523354913,523802760,524193202,526697728,532819221,533077598,535298084,535878450,537447983,538057235,539314888,541938706,543839995,544644487,546305749,547955583,548498125,551170705,551324502,552134774,552875715,554679725,555353306,557687823,558343471,558986699,559230512,559323301,559938585,560210891,563226027,563507307,563909638,564288467,564452443,566969750,568506211,573273713,573293349,574111283,574582812,576065254,576812058,577354774,581867043,583274433,583585557,586271907,588011379,588399212,588784161,590350897,590781481,592684605,593221065,595823719,597359785,598221415,599041131,602744039,603394282,606285240,606837133,606902132,607750377,609004762,609513414,610997700,611930801,613092486,615763215,616246550,619321332,619366899,619781817,620564307,621018743,621696521,622204999,623017567,624224960,625169364,626017942,627837229,628381488,628801581,629355354,629746210,630010201,630224203,631466298,632174174,635066467,635842540,636241889,636349787,636734664,637158089,638909369,638920881,638978098,639710792,640223363,640597826,641804285,644099534,644246516,644252854,645567301,646767031,647352418,648184791,649141154,652479512,652643571,654202248,656288667,656791472,658844147,659005922,659018171,659328019,659410733,660353767,662846350,663035685,664349572,665243624,665630893,667609141,668075001,669658188,669853082,670926647,671518838,672590057,673448382,675409010,677529647,682000641,682298607,685174459,685211992,687089529,687963712,689606726,689986879,692962235,694932052,694953874,695415821,696066424,696205111,698209660,698578810,698754472,699458209,700053058,701874692,705450532,705678387,707723481,707724103,708979402,709444593,709602353,711746632,711807371,712058280,715338240,715865570,716971916,720465470,724451879,725748858,726019174,726774142,728782969,729145567,729849464,729901137,730364098,730900623,732540837,732680160,734125356,735806843,737894147,738395274,738730395,739960140,740500748,743918447,745789040,747005335,747407724,748440818,749072636,749672950,750294272,756158823,756607891,757160651,757376462,757453926,757623300,758181533,758684378,759811013,762194758,762328733,762371135,762660015,764785932,767688694,768277733,768300140,768738685,769122914,769900343,771122534,773428875,774307060,774656795,774873614,775462463,775500760,775521554,776137808,779041380,781826319,783101346,784031542,785440894,786090074,786810925,788505257,788794038,790209347,790224132,792033511,792912910,793304089,793888566,794508926,796871223,797697652,798010732,798982932,799618476,800503895,800780021,801020721,801184593,802063759,802579700,803731973,804358989,805319102,805419344,806176494,808159462,808835191,809662023,810812299,811042789,812789401,814146275,817042932,817213981,817576495,818032332,818414608,819313435,819431359,820029265,820526089,820883336,821751196,822322258,823163420,824568732,825062717,826001700,826609848,827140635,828721858,828840727,829633482,830324289,830941554,832188890,832624466,833695725,837148579,839608845,839822265,841747069,842086362,844188596,849562324,850094913,850985067,852895013,853110529,855853282,859692693,861345992,861551975,863069758,863303092,864241569,867682266,870833029,871407612,871591557,871799113,873360562,882171498,882272160,883992445,885751157,886569216,887014525,887722138,888124241,889159483,889612903,889625378,891248425,892942463,895181068,898798302,899335843,901424631,906096732,906184588,908123669,908779798,909128669,909455698,910542681,913876383,916211361,917239717,918429007,918443330,919692289,923902859,923954877,924987600,926209334,926212160,927674602,928604677,929149875,929501783,929900504,932798449,933476010,934474781,934963565,935934137,937259497,938552445,939986753,941569521,942276119,943384033,945888523,950410096,954865788,955573763,958118550,959943438,960015269,960772049,961482853,962713789,964842667,965101620,965621934,965824091,966530963,968038239,970133147,970616596,972787629,972878934,973340287,973486974,975990610,976484621,978434291,980535199,980833321,981360850,982686980,984746913,988793122,990828691,992047866,993644699,995973354,997809191,998408230])