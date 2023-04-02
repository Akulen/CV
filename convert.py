from argparse import ArgumentParser
import json
import re
import sys

def html2dash(s):
    return s.replace('--', '–')

def html3dash(s):
    return s.replace('---', '—')

def htmltexb(s):
    return re.sub("\\\\textbf{([^}]*)}", "<b>\\1</b>", s)

cnt = 0
def htmltexem(s):
    return re.sub("\\\\textit{([^}]*)}", "<em>\\1</em>", s)

def borderNotFirst(first):
    if first:
        return ""
    return " class='bordertop'"

def fand(s):
    if s == "":
        return ""
    return ", " + s

parser = ArgumentParser(
    prog='CV Converter',
    description='Converts `cv.json` to pdf or html'
)
parser.add_argument('format', nargs='?', default='pdf', help='Format to convert to. Either `pdf` or `html`')
args = parser.parse_args()

with open('cv.json', 'r') as f:
    cv = json.load(f)

if args.format == 'pdf':
    with open('cv.tex', 'w') as f:
        sys.stdout = f
        import tex
        print(tex.snips['intro'])

        print('\\name{' + cv['profile']['firstName'] + "}{" + cv['profile']['lastName'] + "}")
        print('\\address{' + cv['profile']['address']['road'] + "}{" + cv['profile']['address']['postCode'] + ' ' + cv['profile']['address']['city'] + ', ' + cv['profile']['address']['country'] + "}")
        print('\\phone[mobile]{' + cv['profile']['phone'] + '}')
        print('\\email{' + cv['profile']['email'] + '}')
        print('\\social[github]{' + cv['profile']['social']['github'] + '}')

        print(tex.snips['documentStart'])

        print('\n\\section{Education}')
        for ed in cv['education']:
            print('    \\cventry{' + ed['years'] + '}{' + ed['name'] + '}{' + ed['place'] + '}{' + ed['location'] + '}{}{}')

        print('\n\\section{Skills}')
        for tp, ls in cv['skills'].items():
            print('    \\cvitem{' + tp + '}{' + ', '.join(ls) + '}')

        print('\n\\section{Experience}')
        for exp in cv['experience']:
            print('    \\cvitem{' + exp['years'] + '}{' + exp['position'] + '}')
            if exp['description'] != '':
                print('    \\cvitem{}{' + exp['description'] + '}')

        print('\n\\section{Teaching}')
        for tea in cv['teaching']:
            if 'location' in tea:
                print('    \\cventry{' + tea['years'] + '}{' + tea['position'] + '}{' + tea['details'] + '}{' + tea['location'] + '}{}{}{}')
            else:
                print('    \\cventrynocomma{' + tea['years'] + '}{' + tea['position'] + '}{' + tea['details'] + '}{' + tea['contest'] + '}{}{}{}')

        print('\n\\section{Competitions and Awards}')
        for awa in cv['awards']:
            print('    \\cvitem{' + awa['year'] + '}{' + awa['rank'] + '}')

        print(tex.snips['biblio'])
        print('\\bibliography{' + cv['bibliography'] + '}')

        print('\n\\section{Language}')
        for lan in cv['language']:
            print('    \\cvitemwithcomment{' + lan['language'] + '}{' + lan['level'] + '}{' + lan['experience'] + '}')

        print(tex.snips['end'])
if args.format == 'html':
    with open('cv.html', 'w') as f:
        sys.stdout = f
        import html
        import tex
        print(html.sectionHead('Education'))
        for ed in cv['education']:
            print('    <tr>')
            print(f'      <th scope="row">{html2dash(ed["years"])}</th>')
            print(f'      <td><b>{html3dash(ed["name"])}</b>, <em>{ed["place"]}</em>{fand(ed["location"])}</li>')
            print('    </tr>')
        print(html.sectionEnd())

        print(html.sectionHead('Skills'))
        for tp, ls in cv['skills'].items():
            print('    <tr>')
            print(f'      <th scope="row">{tp}</th>')
            print(f'      <td>{", ".join(ls)}</td>')
            print('    </tr>')
        print(html.sectionEnd())

        print(html.sectionHead('Experience'))
        first = True
        for exp in cv['experience']:
            print(f'    <tr{borderNotFirst(first)}>')
            print(f'      <th scope="row">{html2dash(exp["years"])}</th>')
            print(f'      <td>{htmltexb(exp["position"])}</td>')
            print('    </tr>')
            if exp['description'] != '':
                print('    <tr>')
                print('      <th scope="row"></th>')
                print(f'      <td>{htmltexem(exp["description"])}</td>')
                print('    </tr>')
            first = False
        print(html.sectionEnd())

        print(html.sectionHead('Teaching'))
        for tea in cv['teaching']:
            print('    <tr>')
            print(f'      <th scope="row">{html2dash(tea["years"])}</th>')
            if 'location' in tea:
                print(f'      <td><b>{tea["position"]}</b>, <em>{tea["details"]}</em>, {tea["location"]}')
            else:
                print(f'      <td><b>{tea["position"]}</b> <em>{tea["details"]}</em> {tea["contest"]}')
            print('    </tr>')
        print(html.sectionEnd())

        print(html.sectionHead('Competitions and Awards'))
        for awa in cv['awards']:
            print('    <tr>')
            print(f'      <th scope="row">{html2dash(awa["year"])}</th>')
            print(f'      <td>{html3dash(awa["rank"])}</td>')
            print('    </tr>')
        print(html.sectionEnd())

        print(html.sectionHead('Publications'))
        # print(tex.snips['biblio'])
        # print('\\bibliography{' + cv['bibliography'] + '}')
        print(html.sectionEnd())

        print(html.sectionHead('Language'))
        for lan in cv['language']:
            print('    <tr>')
            print(f'      <th scope="row">{html2dash(lan["language"])}</th>')
            print(f'      <td>{lan["level"]}<span class="experience">{lan["experience"]}</span></td>')
            print('    </tr>')
        print(html.sectionEnd())
else:
    raise NotImplementedError(f'{args.format} is not a valid format for this converter')
