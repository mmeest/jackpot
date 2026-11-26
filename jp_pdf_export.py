"""
Genereeritud lotonumbrite eksport PDF-faili.

Appi sai võetud juhend: https://www.youtube.com/watch?v=0SQb__Zrg5Y
Create PDFs with Pure Python - Perfect For Document Automation

Iga faili nimesse lisatakse ka loomise aeg

PDF formaadi genereerimiseks kasutame reportlab
"""
import time
from pathlib import Path

from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Image, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

""" konstandid """
JUUR = Path(__file__).parent
PILDID = JUUR / "pic"
VÄLJUND = JUUR / "tulemused"

""" värvid """
TUMESININE = colors.HexColor("#163d6d")
TUMELILLA = colors.HexColor("#281c5e")
TEKST = colors.HexColor("#1a1a1a")
VALGE = colors.HexColor("#ffffff")
HELESININE = colors.HexColor("#b9f3f7")
KOLLANE = colors.HexColor("#fcf84e")
HELEHALL = colors.HexColor("#eec1c9")
TUMEHALL = colors.HexColor("#c9707f")
TULP = colors.HexColor("#2a7de1")

""" Bingo tabeli värvid """
BINGO_TAUST = [  
    [TUMEHALL, HELEHALL, HELEHALL, HELEHALL, TUMEHALL],
    [HELEHALL, TUMEHALL, HELEHALL, TUMEHALL, HELEHALL],
    [HELEHALL, HELEHALL, TUMEHALL, HELEHALL, HELEHALL],
    [HELEHALL, TUMEHALL, HELEHALL, TUMEHALL, HELEHALL],
    [TUMEHALL, HELEHALL, HELEHALL, HELEHALL, TUMEHALL],
]

STIILID = getSampleStyleSheet()
SILT = ParagraphStyle(
    "silt",
    parent=STIILID["Normal"],
    alignment=TA_CENTER,
    textColor=TUMESININE,
    fontName="Helvetica-Bold",
    fontSize=11,
    spaceBefore=6,
    spaceAfter=4,
)
PEALKIRI = ParagraphStyle(
    "pealkiri",
    parent=STIILID["Heading2"],
    alignment=TA_CENTER,
    textColor=TUMESININE,
    fontName="Helvetica-Bold",
    fontSize=14,
    spaceBefore=8,
    spaceAfter=2,
)
SELGITUS = ParagraphStyle(
    "selgitus",
    parent=STIILID["Normal"],
    alignment=TA_CENTER,
    textColor=TEKST,
    fontName="Helvetica",
    fontSize=9,
    leading=12,
    spaceAfter=4,
)

""" ekspordi meetod """
def ekspordi_pdf(viking_põhi, viking_lisa, euro_põhi, euro_lisa, bingo, sagedused=None):
    VÄLJUND.mkdir(parents=True, exist_ok=True)
    aeg = time.strftime("%Y-%m-%d_%H-%M-%S")
    fail = VÄLJUND / f"tulemused_{aeg}.pdf"			# <-- failinimes on loomise aeg
    nr = 2
    while fail.exists():
        fail = VÄLJUND / f"tulemused_{aeg}_{nr}.pdf"
        nr += 1
    sisu_laius = A4[0] - 72
    doc = SimpleDocTemplate(
        str(fail),
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=28,
    )
    sisu = [pilt("lotogen.png", 240), Spacer(1, 8)]		# <-- päisesse jääb ainult LotoGeni logo ja 
    sisu.append(mängu_plokk([("Vikingloto põhinumbrid", viking_põhi, VALGE), ("Lisanumber", viking_lisa, HELESININE),]))
    sisu.append(Spacer(1, 8))
    sisu.append(mängu_plokk([("Eurojackpot põhinumbrid", euro_põhi, VALGE), ("Lisanumbrid", euro_lisa, KOLLANE),]))
    sisu.append(Spacer(1, 6))
    sisu.extend(bingo_plokk(bingo))
    if _sagedus_olemas(sagedused):		# graafik tuleb ainult siis, kui scraper on juba käinud
        sisu.append(Paragraph("Numbrite esinemissagedus", PEALKIRI))
        sisu.append(Paragraph("Kõigi eelnevate loosimiste kogutud numbrite sagedus. Tulba kõrgus näitab, mitu korda number esines.", SELGITUS,))
        sisu.extend(sageduse_joonised(list(sagedused), sisu_laius))
    doc.build(sisu)
    return fail

""" piltide lisamine """
def pilt(nimi, laius):
    tee = str(PILDID / nimi)
    laius_px, kõrgus_px = ImageReader(tee).getSize()
    return Image(tee, width=laius, height=laius * kõrgus_px / laius_px, hAlign="CENTER")

