from pathlib import Path
import subprocess


ROOT = Path.cwd()
TMP = ROOT / "tmp" / "pdfs"
OUT = ROOT / "output" / "pdf"
TEX = TMP / "on-the-side-one-sheet.tex"
ROOT_PDF = ROOT / "OnTheSide-One-Sheet.pdf"
OUT_PDF = OUT / "OnTheSide-One-Sheet.pdf"


LATEX = r"""
\documentclass[letterpaper,10pt]{article}
\usepackage[margin=0.55in]{geometry}
\usepackage{graphicx}
\usepackage[table]{xcolor}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{tabularx}
\usepackage{pagecolor}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\newcommand{\displayfont}{\fontfamily{phv}\selectfont}
\newcommand{\bodyfont}{\fontfamily{ptm}\selectfont}
\definecolor{paper}{HTML}{F6F1E8}
\definecolor{ink}{HTML}{18181B}
\definecolor{muted}{HTML}{57534E}
\definecolor{accent}{HTML}{C77D2B}
\definecolor{accent2}{HTML}{A4442F}
\pagecolor{paper}
\color{ink}
\begin{document}
\bodyfont

\begin{center}
  \includegraphics[width=\textwidth,height=2.9in,keepaspectratio]{Band.JPG}
\end{center}

\vspace{-0.15in}

{\displayfont\fontsize{28}{30}\selectfont\bfseries ON THE SIDE\par}
{\color{accent}\displayfont\large Americana, roots rock, and classic rock from Sonoma County\par}

\vspace{0.12in}

\begin{minipage}[t]{0.58\textwidth}
{\displayfont\large\bfseries ABOUT\par}
{\color{muted}\small
On the Side brings together Americana warmth, rootsy grooves, and classic rock energy for wineries, restaurants, festivals, town events, and private gatherings across Sonoma and Marin.\par}

\vspace{0.12in}

{\displayfont\large\bfseries SOUND\par}
{\color{muted}\small
Crowd-friendly live sets with strong harmonies, relaxed feel, and a polished but down-to-earth stage presence.\par}

\vspace{0.12in}

{\displayfont\large\bfseries IDEAL FOR\par}
{\color{muted}\small
Wineries, pizza nights, tasting rooms, community events, private parties, and outdoor concerts.\par}

\vspace{0.12in}

{\displayfont\large\bfseries BOOKING\par}
{\color{muted}\small
Book through the contact form on the On the Side website for venue, festival, winery, and private event inquiries.\par}
\end{minipage}
\hfill
\begin{minipage}[t]{0.37\textwidth}
{\displayfont\large\bfseries UPCOMING SHOWS\par}
\renewcommand{\arraystretch}{1.15}
{\color{muted}\small
\begin{tabularx}{\linewidth}{@{}>{\bfseries}p{0.27\linewidth}X@{}}
Sep 10 & D'Argenzio Winery and Tasting Room, Santa Rosa \\
Oct 1 & D'Argenzio Winery and Tasting Room, Santa Rosa \\
Oct 8 & Sonoma Pizza Co, Forestville \\
Oct 31 & Graton Town Square Halloween, Graton \\
\end{tabularx}\par}

\vspace{0.16in}
\includegraphics[width=\linewidth,height=1.6in,keepaspectratio]{Steve_sonoma_pizza.JPG}

\vspace{0.12in}
\includegraphics[width=\linewidth,height=1.25in,keepaspectratio]{Devon and Jimmy.JPG}
\end{minipage}

\vfill

\noindent\textcolor{accent}{\rule{2.2in}{0.12in}}\hspace{0.18in}\textcolor{accent2}{\rule{2.2in}{0.12in}}

{\color{muted}\small Press photos included in the companion zip file and mirrored from the website gallery.\par}

\end{document}
"""


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    TEX.write_text(LATEX, encoding="utf-8")
    cmd = [
        "/Library/TeX/texbin/pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={TMP}",
        str(TEX),
    ]
    subprocess.run(cmd, check=True, cwd=ROOT)
    built_pdf = TMP / "on-the-side-one-sheet.pdf"
    ROOT_PDF.write_bytes(built_pdf.read_bytes())
    OUT_PDF.write_bytes(built_pdf.read_bytes())


if __name__ == "__main__":
    main()
