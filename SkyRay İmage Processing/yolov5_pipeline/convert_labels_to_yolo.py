"""convert_labels_to_yolo.py
Convert labels.csv (filename,sequence,frame,x,y,w,h) to YOLO v5 txt format.
Usage: python convert_labels_to_yolo.py --labels /path/to/labels.csv --imdir /path/to/images --outdir /path/to/yolo_dataset
"""
import argparse, csv, os
from pathlib import Path

def convert(labels_csv, imgdir, outdir):
    imgdir = Path(imgdir); outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir/'images').mkdir(exist_ok=True)
    (outdir/'labels').mkdir(exist_ok=True)
    # read labels
    with open(labels_csv, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    # assume all images same size, infer from first image using PIL
    from PIL import Image
    if len(rows)==0:
        print('no rows')
        return
    first = imgdir / rows[0]['filename']
    w,h = Image.open(first).size
    for r in rows:
        src = imgdir / r['filename']
        dst_img = outdir/'images'/r['filename']
        if not dst_img.exists():
            # copy
            from shutil import copyfile
            copyfile(src, dst_img)
        # YOLO format: class x_center y_center width height (normalized)
        x = float(r['x']); y = float(r['y']); ww = float(r['w']); hh = float(r['h'])
        x_c = x + ww/2.0
        y_c = y + hh/2.0
        nx = x_c / w; ny = y_c / h; nw = ww / w; nh = hh / h
        label_fname = (outdir/'labels')/ (Path(r['filename']).stem + '.txt')
        with open(label_fname, 'w') as lf:
            lf.write(f"0 {nx:.6f} {ny:.6f} {nw:.6f} {nh:.6f}\n")
    print('converted', len(rows), 'labels to', outdir)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--labels', required=True)
    p.add_argument('--imdir', required=True)
    p.add_argument('--outdir', required=True)
    args = p.parse_args()
    convert(args.labels, args.imdir, args.outdir)
