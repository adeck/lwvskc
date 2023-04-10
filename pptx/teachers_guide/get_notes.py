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
    num_slides = len(prs.slides)
    for i, slide in enumerate(prs.slides):
        if not slide.has_notes_slide:
            continue
        cur_frame = slide.notes_slide.notes_text_frame
        if cur_frame.text.strip() == '':
            continue
        notes_dict[i] = cur_frame
#    for k, v in notes_dict.items():
#        print(f"slide {k} notes: {v.text}")
    print(f"{len(notes_dict)} of {num_slides} slides have text.")
    indices = [k + 1 for k in sorted(notes_dict.keys())]
    print(f"Specifically: {indices}")
    print("And in an easier to use format:")
    run_start = 1
    prev_i = -1
    for i in indices + [num_slides + 50]:
        if prev_i != i - 1:
            if run_start == prev_i:
                print(run_start)
            elif prev_i > 0:
                print(f"{run_start} - {prev_i}")
            run_start = i
        prev_i = i



if __name__ == '__main__':
    assert len(argv) == 2
    pptx_path = argv[1]
    main(pptx_path)

