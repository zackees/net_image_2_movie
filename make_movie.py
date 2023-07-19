
import os
import shutil

SELF_DIR = os.path.abspath(os.path.dirname(__file__))

jpg_SRC_DIR = os.path.join(SELF_DIR, 'data')

OUT_DIR = os.path.join(SELF_DIR, 'out')
jpg_OUT_DIR = os.path.join(OUT_DIR, 'jpg')
MP4_OUT_FILE = os.path.join(OUT_DIR, 'out.mp4')


def main():
	shutil.rmtree(OUT_DIR, ignore_errors=True)
	os.makedirs(jpg_SRC_DIR, exist_ok=True)
	os.makedirs(jpg_OUT_DIR, exist_ok=True)
	os.chdir(jpg_SRC_DIR)
	files = sorted(os.listdir())
	for i, src_f in enumerate(files):
		dst_f = os.path.join(jpg_OUT_DIR, 'image%05d.jpg' % i)
		print(f'Copying {src_f} -> {dst_f}')
		shutil.copy(src_f, dst_f)
	os.chdir(SELF_DIR)
	cmd = r'ffmpeg -loglevel error -hide_banner -f image2 -r 60 -i out/jpg/image%05d.jpg -c:v libx264 -y out/out.mp4'
	print(f'Executing: "{cmd}"')
	os.system(cmd)
	print('Wrote out/out.mp4')
	

if __name__ == '__main__':
	main()
