# coding=utf-8
from __future__ import unicode_literals, print_function

from clldutils.path import Path

from pylexibank.providers import abvd
from pylexibank.dataset import Metadata

SOURCES = {
    'bantu-1': ['maganga1992'],
    'bantu-2': ['khisa2000'],
    'bantu-3': ['gazania1996'],
    'bantu-4': ['mann1995'],
    'bantu-5': ['teildautrey1994', '46178'],
    'bantu-6': None,  # unable to identify
    'bantu-7': ['33386'],
    'bantu-8': ['botne1994'],
    'bantu-9': ['creissels1996'],
    'bantu-10': ['ngunga1997'],
}


class Dataset(abvd.BVD):
    dir = Path(__file__).parent
    id = 'bantubvd'
    SECTION = 'bantu'

    def cmd_download(self, **kw):
        return

    def cmd_install(self, **kw):
        concept_map = {
            c.attributes['url'].unsplit().split('v=')[1]: c.concepticon_id
            for c in self.conceptlist.concepts.values()}
        for c in self.concepts:
            concept_map[c['ID']] = c['CONCEPTICON_ID'] or None
        bibtexes = self.raw.read_bib()

        with self.cldf as ds:
            for wl in self.iter_wordlists({}, kw['log']):
                citekeys = SOURCES[wl.id]
                wl.to_cldf(
                    ds,
                    concept_map,
                    citekey=";".join(citekeys) if citekeys is not None else None,
                    source=None if citekeys is None
                    else [b for b in bibtexes if b.id in citekeys],
                    concept_key=None)
