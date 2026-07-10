class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = './workspace'
        self.tensorboard_dir = self.workspace_dir + '/tensorboard/'  # Directory for tensorboard files.
        self.pretrained_nets_dir = './pretrained_networks'  # Directory for pre-trained networks.
        self.save_predictions_path = self.workspace_dir + '/saved_images'  # Directory for saving network predictions for evaluation.

        self.zurichraw2rgb_dir = '/data1/sr617/codes/wsy/dataset/BurstSR/syn/zurich-raw-to-rgb'     # Zurich RAW 2 RGB path
        self.synburstval_dir = '/data1/sr617/codes/wsy/dataset/BurstSR/syn/SyntheticBurstVal'       # SyntheticBurst validation set path
        self.burstsr_dir = '/data1/sr617/codes/wsy/dataset/BurstSR/burstsr'             # BurstSR dataset path
        self.rbsr_dir = '/data1/sr617/codes/wsy/dataset/BurstSR/realbsr'
