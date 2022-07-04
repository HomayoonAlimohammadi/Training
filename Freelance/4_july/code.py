def longtidual(self):
    names = []
    for id in frames:
        tidy = [id]
        if tidy[:][0]["label"].startswith("B"):
            label = tidy[:][0]["label"]
            names.append(tidy[:][0]["id"])

    beam = []
    beam_first = []
    beam_end = []
    beam_middle = []
    dif_first_middle = []
    for id in range(len(names)):
        beam.append(self.etabs.DesignConcrete.GetSummaryResultsBeam(names[id])[1][1])
        beam_first.append(
            self.etabs.DesignConcrete.GetSummaryResultsBeam(names[id][4][0] * 100)
        )
        beam_end.append(
            self.etabs.DesignConcrete.GetSummaryResultsBeam(names[id][4][-1] * 100)
        )
        beam_middle.append(
            self.etabs.DesignConcrete.GetSummaryResultsBeam(names[id][4][4] * 100)
        )
        dif_first_middle.append((beam_first[id] - beam_middle[id]))

    return dif_first_middle
