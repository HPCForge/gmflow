#C+B
python main.py --checkpoint_dir chairs_boil/ --resume pretrained/gmflow_chairs-1d776046.pth --stage boiling --batch_size 4 --num_workers 4  --lr 1e-6 --weight_decay 1e-6 --image_size 512 512  --val_freq 100 --val_dataset chairs things sintel kitti boiling  --save_ckpt_freq 100 --num_steps 2000
#C+T+B
python main.py --checkpoint_dir things_boil/ --resume pretrained/gmflow_things-e9887eda.pth --stage boiling --batch_size 4 --num_workers 4  --lr 1e-6 --weight_decay 1e-6 --image_size 512 512  --val_freq 100 --val_dataset chairs things sintel kitti boiling  --save_ckpt_freq 100 --num_steps 2000
#C+T+S+B
python main.py --checkpoint_dir sintel_boil/ --resume pretrained/gmflow_sintel-0c07dcb3.pth --stage boiling --batch_size 4 --num_workers 4  --lr 1e-6 --weight_decay 1e-6 --image_size 512 512  --val_freq 100 --val_dataset chairs things sintel kitti boiling  --save_ckpt_freq 100 --num_steps 2000
