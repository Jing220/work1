conda create -n sbfburst python=3.10 -y
conda activate sbfburst
#pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.6 -c pytorch -c conda-forge

pip install mmcv==2.0.0 -f https://download.openmmlab.com/mmcv/dist/cu118/torch2.0/index.html
conda install -c conda-forge cupy==12.3.0 cuda-version=11.8
pip install -r requirements.txt