import openpyxl
from openpyxl import Workbook

path = r'D:/02Project/03Szorb/2017扬子石化/02.整理资料/yz-szorb闭锁料斗取数/'

tag_list = ['aAI_2401', 'aAI_2402', 'AI1001.PV', 'AI5201.PV', 'aLI_2401', 'aLI_2501', 'aPDI_2301', 'aPDI_2403', 'aPDI_2405', 'aPDI_2406', 'aPDI_2407', 'aPDI_2408', 'aPDI_2409', 'aPDI_2501', 'aPDI_2703', 'aPI_2402', 'aPI_2403', 'aPI_2405', 'aPI_2406', 'aPI_2407', 'aPI_2408', 'aPI_3701', 'aPI_3702', 'FI3501.PV', 'FIC1101.PV', 'FIC1102.PV', 'FIC2432.SP', 'FIC2801.PV', 'FIC3101.PV', 'FIC3103.PV', 'fTH_2701', 'LI2104', 'LI2107', 'LI2604', 'PDI2102', 'PDI2104.PV', 'PDI2301.PV', 'PDI2501.PV', 'PDI2604.PV', 'PDI2704.PV', 'PDI2801.PV', 'PI2101.PV', 'PI2801.PV', 'PIC2601.PV', 'PIC3101.PV', 'PI_2301', 'rFI2431', 'rFI2432', 'rFI2433', 'rPDT2409', 'rPT2401', 'rPT2501', 'rPT2801', 'rTE2401', 'TI2003.PV', 'TI2103.PV', 'TI2104.PV', 'TI2601', 'TI3101.PV', 'TIC1606.PV', 'TIC2607.PV']
# file_list = ['time']
# file_list.extend(tag_list)
# print(file_list)
i= 0
for tag in tag_list:
    excel_file = path + tag + '.xlsx'
    wb = openpyxl.load_workbook(filename=excel_file)
    sheet = wb['Sheet1']
    for j in range(1,5):
        sheet['A'+str(j)] = 0
    wb.close()
    i += 1
    if i > 1:
        break
print('\n文件转换完毕')
