from dataset.synthetic_burst_val_set import SyntheticBurstVal
import tqdm
device = 'cuda'

if __name__ == '__main__':

    dataset = SyntheticBurstVal(root=r'F:\Dataset\BurstSR\burstSR_data\synthetic\SyntheticBurstVal')
    for idx in tqdm.tqdm(range(len(dataset))):
        burst, gt, meta_info = dataset[idx]
        burst_name = meta_info['burst_name']
        burst = burst.to(device).unsqueeze(0)
        gt = gt.to(device)