""" Vikingi ja Eurojackpoti numbrite tabel """
def mängu_plokk(read):
    #plokk = [pilt("vl_logo.png", 210)]
    #plokk = [pilt("ej_logo.jpg", 230)]
    plokk = []
    for silt, numbrid, taust in read:
        tabel = numbri_tabel(numbrid, taust)
        if tabel is None:		# tühja numbririda PDF-i ei panda
            continue
        plokk.append(Paragraph(silt, SILT))
        plokk.append(tabel)
    return KeepTogether(plokk)

""" Bingo tabel """
def numbri_tabel(numbrid, taust):
    lahtrid = [str(n) for n in numbrid if str(n).strip()]
    if not lahtrid:
        return None
    tabel = Table([lahtrid], colWidths=[32] * len(lahtrid), rowHeights=[26])
    tabel.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, -1), taust),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEKST),
        ("GRID", (0, 0), (-1, -1), 0.6, TUMELILLA),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    tabel.hAlign = "CENTER"
    return tabel


def bingo_plokk(numbrid):
    lahtrid = [str(n).strip() for n in list(numbrid)[:25]]
    lahtrid += [""] * (25 - len(lahtrid))
    #plokk = [pilt("bingo.jpg", 210)]
    plokk = []
    if not any(lahtrid):
        return plokk
    read = [["B", "I", "N", "G", "O"]]		# <-- Bingoloto tabeli päis
    for rida in range(5):
        read.append([lahtrid[veerg * 5 + rida] for veerg in range(5)])
    tabel = Table(read, colWidths=[36] * 5, rowHeights=[24] * 6)
    käsud = [
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("FONTSIZE", (0, 1), (-1, -1), 11),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (-1, 0), TUMELILLA),
        ("TEXTCOLOR", (0, 0), (-1, 0), VALGE),
        ("TEXTCOLOR", (0, 1), (-1, -1), TEKST),
        ("GRID", (0, 0), (-1, -1), 0.6, TUMELILLA),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]
    for rida in range(5):
        for veerg in range(5):
            käsud.append(("BACKGROUND", (veerg, rida + 1), (veerg, rida + 1), BINGO_TAUST[rida][veerg]))
    tabel.setStyle(TableStyle(käsud))
    tabel.hAlign = "CENTER"
    plokk.append(Spacer(1, 6))
    plokk.append(tabel)
    return plokk

""" kontrollime kas andmed on olemas ja kas neid on täpselt 75 tk """
def _sagedus_olemas(sagedused):
    return isinstance(sagedused, (list, tuple)) and len(sagedused) == 75

""" tulpdiagrammi välja arvutamine """
def sageduse_joonised(sagedused, laius):
    maks = max(sagedused)
    if maks <= 0:
        ülempiir, samm = 1, 1
    else:
        samm = 1 if maks <= 10 else max(1, (maks + 4) // 5)
        ülempiir = ((maks + samm - 1) // samm) * samm
        if ülempiir <= maks:
            ülempiir += samm
    return [KeepTogether([tulpdiagramm(sagedused, 1, ülempiir, samm, laius),])]

"""
tulpdiagramm enimesinenud numbrite kohta viimastest loosimistest
https://docs.reportlab.com/reportlab/userguide/ch11_graphics/
https://www.reportlab.com/docs/reportlab-userguide.pdf
"""
def tulpdiagramm(väärtused, esimene_number, ülempiir, samm, laius):
    joonis = Drawing(laius, 132)
    tulbad = VerticalBarChart()
    tulbad.x = 32
    tulbad.y = 20
    tulbad.height = 100
    tulbad.width = laius - 44
    tulbad.data = [list(väärtused)]
    """ silt iga viienda numbri juurde """
    tulbad.categoryAxis.categoryNames = [str(n) if n == esimene_number or (n - esimene_number) % 5 == 4 else ""	for n in range(esimene_number, esimene_number + len(väärtused))]
    tulbad.categoryAxis.labels.fontName = "Helvetica"
    tulbad.categoryAxis.labels.fontSize = 6
    tulbad.categoryAxis.labels.angle = 0
    tulbad.categoryAxis.labels.boxAnchor = "n"
    tulbad.categoryAxis.labels.dx = 0
    tulbad.categoryAxis.labels.dy = -6
    tulbad.valueAxis.valueMin = 0
    tulbad.valueAxis.valueMax = ülempiir
    tulbad.valueAxis.valueStep = samm
    tulbad.valueAxis.labels.fontName = "Helvetica"
    tulbad.valueAxis.labels.fontSize = 7
    tulbad.barWidth = 2		# kitsad tulbad, et 1-75 mahuks ühele reale
    tulbad.barSpacing = 0
    tulbad.groupSpacing = 5
    tulbad.bars[0].fillColor = TULP
    tulbad.bars[0].strokeColor = TUMESININE
    tulbad.bars[0].strokeWidth = 0.15
    joonis.add(tulbad)
    return joonis
