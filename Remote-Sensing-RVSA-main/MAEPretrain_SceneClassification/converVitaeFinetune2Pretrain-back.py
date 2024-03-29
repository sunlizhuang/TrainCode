###逆过程
import torch
import torch.nn.functional as F
import argparse

parser = argparse.ArgumentParser('MAE pre-training convert checkpoint', add_help=False)
parser.add_argument('--pretrained', default='', type=str)
parser.add_argument('--out', default='', type=str)

args = parser.parse_args()

ckpt_transformed = torch.load('/Remote-Sensing-RVSA-main/ViT-retail/vitae-b-checkpoint-1599-new.pth', map_location='cpu')['model']

args.out = '/Remote-Sensing-RVSA-main/ViT-retail/vitae-b-checkpoint-1599-for-pretrain.pth'

newCkpt = {}

for key, value in ckpt_transformed.items():
    if 'PCM' in key and 'weight' in key:
        if len(value.shape) == 4 and value.shape[-1] == 3:
            value = value[:,:,1:-1,1:-1]
    newCkpt[key] = value

ckpt_transformed = {'model':newCkpt}
torch.save(ckpt_transformed, args.out)