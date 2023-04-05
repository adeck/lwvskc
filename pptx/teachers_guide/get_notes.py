#!/usr/bin/env python3
#
#   TODO -- add docstring
#   TODO -- use click
#

from sys import argv

from pptx import Presentation

notes_dict = {}

def main(pptx_path):
    prs = Presentation(pptx_path)
    for i, slide in enumerate(prs.slides):
        if not slide.has_notes_slide:
            continue
        cur_frame = slide.notes_slide.notes_text_frame
        if cur_frame.text.strip() == '':
            continue
        notes_dict[i] = cur_frame
#    for k, v in notes_dict.items():
#        print(f"slide {k} notes: {v.text}")
    print(f"{len(notes_dict)} of {len(prs.slides)} slides have text.")
    print(f"Specifically: {sorted(notes_dict.keys())}")


if __name__ == '__main__':
    assert len(argv) == 2
    pptx_path = argv[1]
    main(pptx_path)

