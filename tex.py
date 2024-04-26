snips = {
    'intro':
r"""\documentclass[11pt,a4paper,sans]{moderncv}

\moderncvstyle{classic}                             % style options are 'casual' (default), 'classic', 'banking', 'oldstyle' and 'fancy'
\moderncvcolor{green}                               % color options 'black', 'blue' (default), 'burgundy', 'green', 'grey', 'orange', 'purple' and 'red'
%\renewcommand{\familydefault}{\sfdefault}         % to set the default font; use '\sfdefault' for the default sans serif font, '\rmdefault' for the default roman one, or any tex font name
%\nopagenumbers{}                                  % uncomment to suppress automatic page numbering for CVs longer than one page

\usepackage[utf8]{inputenc}

\usepackage[scale=0.75,left=0.8in,right=0.8in,top=1in,bottom=1.5in]{geometry}
%\setlength{\hintscolumnwidth}{3cm}                % if you want to change the width of the column with the dates
%\setlength{\makecvtitlenamewidth}{10cm}           % for the 'classic' style, if you want to force the width allocated to your name and avoid line breaks. be careful though, the length is normally calculated to avoid any overlap with your personal info; use this at your own typographical risks...

\newcommand*{\cventrynocomma}[7][.25em]{%
  \cvitem[#1]{#2}{%
    {\bfseries#3}%
    \ifthenelse{\equal{#4}{}}{}{ {\slshape#4}}%
    \ifthenelse{\equal{#5}{}}{}{ #5}%
    \ifthenelse{\equal{#6}{}}{}{ #6}%
    \strut%
    \ifx&#7&%
      \else{\newline{}\begin{minipage}[t]{\linewidth}\small#7\end{minipage}}\fi}}
\setlength{\hintscolumnwidth}{2.4cm}

% personal data""",
    'documentStart':
r"""
\makeatletter\renewcommand*{\bibliographyitemlabel}{\@biblabel{\arabic{enumiv}}}\makeatother
%   to redefine the bibliography heading string ("Publications")
%\renewcommand{\refname}{Articles}

\begin{document}
\makecvtitle""",
    'biblio': r"""
\nocite{*}
\bibliographystyle{hunsrt}""",
    'end': r'\end{document}'
}
