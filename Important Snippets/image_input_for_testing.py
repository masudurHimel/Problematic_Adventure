import tempfile
from PIL import Image

RES = {}
image = Image.new('RGB', (100, 100))
tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
image.save(tmp_file)
with open(tmp_file.name, 'rb') as fp:
    RES['nid_front'] = fp
    RES['nid_back'] = fp
    RES['distributor_photo'] = fp