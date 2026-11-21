import tkinter as tk

def check(*args):
    global check_deduction
    check_deduction = [ deduction_clothing , deduction_reskill , deduction_book ]
    for var in check_deduction:
        try:
            if var.get() == '':
                deduction_msg_error.set('')
            elif int(var.get()) >= 0:
                deduction_msg_error.set('')
            else:
                raise ValueError
        except ValueError:
            deduction_msg_error.set('請輸入數字')
            return

def updata(*args):
    try:
        if revenus.get() == '':
            error_msg.set('請輸入薪資收入')
            error_Label.config(fg='black')

        elif int(revenus.get()) >= 0:
            error_msg.set('')
            
            # 扣繳稅額
            tax_withholding = int(int(revenus.get())*0.05)
            if int(revenus.get()) >= 90501 and tax_withholding >=2000:
                withholding.set(f'{tax_withholding:,}')
            else:
                withholding.set('0')

            # 特別扣除額
            special_deduction_math = min(218000,int(revenus.get()))
            special_deduction.set(f'{special_deduction_math:,}')
            
            # 必要費用
            check()
            deduction_list = 0
            for var in check_deduction:
                try:
                    deduction_math = min(int(int(revenus.get())*0.03),int(var.get()))
                except ValueError:
                    deduction_math = 0
                deduction_list += deduction_math    
            msg_deduction_list.set(f'薪資必要費用扣抵額：{deduction_list:,}')

            # 扣除額
            if special_deduction_math >= deduction_list:
                deduction.set(special_deduction_math)
                deduction_msg.set('採用薪資所得特別扣除額較有利')
            else:
                deduction.set(deduction_list)
                deduction_msg.set('採用薪資必要費用(核實減除)較有利')

            # 薪資所得
            income.set(f'{int(revenus.get())-int(deduction.get()):,}')

        else:
            raise ValueError
        
    except ValueError:
        withholding.set('')
        special_deduction.set('')
        deduction.set('')
        income.set('')
        error_msg.set('薪資所得輸入錯誤!')
        error_Label.config(fg='red')

root = tk.Tk()
root.title('薪資所得計算器')
root.geometry('400x450')

revenus = tk.StringVar()
withholding = tk.StringVar()
special_deduction = tk.StringVar()
deduction_clothing = tk.StringVar()
deduction_reskill = tk.StringVar()
deduction_book = tk.StringVar()
income = tk.StringVar()

error_msg = tk.StringVar()
error_Label = tk.Label(root,textvariable=error_msg)
deduction = tk.StringVar()
deduction_msg = tk.StringVar()
deduction_msg_error = tk.StringVar()
deduction_Label = tk.Label(root,textvariable=deduction_msg)
msg_deduction_list = tk.StringVar()

revenus.set('0')
error_msg.set('請輸入薪資收入')
special_deduction.set('')
deduction_msg.set('')
deduction_msg_error.set('')
deduction_clothing.set('')
deduction_reskill.set('')
deduction_book.set('')
msg_deduction_list.set('薪資必要費用扣抵額：0')
income.set('')

tk.Label(root,text='薪資收入').pack()
tk.Entry(root,textvariable=revenus).pack()
error_Label.pack()

tk.Label(root,text='扣繳稅額').pack()
tk.Entry(root,textvariable=withholding,state='readonly').pack()

tk.Label(root,text='薪資所得特別扣除額').pack()
tk.Entry(root,textvariable=special_deduction,state='readonly').pack()

tk.Label(root,text='\n職業專用服裝費').pack()
tk.Entry(root,textvariable=deduction_clothing).pack()

tk.Label(root,text='進修訓練費').pack()
tk.Entry(root,textvariable=deduction_reskill).pack()

tk.Label(root,text='職業上工具支出').pack()
tk.Entry(root,textvariable=deduction_book).pack()
tk.Label(root,textvariable=msg_deduction_list).pack()
tk.Label(root,textvariable=deduction_msg_error,fg='red').pack()

tk.Label(root,text='薪資扣除額').pack()
tk.Entry(root,textvariable=deduction,state='readonly').pack()
deduction_Label.pack()

tk.Label(root,text='薪資所得').pack()
tk.Entry(root,textvariable=income,state='readonly').pack()

revenus.trace_add('write',updata)
deduction_clothing.trace_add('write',updata)
deduction_reskill.trace_add('write',updata)
deduction_book.trace_add('write',updata)

root.mainloop()
