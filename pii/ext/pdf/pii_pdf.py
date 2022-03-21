import os

from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

home = os.path.expanduser("~")

try:
    pdfmetrics.registerFont(TTFont("HanSans", f"{home}/.fonts/SourceHanSansCN-Normal.ttf"))
    pdfmetrics.registerFont(TTFont("HanSans-Bold", f"{home}/.fonts/SourceHanSansCN-Bold.ttf"))
    registerFontFamily("HanSans", normal="HanSans", bold="HanSans-Bold")
    FONT_NAME = "HanSans"
except:
    FONT_NAME = "Helvetica"


class MyCSS:
    h3 = ParagraphStyle(name="h3", fontName=FONT_NAME, fontSize=14, leading=21, alignment=1)
    p = ParagraphStyle(name="p", fontName=FONT_NAME, fontSize=12, leading=18, firstLineIndent=24)


"""
doc = SimpleDocTemplate("Hello.pdf")

p = PiiPdf()
doc.build([
    p.doH3("<b>水泵能源消耗简报</b>"),
    p.doH3("<b>2021.12.1 ~ 2021.12.31</b>"),
    p.doP("该月接入能耗管理系统水泵系统 xx 套，水泵 x 台。"),
    p.doP("本月最大总功率 xx kW，环比上月增加 xx %，平均功率 xx kW；环比上月增加 xx %。"),
    p.doP("功率消耗趋势图："),
    p.doLine(),
    p.doP("本月总能耗 xxx kWh，环比上月增加 xx %。"),
    p.doP("分水泵能耗统计："),
    p.doChart(list(range(15, 105, 20))),
    p.doP("其中能耗最高的水泵为：xxx， 环比上月增加 xxx kWh，xx %。"),
])
"""


class PiiPdf:
    @classmethod
    def doH3(cls, text: str):
        return Paragraph(text, MyCSS.h3)

    @classmethod
    def doP(cls, text: str):
        return Paragraph(text, MyCSS.p)

    @classmethod
    def doLine(cls):
        drawing = Drawing(500, 220)
        line = LinePlot()
        line.x = 50
        line.y = 50
        line.height = 125
        line.width = 300
        line.lines[0].strokeColor = colors.blue
        line.lines[1].strokeColor = colors.red
        line.lines[2].strokeColor = colors.green
        line.data = [((0, 50), (100, 100), (200, 200), (250, 210), (300, 300), (400, 800))]

        drawing.add(line)
        return drawing

    @classmethod
    def doChart(cls, data):
        drawing = Drawing(width=500, height=200)
        pie = Pie()
        pie.x = 150
        pie.y = 65
        pie.sideLabels = False
        pie.labels = [letter for letter in "abcdefg"]
        pie.data = data  # list(range(15, 105, 15))
        pie.slices.strokeWidth = 0.5

        drawing.add(pie)
        return drawing
