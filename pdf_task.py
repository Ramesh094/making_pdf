from fpdf import FPDF

v_num = 'v000426'
voucher_number = 'PV-242200099'

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
pdf.set_xy(10, 20)
pdf.cell(0, 0, txt='PAYMENT VOUCHER', ln=1, align='C', fill=True)

# logo heading
pdf.set_fill_color(255, 255, 255)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', size=12, style='B')
pdf.set_xy(5, 30)
pdf.cell(0, 0, txt='ALD MHC Mobility Services (Thailand) Co., Ltd.', ln=0, align='L', fill=True)
pdf.cell(0, 0, txt=date_str, ln=1, align='R', fill=True)


# logo
pdf.image(path + '/logo.jpg', x=5, y=33, w=15)
pdf.set_xy(0, 35)
pdf.cell(0, 0, txt=time_str, ln=1, align='R', fill=True)

pdf.set_xy(15, 55)
pdf.set_font('Arial', size=10)

# Calculate the widths for each component
name_width = pdf.get_string_width('Name : Hino Motors Sales (Thailand) Ltd')
v_num_width = pdf.get_string_width(v_num)
voucher_number_width = pdf.get_string_width(voucher_number)
bold_text_width = pdf.get_string_width('Voucher Number')

# Total width of the line
total_width = name_width + v_num_width + bold_text_width + voucher_number_width

# Calculate the x-coordinate for the center alignment
center_x = (210 - total_width) / 2  # Assuming the width of the page is 210 (A4 size)

# Set x-coordinate for each component
pdf.set_xy(15, 48)
pdf.cell(name_width, 0, txt='Name : Hino Motors Sales (Thailand) Ltd', ln=0, align='L', fill=True)

pdf.set_xy(15 + name_width + 20, 48)
pdf.cell(v_num_width, 0, txt=v_num, ln=0, align='C', fill=True)

# Set bold font before drawing the bold text
pdf.set_font('Arial', size=11, style='B')
pdf.set_xy(15 + name_width + v_num_width + 30, 48)
pdf.cell(bold_text_width, 0, txt='Voucher Number:', ln=0, align='L', fill=True)

# Reset font style to normal
pdf.set_font('Arial', size=10)

pdf.set_xy(15 + name_width + v_num_width + bold_text_width + 50, 48)
pdf.cell(voucher_number_width, 0, txt=voucher_number, ln=1, align='R', fill=True)



pdf.output(output_path)

