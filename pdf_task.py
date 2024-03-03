from fpdf import FPDF

class MyPdf(FPDF):
    def add_border_to_page(self):
        self.rect(0, 0, self.w, self.h)

v_num = '- V000426'
voucher_number = 'PV-242200099'
height = 297
width = 210


from datetime import datetime
current_datetime = datetime.now()
current_date = current_datetime.date()
date_str = current_date.strftime("%Y-%m-%d")
current_time = current_datetime.time()
time_str = current_time.strftime("%H:%M:%S %p")

path = 'c:/Users/91939/OneDrive/Desktop/projects/project2'
pdf = FPDF(orientation='P', unit='mm', format='A4')
output_path = path + '/output.pdf'
pdf.add_page()

# Heading
pdf.set_fill_color(255, 255, 255)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', size=18, style='B')
pdf.set_xy(0, 10)
pdf.cell(0, 0, txt='PAYMENT VOUCHER', ln=1, align='C')

# logo heading
pdf.set_fill_color(255, 255, 255)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', size=12, style='B')
pdf.set_xy(10, 20)
pdf.cell(0, 0, txt='ALD MHC Mobility Services (Thailand) Co., Ltd.', ln=0, align='L')
pdf.cell(0, 0, txt=date_str, ln=1, align='R')


# logo
pdf.image(path + '/logo.jpg', x=5, y=23, w=15)
pdf.set_xy(0, 25)
pdf.cell(0, 0, txt=time_str, ln=1, align='R')

# pdf.set_xy(15, 55)
# pdf.set_font('Arial', size=10)

# # Calculate the widths for each component
# name_width = pdf.get_string_width('Name : Hino Motors Sales (Thailand) Ltd')
# v_num_width = pdf.get_string_width(v_num)
# voucher_number_width = pdf.get_string_width(voucher_number)
# bold_text_width = pdf.get_string_width('Voucher Number')

# # Total width of the line
# total_width = name_width + v_num_width + bold_text_width + voucher_number_width

# # Calculate the x-coordinate for the center alignment
# center_x = (210 - total_width) / 2  # Assuming the width of the page is 210 (A4 size)

# # Set x-coordinate for each component
# pdf.set_xy(15, 48)
# pdf.cell(name_width, 0, txt='Name : Hino Motors Sales (Thailand) Ltd', ln=0, align='L')

# pdf.set_xy(15 + name_width + 20, 48)
# pdf.cell(v_num_width, 0, txt=v_num, ln=0, align='C')

# # Set bold font before drawing the bold text
# pdf.set_font('Arial', size=11, style='B')
# pdf.set_xy(15 + name_width + v_num_width + 30, 48)
# pdf.cell(bold_text_width, 0, txt='Voucher Number:', ln=0, align='L')

# # Reset font style to normal
# pdf.set_font('Arial', size=10)

# pdf.set_xy(15 + name_width + v_num_width + bold_text_width + 50, 48)
# pdf.cell(voucher_number_width, 0, txt=voucher_number, ln=1, align='R')
pdf.set_xy(10, 45)
pdf.set_font('Arial', size=11)
w_txt_7 = pdf.get_string_width('Method of Payment : ')
pdf.cell(w_txt_7, 0, txt='Name : ', ln=0, align='R')
pdf.cell(40, 0, txt='Hino Motor Sales (Thailand) Ltd.', ln=0, align='L')
pdf.cell(60, 0, txt=v_num, ln=0, align='C')
pdf.set_font('Arial',size=11, style='B')
pdf.cell(20, 0, txt='Voucher Number: ', ln=0, align='R')
pdf.set_font('Arial', size=11)
pdf.cell(30, 0, txt=voucher_number, ln=0, align='R')


method_of_pay = 'DCR-BBL'
bank_account = 'Bank Account 1340744398'
voucher_date = '16-jan-2024'
pdf.set_xy(10, 52)
pdf.cell(w_txt_7, 0, txt='Method of Payment : ', ln=0, align='R')
pdf.cell(30, 0, txt=method_of_pay, ln=0, align='L')
pdf.cell(50, 0, txt=bank_account, ln=0, align='C')
pdf.set_font('Arial', style='B')
pdf.cell(39, 0, txt='Voucher Date:', ln=0, align='R')
pdf.set_font('Arial')
pdf.cell(30, 0, txt=voucher_date, ln=0, align='R')


journal_desc = 'Outgoing Payments - V000426 e-withholding Tax'
pdf.set_xy(10, 58)
pdf.cell(w_txt_7, 0, txt='Journal Description : ', ln=0, align='R')
pdf.cell(80, 0, txt=journal_desc, ln=0, align='L')
pdf.set_font('Arial', style='B')
pdf.cell(39, 0, txt='Invoice No.:', align='R')


