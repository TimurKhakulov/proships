from pikuli.uia import Desktop

# p = Desktop().find_all(ControlType="Pane", exact_level=1)
#
# for el in p:
#     print(el)

calc = Desktop().find_all(ClassName='CalcFrame')
print(calc)

# main_pane = calc.find(ProcessId=4428, exact_level=1)
# print(main_pane)
#
# for el in main_pane.find_all():
#     print(el)


# Нажать на кнопку 7
# b7 = Desktop().find(number='7')
# b7.reg().click()