model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='vig',
        channels=320,
        k=9,
        act='gelu',
        norm='batch',
        bias=True,
        use_dilation=True,
        epsilon=0.2,
        use_stochastic=False,
        conv='mr',
        n_blocks=16,
        drop_path=0.0,
        dropout=0.0,
        n_classes=1000),
    head=dict(
        type='ClsHead',
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),
    ))