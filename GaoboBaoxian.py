#coding=utf-8
__author__ = 'Leon'

import math
def fnCaculateMoney(fBasicMoney,m,n,fRate):
    #n 收益年限，如：30年后的收益
    #m 缴费年限，如：共缴纳10年
    #fRate 收益率
    iFinalMoney = 0
    for i in range(0,min(m,n),1):
        iFinalMoney = iFinalMoney+math.pow((100+fRate)/100,n-i)
        #print iFinalMoney

    print '每年缴纳金额:' + str(fBasicMoney)
    print '共缴纳多少年:' + str(m)
    print '计算收益的年限:' + str(n)
    print '收益率:' + str(fRate)
    print '本金总支出:' + str(min(m,n)*fBasicMoney)
    print '刨除本金后净收益:' + '%.2f'%(iFinalMoney*fBasicMoney - min(m,n)*fBasicMoney)


    return iFinalMoney*fBasicMoney


def main():

    fBasicMoney = 56400
    fRate = 4.0
    iAllYears = 10;

    print '###############'
    print '收益总金额：%.2f'%(fnCaculateMoney(fBasicMoney,iAllYears,5,fRate))
    print '###############'
    print '收益总金额：%.2f'%(fnCaculateMoney(fBasicMoney,iAllYears,10,fRate))
    print '###############'
    print '收益总金额：%.2f'%(fnCaculateMoney(fBasicMoney,iAllYears,20,fRate))




if __name__ == '__main__':
    main()
