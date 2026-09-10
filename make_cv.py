"""Generate a public CV without private phone or institutional identifiers."""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from content import EMAIL,PAPERS

ROOT=Path(__file__).resolve().parent
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name',fontName='Times-Roman',fontSize=25,leading=29,textColor=colors.HexColor('#183952'),spaceAfter=7))
styles.add(ParagraphStyle(name='Role',fontName='Helvetica',fontSize=10,leading=15,textColor=colors.HexColor('#405568'),spaceAfter=5))
styles.add(ParagraphStyle(name='Section',fontName='Times-Roman',fontSize=14,leading=18,textColor=colors.HexColor('#183952'),spaceBefore=11,spaceAfter=6))
styles.add(ParagraphStyle(name='Copy',fontName='Helvetica',fontSize=9.1,leading=12.5,textColor=colors.HexColor('#283c4b'),spaceAfter=7))
styles.add(ParagraphStyle(name='SmallCopy',parent=styles['Copy'],fontSize=8.2,leading=12))
story=[]
def p(text,style='Copy'):story.append(Paragraph(text,styles[style]))
def section(text):p(text,'Section')
p('Shurong Cao','Name')
p('PhD Student in Electronic Engineering | The Chinese University of Hong Kong','Role')
p(f'<link href="mailto:{EMAIL}" color="#315d7d">{EMAIL}</link> &nbsp; | &nbsp; <link href="https://caoshurong.github.io" color="#315d7d">caoshurong.github.io</link> &nbsp; | &nbsp; <link href="https://github.com/CAOShurong" color="#315d7d">GitHub: CAOShurong</link>','SmallCopy')
section('Education & Research Direction')
p('<b>The Chinese University of Hong Kong</b> — PhD in Electronic Engineering, 2026–present<br/>Supervisor: Prof. Ni Zhao. Exploring semiconductor devices and fabrication for BEOL-compatible and monolithic 3D electronics, including low-temperature processing, oxide and p-type semiconductors, and complementary integration.')
p('<b>Nanjing University</b> — B.Eng. in Integrated Circuit and System Design, 2022–2026<br/>School of Integrated Circuits, Suzhou Campus. Undergraduate thesis: <i>Parameter Optimization of Nano-TSVs for 3D Integrated Circuits.</i>')
section('Publications')
for paper in PAPERS:
    authors=paper['authors'].replace('<strong>','<b>').replace('</strong>','</b>')
    detail='DOI: 10.1109/ITC-Asia67627.2025.00016' if paper['id']=='falco-wafer' else 'arXiv:2409.06367; also included in the CVM 2026 conference program.'
    p(f'<b>{paper["title"]}</b><br/>{authors}<br/>{paper["venue"]}<br/>{detail}','SmallCopy')
section('Selected Research & Engineering')
for title,body in [
('Advanced packaging and nano-TSV modeling','Developed Python-assisted equivalent-material modeling workflows and thermo-mechanical simulations of 2.5D chip stacks using COMSOL and ANSYS at Nanjing University.'),
('Vacuum MOSFET sensing','Worked on COMSOL model development, device architecture refinement, simulation verification, and model integration in a national-level undergraduate innovation project. Co-inventor of granted Chinese patent CN120352074B (2025).'),
('Research exchange at HKUST (Guangzhou)','Modeled optical neuromemristors and nano-antennas, explored geometry optimization, and participated in device-characterization work.'),
('FPGA robotic system','Integrated PYNQ-Z2, Raspberry Pi 5, and STM32 hardware, with electronic-module assembly, wireless motion control, radar-based SLAM, and IMU drift compensation.')]:p(f'<b>{title}.</b> {body}')
section('Open-Source Engineering')
p('<b>BenchLineage maintainer.</b> Research provenance, calibration records, uncertainty budgets, evidence bundles, and ELN archive interoperability. Related contributions were integrated into the ELN format checks and eLabFTW importer tests.')
p('<b>Upstream contributor.</b> 37 merged pull requests across 22 external repositories, including Astropy, cibuildwheel, the ELN File Format, and GitHub MCP Server (GitHub snapshot: 11 September 2026).')
section('Recognition & Communication')
p('<b>National Second Prize, 2024.</b> FPGA Innovation Design Track Finals, 7th National College Embedded Chip and System Design Competition.<br/><b>People’s Scholarship, 2023 and 2024.</b> Nanjing University.<br/><b>Team leader and commencement speaker.</b> Hardware design program at St Catharine’s College, Cambridge.')
section('Technical Background')
p('Semiconductor-device modeling; COMSOL and ANSYS; Python, C, PyTorch, Git and Linux; Verilog, FPGA, STM32, ROS and embedded systems. Mandarin and English.')
def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(colors.HexColor('#dce3e7'));canvas.line(44,36,A4[0]-44,36);canvas.setFont('Helvetica',7.5);canvas.setFillColor(colors.HexColor('#63717b'));canvas.drawString(44,24,'Shurong Cao | Public CV | September 2026');canvas.drawRightString(A4[0]-44,24,str(doc.page));canvas.restoreState()
doc=SimpleDocTemplate(str(ROOT/'assets/Shurong-Cao-CV.pdf'),pagesize=A4,leftMargin=44,rightMargin=44,topMargin=37,bottomMargin=48,title='Shurong Cao — Curriculum Vitae',author='Shurong Cao',pageCompression=1)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('Generated public CV')
