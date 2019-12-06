from pathlib import Path
from clldutils.misc import slug
from pylexibank.providers import abvd


class Dataset(abvd.BVD):
    dir = Path(__file__).parent
    id = "bantubvd"
    SECTION = "bantu"

    def cmd_download(self, args):
        return  # no-op as data is stored locally.

    def cmd_makecldf(self, args):
        concepts = args.writer.add_concepts(
            id_factory=lambda c: c.id.split('-')[-1]+ '_' + slug(c.english),
            lookup_factory=lambda c: c['ID'].split('_')[0]
        )
        
        for wl in self.iter_wordlists(args.log):
            wl.to_cldf(args.writer, concepts)

