from zipfile import ZipFile
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

feature_map_path = os.path.join(current_dir, 'featuremaps', 'src', 'featuremap.py')
zipObj = ZipFile(os.path.join(current_dir, 'PS1_submission.zip'), 'w')
zipObj.write(feature_map_path, os.path.basename(feature_map_path))
