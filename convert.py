from argparse import ArgumentParser
import json
import sys

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
else:
    raise NotImplementedError(f'{args.format} is not a valid format for this converter')
