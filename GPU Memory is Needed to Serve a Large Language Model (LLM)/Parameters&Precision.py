from transformers import AutoProcessor, SeamlessM4Tv2Model
import torch
import torchaudio

processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")
# model = model.to(dtype=torch.bfloat16)


# Assuming 'model' is your loaded model
total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f'Total Parameters: {total_params / 1e9:.2f} Billion')
param_precision = model.parameters().__next__().dtype
print(f'Precision: {param_precision}')