# Account details
pdf.set_xy(5, 68)
pdf.set_font('Arial')
pdf.cell(15, 0, txt='Account', ln=0, align='L')
pdf.cell(60, 0, txt='Account Name', ln=0, align='C')
pdf.cell(10, 0, txt='Type', ln=0, align='C')
pdf.cell(15, 0, txt='Dept.', ln=0, align='C')
pdf.cell(20, 0, txt='Product', ln=0, align='C')
pdf.cell(40, 0, txt='Transaction Text', ln=0, align='C')
pdf.cell(20, 0, txt='Debit', ln=0, align='R')
pdf.cell(20, 0, txt='Credit', ln=0, align='R')

data = [{'Account': 212003, 
        'Account Name': 'Accounts Payable - Repair and Maintainance of Lease Vehicle', 
        'Dept': '',
        'Type': '',
        'Product': '',
        'Transaction Text': 'Outgoing Payments',
        'Debit': 420825, 
        'Credit': ''},
        {'Account': 111151, 
        'Account Name': 'Current Account - Bangkok Bank', 
        'Dept': '',
        'Type': '',
        'Product': '',
        'Transaction Text': 'Outgoing Payments',
        'Debit': '',
        'Credit': 420825}, 
        {'Account': 115404, 
        'Account Name': 'Duumy Account for e-Withholding Tax', 
        'Dept': '',
        'Type': '',
        'Product': '',
        'Transaction Text': 'Outgoing Payments',
        'Debit': '',
        'Credit': -3933},
        {'Account': 215307, 
        'Account Name': 'Withholding Tax Payable - e - Withholding Tax', 
        'Dept': '',
        'Type': '',
        'Product': '',
        'Transaction Text': 'Outgoing Payments',
        'Debit': '',
        'Credit': 3933}]
# y = 78
# for i in data:
#     pdf.set_xy(10, y)
#     pdf.cell(20, 0, txt=str(i['Account']), ln=0, align='L')
#     pdf.cell(60, 0, txt=i['Account Name'], ln=0, align='C')
#     pdf.cell(15, 0, txt=i['Type'], ln=0, align='C')
#     pdf.cell(15, 0, txt=i['Product'], ln=0, align='C')
#     pdf.cell(40, 0, txt=i['Transaction Text'], ln=0, align='C')
#     pdf.cell(20, 0, txt=str(i['Debit']), ln=0, align='C')
#     pdf.cell(20, 0, txt=str(i['Credit']), ln=1, align='C')
#     y += 10

y = 78

# Column widths
column_widths = [15, 60, 10, 15, 20, 40, 20, 20]  # Adjust these widths as needed
debit = 0
credit = 0
# Iterate over data
for i in data:
    # Set x and y position for the cells
    # pdf.set_xy(10, y)
    x = 5
    # Add data to cells
    # for j, key in data[0].keys():
    for j, key in enumerate(data[0]):
        if key == 'Debit' and i['Debit'] != "":
            debit += i['Debit']
        if key == 'Credit' and i['Credit'] != "":
            credit += i['Credit']

        text = str(i.get(key, ''))
        width = column_widths[j]
        if key == 'Account Name':
            pdf.set_xy(10 + column_widths[0], y-3)
            pdf.multi_cell(width, 5, txt=text, align='L')
        elif key == 'Account':
            pdf.set_xy(x, y)
            pdf.cell(width, 0, txt=text, ln=0, align='L')
        else:
            pdf.set_xy(x, y)
            pdf.cell(width, 0, txt=text, ln=0, align='R')
        x += width  
    # Move to next line after adding the row
    pdf.ln()
    
    # Update y-coordinate for the next row
    y += 12  # Adjust this value as needed to increase/decrease spacing between rows

pdf.set_xy(145, y)
pdf.cell(20, 0, txt='Total:', align='R', ln=0)
pdf.cell(20, 0, txt=str(debit), align='R', ln=0)
pdf.cell(20, 0, txt=str(credit), align='R', ln=1)


pdf.set_xy(5, y + 8)
pdf.set_font('Arial', style='BU', size=12)
pdf.cell(0, 0, txt='Payment Details', ln=0, align='L')

pdf.set_xy(5, y + 18)
pdf.set_font('Arial', style='', size=11)
pdf.cell(20, 0, txt='Date', align='L', ln=0)
pdf.cell(20, 0, txt='DueDate', align='L', ln=0)
pdf.cell(20, 0, txt='Bill No.', align='L', ln=0)
pdf.cell(20, 0, txt='Voucher', align='L', ln=0)
pdf.cell(20, 0, txt='Invoice', align='L', ln=0)
pdf.cell(35, 0, txt='Ammount Currency', align='L', ln=0)
pdf.cell(35, 0, txt='Ammount Settled Cur', align='L', ln=0)
pdf.cell(20, 0, txt='Amt Settled(THB)', align='L', ln=0)
pdf.output(output_path)

