'''
澡卡缴费计算
'''
zaoka_list = []  # 初始化空列表
def show_menu():
    '''欢迎界面'''
    print('*'*50)
    print('欢迎使用澡卡缴费计算系统  V1.0')
    print('')
    print('1.缴费计算')
    print('')
    print('2.缴费人员查询')
    print('')
    print('3.缴费人员信息')
    print('')
    print('0.退出系统')
    print('*'*50)

def id_suan(name):
    '''计算程序
       先进行身份验证判断，然后再进行计算
       最后保存到字典里，赋值到列表中
    '''
    name_str = input('请输入您的姓名:')
    if name_str in name:
        print('身份验证成功，请继续输入！')
    else:
        print('身份验证失败！')
        exit()
    c = input('请输入每周洗头的次数:')
    d = input('请输入每周洗澡的次数:')
    #澡卡计算过程
    a = 0.5  # 洗漱一次的花费
    zao = 1.5  # 洗澡一次的花费
    ci = int(c)
    num1 = (a * ci) * 20  # 用洗漱一次的花费*每周使用的次数，再*本学期周数
    xi = int(d)
    num2 = (zao * xi) * 20  # 洗澡钱数统计
    zaoka_dict={'name':name_str,
                'tou':c,
                'zao':d,
                'money':num1+num2}
    zaoka_list.append(zaoka_dict)
    print()
    print('%s 同学，你的充值金额合计为%d!' %(name_str,(num1 + num2)))
    print('-----统计原理为-----')
    print('洗头按照每次0.5元，洗澡按照每次1.5元')

def search_ren():
    '''
        缴费人员查询
        输入要查询的姓名，然后使用for循环遍历列表值
        使用if进行比对，搜索到正确的进行输出，然后跳出循环
        如果搜索到不正确的，将提示用户
    :return:
    '''
    print('*'*50)
    print('缴费人员查询')
    find_name=input('请输入要查询的姓名:')
    #使用if语句判断是否有缴费计算
    for zaoka_dict in zaoka_list:
        if zaoka_dict['name']==find_name:
            print('姓名\t\t洗头次数\t洗澡次数\t缴费金额')
            print('%s\t\t%s\t\t%s\t\t%s'%(zaoka_dict['name'],zaoka_dict['tou'],
                                          zaoka_dict['zao'],zaoka_dict['money']))
            break
    else:
         print('请检查输入是否正确，没有搜索到%s！'%find_name)
def show_all():
    '''
        缴费人员信息查询(查询所有人员信息)
        使用if判断列表是否为空
        使用print打印表头
        然后使用for循环进行遍历
    :return:
    '''
    print('*'*50)
    print('缴费人员信息')
    if len(zaoka_list)==0:
        print('澡卡信息为空，请先进行计算！')
        return
    else:
        print('姓名\t\t洗头次数\t洗澡次数\t缴费金额')
    for zaoka_dict in zaoka_list:
        print('%s\t\t%s\t\t%s\t\t%s' % (zaoka_dict['name'], zaoka_dict['tou'],
                                          zaoka_dict['zao'], zaoka_dict['money']))