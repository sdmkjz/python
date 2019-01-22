#记录所有的名片字典
card_list=[]

def show_menu():
    '''显示菜单'''
    print('*'*50)
    print('欢迎使用【名片管理系统】v 1.0')
    print('')
    print('1.新增名片')
    print('2.显示全部')
    print('3.搜索名片')
    print('')
    print('0.退出系统')
    print('*'*50)

def new_card():
    '''新增名片'''
    print('-'*60)
    print('新增名片')
    #1.提示用户输入名片的详细信息
    name_str=input('请输入姓名：')
    phone_str=input('请输入电话：')
    qq_str=input('请输入QQ：')
    email_str=input('请输入邮箱：')
    #2.使用用户输入的信息建立一个名片字典
    card_dict={'name':name_str,
               'phone':phone_str,
               'qq':qq_str,
               'email':email_str}

    #3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    #4.提示用户添加成功
    print('添加%s的名片成功！'%name_str)

def show_all():
    '''显示所有名片'''
    print('-' * 60)
    print('显示所有名片')
    #判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list)==0:
        print('当前没有名片记录，请使用新增功能添加名片！')
        #return可以返回一个函数的执行结果
        #下方的代码不会被执行
        return
    # 打印表头
    for name in ['姓名', '电话', 'QQ', '邮箱']:
        print(name, end='\t\t')
    print('')
    # 分割线
    print('=' * 55)
    # 遍历名片列表 依次输出字典信息
    for card_dict in card_list:
        print('%s\t\t%s\t%s\t%s' % (card_dict['name'],
                                        card_dict['phone'],
                                        card_dict['qq'],
                                        card_dict['email']))


def search_card():
    '''
    搜索名片信息
    利用if进行判断，进行名片信息搜索
    :return:
    '''
    print('-' * 50)
    print('搜索名片')
    #1.提示用户输入要搜索的姓名
    find_name=input('请输入要查找的姓名：')
    #2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if card_dict['name']==find_name:
            print('姓名\t\t电话\t\t\tQQ\t\t\t邮箱')
            print('='*55)
            print('%s\t%s\t%s\t\t%s' % (card_dict['name'],
                                            card_dict['phone'],
                                            card_dict['qq'],
                                            card_dict['email']))
            #找到了以后针对单个名片进行操作
            deal_card(card_dict)

            break
    else:
        print('没有找到%s！'%find_name)

def deal_card(find_dict):
    '''
    查找到名片后，对名片的值进行修改或者删除
    :param find_dict:查找到的名片信息
    :return:
    '''
    action_str=input('请选择要执行的操作'
                     '[1]修改 [2]删除 [0]返回上级菜单:')
    while True:
        if action_str in ['1','2','0']:
            if action_str=='1':
                print('修改名片成功!')
                '''获取字典中的值，调用函数，给函数赋两个值，一个是字典的值，
                   一个是输入的提示信息
                '''
                find_dict['name']=input_card_info(find_dict['name'],'姓名:')
                find_dict['phone']=input_card_info(find_dict['phone'],'电话:')
                find_dict['qq']=input_card_info(find_dict['qq'],'QQ:')
                find_dict['email']=input_card_info(find_dict['email'],'邮箱:')
                break
            elif action_str=='2':
                card_list.remove(find_dict)
                print('删除名片成功!')
                break
            elif action_str=='0':
                break
        else:
            print('请输入正确的操作！')
            action_str = input('请选择要执行的操作'
                               '[1]修改 [2]删除 [0]返回上级菜单:')

def input_card_info(dict_value,tip_message):
    '''
        dict_value为字典原有的值
        tip_message为提示信息
       提示用户输入内容，然后将输入的内容做判断
       如果用户输入了内容，则返回结果，如果用户没有输入内容
       则返回字典中原有的值
    '''
    #1.提示用户输入内容
    result_str=input(tip_message)
    #2.针对用户的输入进行判断，如果用户输入了内容，则返回结果
    if len(result_str)>0:
        return result_str
    #3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value