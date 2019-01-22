import cards_tools
#无限循环，由用户决定什么时候退出循环(输入0)
if __name__ == "__main__": #定义主程序入口
    while True:
        '''
        程序执行原理：用户输入值，程序判断用户输入的值，根据用户不同的输入
        来调用不同的方法
        '''
        #显示功能菜单
        cards_tools.show_menu()
        action_str=input('请选择希望执行的操作:')
        print('您选择的操作是【%s】'%action_str)
        #如果用户输入1,2,3 针对名片的操作
        if action_str in ['1','2','3']:
            #新增名片
            if action_str=='1':
                cards_tools.new_card()
            #显示全部
            if action_str=='2':
                cards_tools.show_all()
            #查询名片
            if action_str=='3':
                cards_tools.search_card()
            #如果在开发程序时，不希望立刻编写分支内部的代码
            #可以使用pass关键字，表示一个占位符，能保证程序的代码结构正确！
            #程序运行时，pass关键字不会执行任何的操作
            pass
        #0 退出系统
        elif action_str=='0':
            print('欢迎再次使用【名片管理系统】')
            break
        #其他内容输入错误，需要提示用户
        else:
            print('您输入有误，请重新输入')