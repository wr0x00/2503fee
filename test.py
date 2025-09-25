import pandas as pd
class xlsx(object):
    def __init__(self,filename):

        self.filename = filename
        
        self.df = pd.read_excel(self.filename)

    def show(self):
        print(self.df)
    '''显示表格内容'''

    def add_one(self,time:str,description:str,amount:str,fee:float,others:str=""):
        new_data = {'时间':time,'描述':description,'收支情况':amount,'余额':fee,'备注':others}
        new_data = pd.DataFrame(new_data,index=[0])
        self.df = self.df._append(new_data,ignore_index=True)
        self.df.to_excel(self.filename,index=False)
    '''
    添加一行数据到表尾
    time:时间
    description:描述
    amount:收支情况
    fee:余额
    others:备注
    '''
    def del_lastone(self):
        self.df.drop(self.df.index[-1], inplace=True)
    '''删除最后一行数据'''

a= xlsx('2503_fee.xlsx')
a.show()
a.del_lastone()
a.show()


    

