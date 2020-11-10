from pathlib import Path
from clldutils.misc import slug
from pylexibank.providers import abvd


class Dataset(abvd.BVD):
    dir = Path(__file__).parent
    id = "bantubvd"
    SECTION = "bantu"

    def cmd_makecldf(self, args):
        concepts = args.writer.add_concepts(
            id_factory=lambda c: c.id.split("-")[-1] + "_" + slug(c.english),
            lookup_factory=lambda c: c["ID"].split("_")[0],
        )

        for wl in self.iter_wordlists(args.log):
            wl.to_cldf(args.writer, concepts)

        # this removes the 'checkedby' column from the languages table as the
        # bantuBVD does not use this field, and it's therefore all empty.
        # ..and being all empty triggers a lexibank check warning later
        args.writer.cldf["LanguageTable"].tableSchema.columns = [
            col
            for col in args.writer.cldf["LanguageTable"].tableSchema.columns
            if col.name != "checkedby"
        ]
