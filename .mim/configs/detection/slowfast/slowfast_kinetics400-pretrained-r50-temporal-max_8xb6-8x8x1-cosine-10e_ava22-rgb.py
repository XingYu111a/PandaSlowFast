_base_ = [
    'slowfast_kinetics400-pretrained-r50_8xb8-8x8x1-20e_ava21-rgb.py'
# slowfast_kinetics400-pretrained-r50_8xb8-8x8x1-20e_ava21-rgb.py
]

model=dict(
    roi_head=dict(
        bbox_roi_extractor=dict(temporal_pool_mode='max')))
