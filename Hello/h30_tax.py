

def individual_tax_rat(raw_tax_incom):
    """
    计算个税税率和速算扣除数
    :param raw_tax_incom: 应纳税所得额
    :return:(税率,速算扣除数)
    """
    if raw_tax_incom < 0:
        return 0, 0
    if raw_tax_incom < 36000:
        return 0.03, 0
    elif raw_tax_incom < 144000:
        return 0.10, 2520
    elif raw_tax_incom < 300000:
        return 0.20, 16920
    elif raw_tax_incom < 420000:
        return 0.25, 31920
    elif raw_tax_incom < 660000:
        return 0.30, 52920
    elif raw_tax_incom < 960000:
        return 0.35, 85920
    else:
        return 0.45, 181920


def individual_income_tax(income=10000, social_base=10000, dis_tax=1000):
    """
    个税计算
    :param income:税前收入
    :param social_base:社保基数
            养老: 8%
            医疗:   2%
            失业:   6.6
            公积金: 5%
    :param dis_tax:每月扣除
    :return:按年度总的(税前,到手,个税)
    """
    social_insurance = social_base*0.08 + social_base*0.02 + 6.6 + social_base*0.05
    total_tax = 0
    for i in range(1, 13):
        raw_tax_income = income*i - 5000*i - dis_tax*i - social_insurance*i
        rate, quick_deduction = individual_tax_rat(raw_tax_income)
        tax = raw_tax_income*rate - quick_deduction - total_tax
        total_tax += tax
        print("%2d月： 到手:%d  税:%4d  三险一金:%d" % (i, income-tax-social_insurance, tax, social_insurance))

    fack_income = income*12
    real_income = income*12 - total_tax - social_insurance*12
    print("全年：")
    print("税前：%.2f" % fack_income)
    print("到手：%.2f" % real_income)
    print("个税：%.2f" % total_tax)
    print("税比：%.2f%%" % (total_tax/fack_income*100))
    return fack_income, real_income, total_tax


if __name__ == "__main__":
    individual_income_tax(12800, 12800, 0)

