import zaoka_function
if __name__=='__main__':#定义主程序入口
    name_str=['王五','李四','测试','此处','随意','更改','计算','缴费']
    while True:
        #显示菜单
        zaoka_function.show_menu()
        action_str=input('请输入您要进行的操作:')
        print('您选择的操作是【%s】'%action_str)
        if action_str in ['1','2','3','0']:
            if action_str=='1':
                #缴费计算
                zaoka_function.id_suan(name_str)
            if action_str=='2':
                #缴费人员查询
                zaoka_function.search_ren()
            if action_str=='3':
                zaoka_function.show_all()
            if action_str=='0':
                print('欢迎再次使用澡卡缴费计算系统！')
                break
        else:
            print('您的输入有误，请重新输入！')