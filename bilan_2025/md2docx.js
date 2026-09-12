// Convertit POINTS_OUVERTS.md en .docx. Sous-ensemble de markdown réellement
// utilisé dans le fichier : deux niveaux de titre, listes à puces et
// numérotées avec continuations indentées, tableaux, gras et code inline.
const fs = require('fs');
const d = require('docx');
const {Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow,
       TableCell, WidthType, ShadingType, BorderStyle, AlignmentType,
       LevelFormat, PageNumber, Footer} = d;

const src = fs.readFileSync(process.argv[2], 'utf8').split('\n');
const OUT = process.argv[3];
const LARGEUR = 9360;                       // A4 moins les marges, en DXA

// --- gras et code inline -> suite de TextRun
function runs(txt, base = {}) {
  const out = [];
  const re = /\*\*(.+?)\*\*|`(.+?)`/g;
  let i = 0, m;
  while ((m = re.exec(txt)) !== null) {
    if (m.index > i) out.push(new TextRun({...base, text: txt.slice(i, m.index)}));
    if (m[1] !== undefined) out.push(new TextRun({...base, text: m[1], bold: true}));
    else out.push(new TextRun({...base, text: m[2], font: 'Consolas', size: 19}));
    i = m.index + m[0].length;
  }
  if (i < txt.length) out.push(new TextRun({...base, text: txt.slice(i)}));
  return out.length ? out : [new TextRun({...base, text: ''})];
}

const cellule = (txt, entete, largeur) => new TableCell({
  width: {size: largeur, type: WidthType.DXA},
  shading: entete ? {type: ShadingType.CLEAR, fill: 'E8EDF2'} : undefined,
  margins: {top: 60, bottom: 60, left: 110, right: 110},
  children: [new Paragraph({children: runs(txt, entete ? {bold: true} : {}),
                            spacing: {before: 0, after: 0}})],
});

function tableau(lignes) {
  const grille = lignes.map(l => l.replace(/^\||\|$/g, '').split('|').map(s => s.trim()));
  const corps = grille.filter(l => !l.every(c => /^:?-+:?$/.test(c)));
  const n = Math.max(...corps.map(l => l.length));
  const largeurs = Array(n).fill(Math.floor(LARGEUR / n));
  largeurs[0] += LARGEUR - largeurs.reduce((a, b) => a + b, 0);
  return new Table({
    columnWidths: largeurs,
    width: {size: LARGEUR, type: WidthType.DXA},
    rows: corps.map((l, i) => new TableRow({
      tableHeader: i === 0,
      children: largeurs.map((w, j) => cellule(l[j] || '', i === 0, w)),
    })),
  });
}

const enfants = [];
let i = 0;
while (i < src.length) {
  const l = src[i];

  if (l.startsWith('# ')) {
    enfants.push(new Paragraph({text: l.slice(2), heading: HeadingLevel.TITLE,
                                spacing: {after: 160}}));
    i++; continue;
  }
  if (l.startsWith('## ')) {
    enfants.push(new Paragraph({children: runs(l.slice(3)), heading: HeadingLevel.HEADING_1,
                                spacing: {before: 360, after: 140},
                                border: {bottom: {style: BorderStyle.SINGLE, size: 6,
                                                  color: 'B8C4D0', space: 6}}}));
    i++; continue;
  }
  if (l.startsWith('|')) {
    const bloc = [];
    while (i < src.length && src[i].startsWith('|')) bloc.push(src[i++]);
    enfants.push(tableau(bloc));
    enfants.push(new Paragraph({text: '', spacing: {after: 120}}));
    continue;
  }
  if (l.trim() === '') { i++; continue; }

  // puce, sous-puce, élément numéroté ou paragraphe — avec ses continuations
  let texte, type;
  if (/^- /.test(l))            { texte = l.slice(2);              type = 'puce'; }
  else if (/^  - /.test(l))     { texte = l.slice(4);              type = 'souspuce'; }
  else if (/^  \d+\. /.test(l)) { texte = l.replace(/^\s*\d+\.\s/, ''); type = 'num'; }
  else                          { texte = l;                       type = 'para'; }
  i++;
  const suite = (x) => x !== undefined && x.trim() !== '' && !x.startsWith('|') &&
                       !x.startsWith('#') && !/^- /.test(x) &&
                       !/^  - /.test(x) && !/^  \d+\. /.test(x);
  while (suite(src[i])) { texte += ' ' + src[i].trim(); i++; }
  if (type === 'para') {
    enfants.push(new Paragraph({children: runs(texte), spacing: {after: 120},
                                alignment: AlignmentType.JUSTIFIED}));
  } else {
    enfants.push(new Paragraph({
      children: runs(texte),
      numbering: {reference: type === 'num' ? 'chiffres' : 'puces',
                  level: type === 'souspuce' ? 1 : 0},
      spacing: {after: 100},
      alignment: AlignmentType.JUSTIFIED,
    }));
  }
}

const doc = new Document({
  creator: 'BV MT Cosmetics Belgium',
  title: 'Points à trancher avec BDH',
  styles: {
    default: {
      document: {run: {font: 'Calibri', size: 21}, paragraph: {spacing: {line: 276}}},
      title: {run: {font: 'Calibri', size: 36, bold: true, color: '1F3864'}},
      heading1: {run: {font: 'Calibri', size: 26, bold: true, color: '1F3864'}},
    },
  },
  numbering: {
    config: [
      {reference: 'puces', levels: [
        {level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
         style: {paragraph: {indent: {left: 360, hanging: 220}}}},
        {level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT,
         style: {paragraph: {indent: {left: 720, hanging: 220}}}},
      ]},
      {reference: 'chiffres', levels: [
        {level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
         style: {paragraph: {indent: {left: 720, hanging: 260}}}},
      ]},
    ],
  },
  sections: [{
    properties: {page: {margin: {top: 1100, bottom: 1100, left: 1080, right: 1080}}},
    footers: {default: new Footer({children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({children: [PageNumber.CURRENT], size: 18, color: '808080'})],
    })]})},
    children: enfants,
  }],
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log(OUT, b.length, 'octets'); });
