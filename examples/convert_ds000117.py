"""
===============================
Create BIDS-compatible ds000117
===============================

Here, we show how to do BIDS conversion for group studies.
The data is available here: https://openfmri.org/dataset/ds000117/

References
----------

[1] Wakeman, Daniel G., and Richard N. Henson.
"A multi-subject, multi-modal human neuroimaging dataset."
Scientific data, 2 (2015): 150001.

"""

# Authors: Mainak Jas <mainak.jas@telecom-paristech.fr>
#          Teon Brooks <teon.brooks@gmail.com>

# License: BSD (3-clause)

###############################################################################
# Let us import ``mne_bids``

import os.path as op
from mne_bids import raw_to_bids
from mne_bids.datasets import fetch_faces_data

###############################################################################
# And fetch the data.

subject_ids = [1]
runs = range(1, 7)

data_path = op.join(op.expanduser('~'), 'mne_data')
repo = 'ds000117'
fetch_faces_data(data_path, repo, subject_ids)

output_path = op.join(data_path, 'ds000117-bids')

###############################################################################
#
# .. warning:: This will download 7.9 GB of data for one subject!
# Define event_ids.

event_id = {
    'face/famous/first': 5,
    'face/famous/immediate': 6,
    'face/famous/long': 7,
    'face/unfamiliar/first': 13,
    'face/unfamiliar/immediate': 14,
    'face/unfamiliar/long': 15,
    'scrambled/first': 17,
    'scrambled/immediate': 18,
    'scrambled/long': 19,
}

###############################################################################
# Let us loop over the subjects and create BIDS-compatible folder

for subject_id in subject_ids:
    subject = 'sub%03d' % subject_id
    for run in runs:
        raw_fname = op.join(data_path, repo, subject, 'MEG',
                            'run_%02d_raw.fif' % run)

        # Make it BIDS compatible
        raw_to_bids(subject_id='%02d' % subject_id, session_id='01', run=run,
                    task='visual_faces', raw_fname=raw_fname,
                    event_id=event_id, output_path=output_path, overwrite=True)
