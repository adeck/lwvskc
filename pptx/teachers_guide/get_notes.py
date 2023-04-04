#!/usr/bin/env python3
#
#   TODO
#

from pptx import Presentation

PPTX_PATH = "./TODO"

prs = Presentation(PPTX_PATH)

for i, slide in enumerate(prs.slides):
    print(i)
    if not slide.has_notes_slide:
        print(f"{i} has no notes")
        continue
    cur_notes_frame = slide.notes_slide.notes_text_frame
    print(f"{i} has notes: {cur_notes_frame}")
    print(f"{i} has notes text: {cur_notes_frame.text}")
    print(f"{i} has notes paragraphs:")
    for paragraph in cur_notes_frame.paragraphs:
        for run in paragraph.runs:
            print(run.text)


